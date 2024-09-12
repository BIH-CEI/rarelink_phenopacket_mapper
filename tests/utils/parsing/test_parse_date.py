import pytest

from phenopacket_mapper.utils.parsing import parse_date


@pytest.mark.parametrize("date_str, expected", [
    (),
]
                         )
def test_parse_date(date_str, expected):
    assert parse_date(date_str) == expected
