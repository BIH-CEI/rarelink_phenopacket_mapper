from typing import Literal, List
import re

from phenopacket_mapper.data_standards import Coding, CodeSystem
from phenopacket_mapper.utils.parsing import get_codesystem_by_namespace_prefx

from phenopacket_mapper.data_standards import Coding, CodeSystem


def parse_coding(
        coding_str: str,
        resources: List[CodeSystem],
        compliance: Literal['soft', 'hard'] = 'soft'
) -> Coding:
    coding_str = coding_str.replace(" ", "")

    if ':' not in coding_str:
        raise ValueError("Invalid coding string, does not contain separator between code and name space prefix: "
                         f"{coding_str}")

    if not resources:
        raise ValueError("No resources provided.")
