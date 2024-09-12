import pytest

from phenopacket_mapper.data_standards import Date
from phenopacket_mapper.utils.parsing import parse_date


@pytest.mark.parametrize("date_str, expected", [
    ("2024-01-01", Date(day=1, month=1, year=2024)),
    ("1999/02/27", Date(day=27, month=2, year=1999)),
    ("03/31/1934", Date(day=31, month=3, year=1934)),
    ("04-13-2013", Date(day=13, month=4, year=2013)),
    ("27/05/1990", Date(day=27, month=5, year=1990)),
    ("19.06.2024", Date(day=19, month=6, year=2024)),
    ("20-07-2024", Date(day=20, month=7, year=2024)),
    ("2024-08", Date(month=8, year=2024)),
    ("2024/09", Date(month=9, year=2024)),
    ("2024.10", Date(month=10, year=2024)),
    ("11.2024", Date(month=11, year=2024)),
    ("12-2024", Date(month=12, year=2024)),
    ("01/2024", Date(month=1, year=2024)),
    ("2024", Date(year=2024)),
    ("2024-09-12 12:33:44", Date(second=44, minute=33, hour=12, day=12, month=9, year=2024)),
])
def test_parse_date_(date_str, expected):
    assert parse_date(date_str) == expected


@pytest.mark.parametrize("date_str, expected", [
    ("2024-1-01", Date(day=1, month=1, year=2024)),
    ("2024-01-1", Date(day=1, month=1, year=2024)),
    ("2024-1-1", Date(day=1, month=1, year=2024)),
    ("1999/2/27", Date(day=27, month=2, year=1999)),
    ("3/31/1934", Date(day=31, month=3, year=1934)),
    ("4-13-2013", Date(day=13, month=4, year=2013)),
    ("27/5/1990", Date(day=27, month=5, year=1990)),
    ("19.6.2024", Date(day=19, month=6, year=2024)),
    ("20-7-2024", Date(day=20, month=7, year=2024)),
    ("2024-8", Date(month=8, year=2024)),
    ("2024/9", Date(month=9, year=2024)),
    ("2024.10", Date(month=10, year=2024)),
    ("11.2024", Date(month=11, year=2024)),
    ("12-2024", Date(month=12, year=2024)),
    ("1/2024", Date(month=1, year=2024)),
    ("2024", Date(year=2024)),
    ("2024-9-12 12:33:44", Date(second=44, minute=33, hour=12, day=12, month=9, year=2024)),
])
def test_parse_date_irregularities(date_str, expected):
    assert parse_date(date_str) == expected
