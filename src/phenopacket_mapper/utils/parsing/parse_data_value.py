from typing import List, Literal, Union, Any

from phenopacket_mapper.data_standards import CodeSystem


def parse_single_data_value(
        value_str: str,
        resources: List[CodeSystem],
        compliance: Literal['soft', 'hard'] = 'soft'
) -> Union[Any, CodeSystem, type, str]:
    raise NotImplementedError
