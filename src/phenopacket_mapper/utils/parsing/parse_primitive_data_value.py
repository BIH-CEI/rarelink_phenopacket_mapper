from typing import Literal, Union


def parse_primitive_data_value(
        value_str: str,
        compliance: Literal['soft', 'hard'] = 'soft'
) -> Union[str, bool, int, float]:
    raise NotImplementedError
