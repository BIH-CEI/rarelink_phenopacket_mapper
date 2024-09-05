import datetime

import pytest

import rarelink_phenopacket_mapper as rlpm


@pytest.fixture
def example_date():
    return rlpm.data_standards.Date(
        year=2024,
        month=9,
        day=5,
        hour=11,
        minute=38,
        second=19
    )


@pytest.fixture
def example_datetime():
    year, month, day, hour, minute, second = 2024, 9, 5, 11, 38, 19
    return (
        datetime.datetime(year, month, day, hour, minute, second),
        rlpm.data_standards.Date(year, month, day, hour, minute, second)
    )


@pytest.mark.parametrize("fmt, result", [
    ("yyyy-mm-dd", "2024-09-05"),
    ("yyyy-mm", "2024-09"),
    ("yyyy", "2024"),
    ("yyyy-mm-dd hh:mm:ss", "2024-09-05 11:38:19"),
    ("iso", "2024-09-05T11:38:19Z"),
    ("iso8601", "2024-09-05T11:38:19Z")
])
def test_date_format(example_date, fmt, result):
    assert example_date.formatted_string(fmt) == result
