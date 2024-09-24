from dataclasses import dataclass, field
from typing import Any, List, Union

from phenopacket_mapper.data_standards import DataModelInstance, DataField


@dataclass(frozen=True, slots=True)
class PhenopacketElement:
    phenopacket_element: Any = field()
    elements: List[Union['PhenopacketElement', DataField]] = field()

    def map(self, instance: DataModelInstance):
        """Creates the phenopacket element by the mapping specified in fields

        >>> import phenopackets
        >>> from phenopacket_mapper.data_standards import DataModelInstance, DataModel, DataField, DataFieldValue
        >>> data_field = DataField("pseudonym", str)
        >>> data_model = DataModel("Example data model", [data_field], [])
        >>> inst = DataModelInstance(0, data_model, [DataFieldValue(0, data_field, "example_pseudonym")])
        >>> PhenopacketElement(phenopackets.Phenopacket, [MapField(data_field, "id")]).map(inst)
                id: "example_pseudonym"
                <BLANKLINE>

        :param instance: the ´DataModelInstance´ from which to map to a Phenopacket schema element
        :return: the resulting Phenopacket schema element
        """
        kwargs = {f.to_field: getattr(instance, f.from_field.id).value for f in self.elements}

        return self.phenopacket_element(**kwargs)
