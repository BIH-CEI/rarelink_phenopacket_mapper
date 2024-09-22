from dataclasses import dataclass, field
from typing import Any, List

from phenopacket_mapper.data_standards import DataModelInstance
from phenopacket_mapper.mapping import MapField


@dataclass(frozen=True, slots=True)
class PhenopacketElement:
    phenopacket_element: Any = field()
    fields: List[MapField] = field()

    def __post_init__(self):
        for f in self.fields:
            if not hasattr(self.phenopacket_element, f.to_field):
                raise AttributeError(f"The class: {self.phenopacket_element} has no attribute {f.to_field}")

    def map(self, instance: DataModelInstance):
        """Creates the phenopacket element by the mapping specified in fields

        >>> import phenopackets
        >>> from phenopacket_mapper.data_standards import DataModelInstance, DataModel, DataField, DataFieldValue
        >>> data_field = DataField("pseudonym", str)
        >>> data_model = DataModel("Example data model", [data_field], [])
        >>> inst = DataModelInstance(0, data_model, [DataFieldValue(0, data_field, "example_pseudonym")])
        >>> PhenopacketElement(phenopackets.Phenopacket, [MapField(data_field, "id")])
        {bla}

        :param instance: the ´DataModelInstance´ from which to map to a Phenopacket schema element
        :return: the resulting Phenopacket schema element
        """
        kwargs = {f.to_field: getattr(instance, f.from_field.id).value for f in self.fields}

        return self.phenopacket_element(**kwargs)
