import datetime

import pytest

import phenopacket_mapper as pm


@pytest.fixture
def example_date():
    return pm.data_standards.Date(
        year=2024,
        month=9,
        day=5,
        hour=11,
        minute=38,
        second=19
    )


@pytest.fixture
def example_date_iso8601():
    return "2024-09-05T11:38:19Z"


@pytest.fixture
def example_datetime():
    year, month, day, hour, minute, second = 2024, 9, 5, 11, 38, 19
    return (
        datetime.datetime(year, month, day, hour, minute, second),
        pm.data_standards.Date(year, month, day, hour, minute, second)
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


def test_iso_8601(example_date, example_date_iso8601):
    assert example_date.iso_8601_datestring() == example_date_iso8601


def test_from_iso8601(example_date, example_date_iso8601):
    assert pm.data_standards.Date.from_iso_8601(example_date_iso8601) == example_date


def test_from_date_time(example_datetime):
    assert pm.data_standards.Date.from_datetime(example_datetime[0]) == example_datetime[1]


@pytest.mark.parametrize(
    "year, month, day, hour, minute, second, raises_exc, exc",
    [
        # negative values
        (-1, 9, 5, 11, 38, 19, True, ValueError),
        (2024, -1, 5, 11, 38, 19, True, ValueError),
        (2024, 9, -1, 11, 38, 19, True, ValueError),
        (2024, 9, 5, -1, 38, 19, True, ValueError),
        (2024, 9, 5, 11, -1, 19, True, ValueError),
        (2024, 9, 5, 11, 38, -1, True, ValueError),
        # outside bounds: month and day
        (2024, 13, 5, 11, 38, 19, True, ValueError),
        (2024, 1, 31, 11, 38, 19, False, None),
        (2024, 1, 32, 11, 38, 19, True, ValueError),
        (2024, 2, 29, 11, 38, 19, False, None),
        (2025, 2, 29, 11, 38, 19, True, ValueError),
        (2024, 3, 31, 11, 38, 19, False, None),
        (2025, 3, 32, 11, 38, 19, True, ValueError),
        (2024, 4, 30, 11, 38, 19, False, None),
        (2025, 4, 31, 11, 38, 19, True, ValueError),
        (2024, 5, 31, 11, 38, 19, False, None),
        (2025, 5, 32, 11, 38, 19, True, ValueError),
        (2024, 6, 30, 11, 38, 19, False, None),
        (2025, 6, 31, 11, 38, 19, True, ValueError),
        (2024, 7, 31, 11, 38, 19, False, None),
        (2025, 7, 32, 11, 38, 19, True, ValueError),
        (2024, 8, 31, 11, 38, 19, False, None),
        (2025, 8, 32, 11, 38, 19, True, ValueError),
        (2024, 9, 30, 11, 38, 19, False, None),
        (2025, 9, 31, 11, 38, 19, True, ValueError),
        (2024, 10, 31, 11, 38, 19, False, None),
        (2025, 10, 32, 11, 38, 19, True, ValueError),
        (2024, 11, 30, 11, 38, 19, False, None),
        (2025, 11, 31, 11, 38, 19, True, ValueError),
        (2024, 12, 31, 11, 38, 19, False, None),
        (2025, 12, 32, 11, 38, 19, True, ValueError),
        # outside bounds: hour, minute, second
        (2024, 9, 5, 24, 38, 19, True, ValueError),
        (2024, 9, 5, 11, 60, 19, True, ValueError),
        (2024, 9, 5, 11, 38, 60, True, ValueError),
    ]
)
def test_invalid_values(
        year: int, month: int, day: int,
        hour: int, minute: int, second: int,
        raises_exc: bool, exc: type):
    if raises_exc:
        with pytest.raises(exc):
            pm.data_standards.Date(year, month, day, hour, minute, second)
