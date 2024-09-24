from typing import List, Union, Dict

from phenopackets import Phenopacket

from phenopacket_mapper.data_standards import CodeSystem
from phenopacket_mapper.data_standards.data_model import DataModel, DataSet, DataField, DataFieldValue
from phenopacket_mapper.mapping import PhenopacketElement


class PhenopacketMapper:
    """Class to map data to Phenopackets

    :ivar data_set: The data set to map to Phenopackets
    :ivar elements: List of PhenopacketElements to map the data to Phenopackets
    """

    def __init__(self, data_model: DataModel, resources: List[CodeSystem], **kwargs):
        """Create a PhenopacketMapper, this method is equivalent to the constructor of the ´Phenopacket´ for the mapping

        List fields of the ´Phenopacket´ constructor in the kwargs to map the data to Phenopackets.

        :param data_model: The data model to map to Phenopackets
        :param kwargs: The elements to map the data to Phenopackets
        """
        self.data_model = data_model
        self.elements: Dict[str, Union[PhenopacketElement, DataField]] = {}
        self.resources = resources
        for k, v in kwargs.items():
            setattr(self, k, v)
            self.elements[k] = v

        self.__post_init__()

    def __post_init__(self):
        # Check if the fields in the mapping are in the data model
        for e in self.elements.values():
            self.check_data_fields_in_model(e)

    def check_data_fields_in_model(self, element: Union[PhenopacketElement, DataField]):
        if isinstance(element, DataField):
            field = element
            if field not in self.data_model:
                raise AttributeError(f"The mapping definition contains an invalid field. "
                                     f"{field} is not in the data model underlying the passed data set."
                                     f" (The data model includes the fields: {self.data_model.get_field_ids()})")
        elif isinstance(element, PhenopacketElement):
            for key, ee in element.elements.items():
                self.check_data_fields_in_model(ee)

    def map(self, data: DataSet) -> List[Phenopacket]:
        """Map data from the DataModel to Phenopackets

        The mapping is based on the definition of the DataModel and the parameters passed to the constructor.

        If successful, a list of Phenopackets will be returned

        :param data: List of DataModelInstances created from the data using the DataModel
        :return: List of Phenopackets
        """
        phenopackets_list = []
        for instance in data:
            kwargs = {}
            for key, e in self.elements.items():
                if isinstance(e, DataField):
                    data_field = e
                    try:
                        value: DataFieldValue = getattr(instance, data_field.id).value
                        kwargs[key] = value
                    except AttributeError:
                        continue
                elif isinstance(e, PhenopacketElement):
                    phenopacket_element = e
                    kwargs[key] = phenopacket_element.map(instance)
            # TODO: Add the resources to the phenopacket
            try:
                phenopackets_list.append(
                    Phenopacket(
                        **kwargs
                    )
                )
            except TypeError as e:
                raise TypeError(f"Error in mapping: {e}")
            except Exception as e:
                raise e

        return phenopackets_list
