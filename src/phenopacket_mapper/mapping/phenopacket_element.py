from typing import Union, Dict

from phenopacket_mapper.data_standards import DataModelInstance, DataField, DataFieldValue


class PhenopacketElement:

    def __init__(self, phenopacket_element, **kwargs):
        """Mapping equivalent to the constructor of a Phenopacket element (e.g., Individual) for the mapping

        List fields of the Phenopacket element constructor in the kwargs to map the data to Phenopackets.

        :param phenopacket_element: The phenopacket element to map to (e.g., `phenopackets.Individual`)
        :param kwargs: The elements to map the data to Phenopackets
        """
        self.phenopacket_element = phenopacket_element
        self.elements: Dict[str, Union[PhenopacketElement, DataField]] = {}
        for k, v in kwargs.items():
            setattr(self, k, v)
            self.elements[k] = v

    def map(self, instance: DataModelInstance):
        """Creates the phenopacket element by the mapping specified in fields

        >>> import phenopackets
        >>> from phenopacket_mapper.data_standards import DataModelInstance, DataModel, DataField, DataFieldValue
        >>> data_field = DataField("pseudonym", str)
        >>> data_model = DataModel("Example data model", [data_field], [])
        >>> inst = DataModelInstance(0, data_model, [DataFieldValue(0, data_field, "example_pseudonym")])
        >>> individual = PhenopacketElement(phenopackets.Individual, id=data_field).map(inst)
        >>> individual.id
        "example_pseudonym"

        :param instance: the ´DataModelInstance´ from which to map to a Phenopacket schema element
        :return: the resulting Phenopacket schema element
        """
        kwargs = {}
        for key, e in self.elements.items():
            if isinstance(e, DataField):
                df = e
                try:
                    value: DataFieldValue = getattr(instance, df.id).value
                    kwargs[key] = value
                except AttributeError:
                    continue
            elif isinstance(e, PhenopacketElement):
                phenopacket_element = e
                kwargs[key] = phenopacket_element.map(instance)

        return self.phenopacket_element(**kwargs)
