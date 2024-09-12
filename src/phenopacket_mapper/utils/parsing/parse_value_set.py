from typing import List, Literal

from phenopacket_mapper.data_standards import CodeSystem, HPO, SNOMED_CT
from phenopacket_mapper.data_standards.code_system import ICD9
from phenopacket_mapper.utils.parsing import parse_single_data_type, parse_value
from phenopacket_mapper.data_standards.value_set import ValueSet


def parse_value_set(
        value_set_str: str,
        value_set_name: str = "",
        value_set_description: str = "",
        resources: List[CodeSystem] = None,
        compliance: Literal['soft', 'hard'] = 'soft',
) -> ValueSet:
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
    value_set_str = value_set_str.strip()

    if resources is None:
        resources = []

    elements_str = value_set_str.split(",")

    elements = []
    for element_str in elements_str:
        # parsing as a data type
        try:
            # compliance is set to 'hard' because we want to raise an error if the element is not recognized
            element = parse_single_data_type(type_str=element_str, resources=resources, compliance='hard')
        except ValueError:  # parsing as type failed, parsing as a value
            element = parse_value(value_str=element_str, resources=resources)

        elements.append(element)

        return ValueSet(name=value_set_name, elements=elements, description=value_set_description)