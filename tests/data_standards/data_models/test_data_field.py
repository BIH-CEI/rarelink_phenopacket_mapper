import pytest

from build.lib.phenopacket_mapper.data_standards import ValueSet
from phenopacket_mapper.data_standards import DataField

@pytest.fixture
def name():
    return "name"

@pytest.mark.parametrize("viable_values, expected", [
    (str, ValueSet([str])),
    ([str, int], ValueSet([str, int])),
    (ValueSet([str, int]), ValueSet([str, int])),
])
def test_data_field_constructor(name, viable_values, expected):
    assert DataField(name=name, viable_values=viable_values).viable_values.elements == expected.elements