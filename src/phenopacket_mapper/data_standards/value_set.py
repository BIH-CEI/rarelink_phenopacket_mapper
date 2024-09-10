from dataclasses import dataclass
from typing import List, Union

from phenopacket_mapper.data_standards import Coding, CodeableConcept, CodeSystem, Date


@dataclass(slots=True, frozen=True)
class ValueSet:
    name: str
    elements: List[Union[Coding, CodeableConcept, CodeSystem, str, bool, int, float, Date, type]]
    description: str = ""
