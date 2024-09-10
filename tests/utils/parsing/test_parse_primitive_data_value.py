import pytest

from phenopacket_mapper.utils.parsing import parse_data_type


@pytest.mark.parametrize("value_str, expected", [
    [" 1", 1],
    ["2", 2],
    ["3 ", 3],
    [" 4 ", 4],
    [" 5.6", 5.6],
    ["7.89", 7.89],
    ["10.11 ", 10.11],
    [".1", 0.1],
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
    ["word", "word"],
])
def test_parse_data_type(value_str, expected):
    assert parse_data_type(value_str, []) == expected
