from dataclasses import dataclass
from typing import List, Union, Literal

from phenopacket_mapper.data_standards import CodeSystem


@dataclass(frozen=True, slots=True)
class Coding:
    """
    Data class for Code
    """
    system: Union[str, CodeSystem]
    code: str
    display: str = None
    text: str = None

    @staticmethod
    def parse_parse_coding(
            coding_str: str,
            resources: List[CodeSystem],
            compliance: Literal['soft', 'hard'] = 'soft'
    ) -> 'Coding':
        """Parsed a string representing a coding to a Coding object

        Expected format: <namespace_prefix>:<code>

        E.g.:
        >>> parse_coding("SNOMED:404684003", [code_system_module.SNOMED_CT])
        Coding(system=CodeSystem(name=SNOMED CT, name space prefix=SNOMED, version=0.0.0), code='404684003', display=None, text=None)

        Intended to be called with a list of all resources used.

        Can only recognize the name space prefixes that belong to code systems provided in the resources list. If a name
        space is not found in the resources, it will return a Coding object with the system as the name space prefix and the
        code as the code.

        E.g.:
        >>> parse_coding("SNOMED:404684003", [])
        Warning: Code system with namespace prefix 'SNOMED' not found in resources.
        Warning: Returning Coding object with system as namespace prefix and code as '404684003'
        Coding(system='SNOMED', code='404684003', display=None, text=None)

        :param coding_str: a string representing a coding
        :param resources: a list of all resources used
        :param compliance: whether to throw a ValueError or just a warning if a name space prefix is not found in the
        resources
        :return: a Coding object as specified in the coding string
        """
        from phenopacket_mapper.utils.parsing import parse_coding
        return parse_coding(coding_str, resources, compliance)


@dataclass(frozen=True, slots=True)
class CodeableConcept:
    """
    Data class for CodeableConcept
    """
    coding: List[Coding]
    text: str = None
