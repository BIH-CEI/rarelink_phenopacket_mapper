from dataclasses import dataclass
from typing import List, Union

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


@dataclass(frozen=True, slots=True)
class CodeableConcept:
    """
    Data class for CodeableConcept
    """
    coding: List[Coding]
    text: str = None
