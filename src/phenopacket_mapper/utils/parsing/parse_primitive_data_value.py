from typing import List, Literal, Union, Any

from phenopacket_mapper.data_standards import CodeSystem, Date


def parse_single_data_value(
        value_str: str,
        resources: List[CodeSystem],
        compliance: Literal['soft', 'hard'] = 'soft'
) -> Union[str, bool, int, float, Date, type]:
    raise NotImplementedError
