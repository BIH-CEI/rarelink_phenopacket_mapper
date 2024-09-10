from typing import Literal, List
import re

from phenopacket_mapper.data_standards import Coding, CodeSystem
from phenopacket_mapper.utils.parsing import get_codesystem_by_namespace_prefx


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

    pattern = r'^(.*?):(.*)$'

    match = re.match(pattern, coding_str)

    if match:
        namespace_prefix = match.group(1)  # Part before the colon
        code = match.group(2)  # Part after the colon

        code_system = get_codesystem_by_namespace_prefx(namespace_prefix, resources)

        if code_system:
            return Coding(system=code_system, code=code)
        else:
            if compliance == 'hard':
                raise ValueError(f"Code system with namespace prefix '{namespace_prefix}' not found in resources.")
            else:
                print(f"Warning: Code system with namespace prefix '{namespace_prefix}' not found in resources.")
                coding = Coding(system=namespace_prefix, code=code)
                print(f"Warning: Returning Coding object with system as namespace prefix and code as '{code}'")
                return coding

    else:
        raise ValueError(f"Invalid coding string: {coding_str}")
