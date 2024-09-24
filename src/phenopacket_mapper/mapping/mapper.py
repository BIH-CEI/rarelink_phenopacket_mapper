from pathlib import Path
from typing import List, Union

from phenopackets import Phenopacket

from phenopacket_mapper.data_standards.data_model import DataModel, DataSet, DataField
from phenopacket_mapper.mapping import PhenopacketElement


class PhenopacketMapper:
    """Class to map data to Phenopackets

    :ivar data_set: The data set to map to Phenopackets
    :ivar elements: List of PhenopacketElements to map the data to Phenopackets
    """

    def __init__(self, data_model: DataModel, **kwargs):
        """Create a PhenopacketMapper, this method is equivalent to the constructor of the ´Phenopacket´ for the mapping

        List fields of the ´Phenopacket´ constructor in the kwargs to map the data to Phenopackets.

        :param data_model: The data model to map to Phenopackets
        :param kwargs: The elements to map the data to Phenopackets
        """
        self.data_set = data_model
        self.elements: List[Union[PhenopacketElement, DataField]] = []
        for k, v in kwargs:
            setattr(self, k, v)
            self.elements.append(v)

        self.__post_init__()

    def __post_init__(self):
        # Check if the fields in the mapping are in the data model
        for e in self.elements:
            self.check_data_fields_in_model(e)

    def check_data_fields_in_model(self, element: Union[PhenopacketElement, DataField]):
        dm = self.data_set.data_model
        if isinstance(element, DataField):
            field = element
            if field not in dm:
                raise AttributeError(f"The mapping definition contains an invalid field. "
                                     f"{field} is not in the data model underlying the passed data set."
                                     f" (The data model includes the fields: {dm.get_field_ids()})")
        elif isinstance(element, PhenopacketElement):
            for ee in element.elements:
                self.check_data_fields_in_model(ee)

    def map(self, data: DataSet) -> List[Phenopacket]:
        """Map data from the DataModel to Phenopackets

        The mapping is based on the definition of the DataModel and the DataModel2PhenopacketSchema mapping.

        If successful, a list of Phenopackets will be returned

        :param mapping_: Mapping from the DataModel to the Phenopacket schema, defined in DataModel2PhenopacketSchema
        :param data: List of DataModelInstances created from the data using the DataModel
        :return: List of Phenopackets
        """
        phenopackets_list = []
        for instance in data:
            phenopacket_elements = [phenopacket_element.map(instance) for phenopacket_element in self.elements]
            kwargs = {}
            # TODO: implement filling out of constructor of the phenopacket
            phenopackets_list.append(Phenopacket(

            ))
        return phenopackets_list

    def write(self, phenopackets: List[Phenopacket], output_path: Union[str, Path]) -> bool:
        """Write Phenopackets to a file

        :param phenopackets: List of Phenopackets to write
        :param output_path: Path to write the Phenopackets to
        :return: True if successful, False otherwise
        """
        raise NotImplementedError
