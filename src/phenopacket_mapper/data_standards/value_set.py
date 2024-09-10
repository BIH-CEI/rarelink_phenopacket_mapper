from dataclasses import dataclass
from typing import List, Union

from phenopacket_mapper.data_standards import Coding, CodeableConcept, CodeSystem, Date


@dataclass(slots=True, frozen=True)
class ValueSet:
    name: str
    elements: List[Union[Coding, CodeableConcept, CodeSystem, str, bool, int, float, Date, type]]
    description: str = ""

    def extend(self, new_name: str, value_set: 'ValueSet', new_description: str) -> 'ValueSet':
        return ValueSet(name=new_name,
                        elements=list(set(self.elements + value_set.elements)),
                        description=new_description)

