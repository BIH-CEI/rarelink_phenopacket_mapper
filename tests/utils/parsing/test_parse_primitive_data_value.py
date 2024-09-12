import pytest

from phenopacket_mapper.utils.parsing import parse_primitive_data_value, parse_int, parse_float


@pytest.mark.parametrize("value_str, expected", [
    # int
    [" 1", 1],
    ["2", 2],
    ["3 ", 3],
    [" 4 ", 4],
    ["- 5", -5],
    [" - 6", -6],
    ["-7", -7],
    # float
    [" 5.6", 5.6],
    ["7.89", 7.89],
    ["10.11 ", 10.11],
    [" 134560.1079841 ", 134560.1079841],
    [".1", 0.1],
    ["- 5.6", -5.6],
    ["-7.89", -7.89],
    ["-10.11 ", -10.11],
    [" -134560.1079841 ", -134560.1079841],
    ["-.1", -0.1],
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


@pytest.mark.parametrize("value_str, expected", [
    ("1", 1),
    ("-3248", -3248),
    ("234678", 234678),
    ("0", 0),
    ("0.1", None),
    ("wordle", None),
    ("True", None),
    ("False", None),
    ("t", None),
    ("f", None),
    ("T", None),
    ("F", None),
    ("", None),
    (" ", None),
    ("  ", None),
    ("   ", None),
])
def test_parse_int(value_str, expected):
    assert parse_int(value_str) == expected


@pytest.mark.parametrize("value_str, expected", [
    ("1.02", 1.02),
    ("234678.123456", 234678.123456),
    ("-3248.123", -3248.123),
    ("0.0", 0.0),
    ("0", 0.0),
    ("-.578483", -0.578483),
    (".3784", 0.3784),
    ("wordle", None),
    ("True", None),
    ("False", None),
    ("t", None),
    ("f", None),
    ("T", None),
    ("F", None),
    ("", None),
    (" ", None),
    ("  ", None),
    ("   ", None),
    ("1", 1.0),
    ("-20", -20.0),
])
def test_parse_float(value_str, expected):
    assert parse_float(value_str) == expected
