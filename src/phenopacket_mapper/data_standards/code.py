from dataclasses import dataclass
from typing import List


@dataclass(frozen=True, slots=True)
class Coding:
    """
    Data class for Code
    """
    system: str
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
