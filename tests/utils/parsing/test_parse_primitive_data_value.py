import pytest

from phenopacket_mapper.utils.parsing import parse_primitive_data_value


@pytest.mark.parametrize("value_str, expected", [
    # int
    [" 1", 1],
    ["2", 2],
    ["3 ", 3],
    [" 4 ", 4],
    # float
    [" 5.6", 5.6],
    ["7.89", 7.89],
    ["10.11 ", 10.11],
    [" 134560.1079841 ", 134560.1079841],
    [".1", 0.1],
    # bool
    ["True", True],
    [" True", True],
    ["True ", True],
    [" True ", True],
    ["False", False],
    [" False", False],
    ["False ", False],
    [" False ", False],
    ["true", True],
    ["false", False],
    ["t", True],
    ["f", False],
    ["T", True],
    ["F", False],
    # str
    ["word", "word"],
])
def test_parse_data_type(value_str, expected):
    assert parse_primitive_data_value(value_str) == expected
