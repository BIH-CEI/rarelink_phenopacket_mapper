from dataclasses import dataclass
from pathlib import Path
from typing import List, Union, Literal

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

    @staticmethod
    def parse_value_set(
            value_set_str: str,
            value_set_name: str,
            value_set_description: str,
            resources: List[CodeSystem],
            parse_data_types: bool = False,
            compliance: Literal['soft', 'hard'] = 'soft',
            remove_line_breaks: bool = False,
            parse_ordinals: bool = True,
    ) -> 'ValueSet':
        """Reads a value set from a file"""
        # TODO
        raise NotImplementedError


TRUE_FALSE_VALUE_SET = ValueSet(name="TrueFalseValueSet",
                                elements=[True, False],
                                description="A value set for True and False")

UNKNOWN_VALUE_SET = ValueSet(name="UnknownValueSet",
                             elements=["unknown"],
                             description="A value set for Unknown")

TRUE_FALSE_UNKNOWN_VALUE_SET = TRUE_FALSE_VALUE_SET.extend(new_name="TrueFalseUnknownValueSet",
                                                           value_set=UNKNOWN_VALUE_SET,
                                                           new_description="A value set for True, False, and Unknown")
