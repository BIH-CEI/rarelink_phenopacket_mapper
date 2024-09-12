from dataclasses import dataclass
from typing import List, Union, Literal

from phenopacket_mapper.data_standards import Coding, CodeableConcept, CodeSystem, Date
from phenopacket_mapper.utils.parsing.parse_value_set import parse_value_set


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
            value_set_description: str = "",
            resources: List[CodeSystem] = None,
            compliance: Literal['soft', 'hard'] = 'soft',
    ) -> 'ValueSet':
        """Parses a value set from a string representation

        >>> ValueSet.parse_value_set("True, False", "TrueFalseValueSet", "A value set for True and False", [])
        ValueSet(name="TrueFalseValueSet", elements=[True, False], description="A value set for True and False")

        :param value_set_str: String representation of the value set
        :param value_set_name: Name of the value set
        :param value_set_description: Description of the value set
        :param resources: List of CodeSystems to use for parsing the value set
        :param compliance: Compliance level for parsing the value set
        :return: A ValueSet object as defined by the string representation
        """
        return parse_value_set(
            value_set_str=value_set_str,
            value_set_name=value_set_name,
            value_set_description=value_set_description,
            resources=resources,
            compliance=compliance,
        )


TRUE_FALSE_VALUE_SET = ValueSet(name="TrueFalseValueSet",
                                elements=[True, False],
                                description="A value set for True and False")

UNKNOWN_VALUE_SET = ValueSet(name="UnknownValueSet",
                             elements=["unknown"],
                             description="A value set for Unknown")

TRUE_FALSE_UNKNOWN_VALUE_SET = TRUE_FALSE_VALUE_SET.extend(new_name="TrueFalseUnknownValueSet",
                                                           value_set=UNKNOWN_VALUE_SET,
                                                           new_description="A value set for True, False, and Unknown")
