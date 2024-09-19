import pytest

from phenopacket_mapper.data_standards import code_system, Date
from phenopacket_mapper.utils.parsing import parse_value


@pytest.fixture
def resources():
    return [
        code_system.SNOMED_CT,
        code_system.HPO
    ]


@pytest.mark.parametrize("value, expected", [
    ("02.2002", Date(year=2002, month=2)),
    ("2.2002", Date(year=2002, month=2)),
])
def test_parse_value(value, expected, resources):
    assert parse_value(value, resources) == expected
