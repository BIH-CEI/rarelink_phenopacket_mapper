from typing import Literal, List

from phenopacket_mapper.data_standards import Coding, CodeSystem


def parse_coding(
        coding_str: str,
        resources: List[CodeSystem],
        compliance: Literal['soft', 'hard'] = 'soft'
) -> Coding:
    raise NotImplementedError
