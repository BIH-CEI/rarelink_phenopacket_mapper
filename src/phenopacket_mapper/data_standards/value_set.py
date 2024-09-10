from dataclasses import dataclass
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
        if resources is None:
            resources = []

        value_set_str = value_set_str.replace(" ", "")  # Remove spaces

        elements_str = value_set_str.split(",")

        elements = []
        for element_str in elements_str:
            try:  # parsing as a data type
                # compliance is set to 'hard' because we want to raise an error if the element is not recognized
                element = parse_single_data_type(type_str=element_str, resources=resources, compliance='hard')
            except ValueError:  # parsing as a data type failed, try parsing as a value
                try:
                    element = parse_single_data_type(type_str=element_str, resources=resources, compliance='hard')
                except ValueError:  # could not parse as a value or type, leaving as a string
                    element = element_str

            elements.append(element)

        return ValueSet(name=value_set_name, elements=elements, description=value_set_description)


TRUE_FALSE_VALUE_SET = ValueSet(name="TrueFalseValueSet",
                                elements=[True, False],
                                description="A value set for True and False")

UNKNOWN_VALUE_SET = ValueSet(name="UnknownValueSet",
                             elements=["unknown"],
                             description="A value set for Unknown")

TRUE_FALSE_UNKNOWN_VALUE_SET = TRUE_FALSE_VALUE_SET.extend(new_name="TrueFalseUnknownValueSet",
                                                           value_set=UNKNOWN_VALUE_SET,
                                                           new_description="A value set for True, False, and Unknown")
