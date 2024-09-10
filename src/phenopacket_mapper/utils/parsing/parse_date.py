from typing import Literal

from phenopacket_mapper.data_standards import Date


def parse_date(
        date_str: str,
        compliance: Literal['soft', 'hard'] = 'soft'
) -> Date:
    raise NotImplementedError
