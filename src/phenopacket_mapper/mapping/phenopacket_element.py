from typing import Union, Dict

from phenopacket_mapper.data_standards import DataModelInstance, DataField


class PhenopacketElement:

    def __init__(self, phenopacket_element, **kwargs):
        """Mapping equivalent to the constructor of a Phenopacket element (e.g., Individual) for the mapping

        List fields of the Phenopacket element constructor in the kwargs to map the data to Phenopackets.

        :param phenopacket_element: The phenopacket element to map to (e.g., `phenopackets.Individual`)
        :param kwargs: The elements to map the data to Phenopackets
        """
        self.phenopacket_element = phenopacket_element
        self.elements: Dict[str, Union[PhenopacketElement, DataField]] = {}
        for k, v in kwargs:
            setattr(self, k, v)
            self.elements[k] = v

    def map(self, instance: DataModelInstance):
        """Creates the phenopacket element by the mapping specified in fields

        >>> import phenopackets
        >>> from phenopacket_mapper.data_standards import DataModelInstance, DataModel, DataField, DataFieldValue
        >>> data_field = DataField("pseudonym", str)
        >>> data_model = DataModel("Example data model", [data_field], [])
        >>> inst = DataModelInstance(0, data_model, [DataFieldValue(0, data_field, "example_pseudonym")])
        >>> PhenopacketElement(phenopackets.Individual, id=data_field).map(inst)
                id: "example_pseudonym"
                <BLANKLINE>

        :param instance: the ´DataModelInstance´ from which to map to a Phenopacket schema element
        :return: the resulting Phenopacket schema element
        """
        kwargs = {}
        for key, e in self.elements.items():
            if isinstance(e, DataField):
                kwargs[key] = e
            elif isinstance(e, PhenopacketElement):
                kwargs[key] = e.map(instance)

        return self.phenopacket_element(**kwargs)
