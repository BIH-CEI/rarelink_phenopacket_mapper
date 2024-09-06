import pytest

from phenopacket_mapper.utils.parsing import parse_ordinal


@pytest.mark.parametrize(
    "field_name, result", [
        ("1.1. Pseudonym", ("1.1", "Pseudonym")),
        ("2.1. Date of Birth", ("2.1", "Date of Birth")),
        ("2.2. Sex", ("2.2", "Sex")),
        ("3.1. Patient's status", ("3.1", "Patient's status")),
        ("3.2. Date of death", ("3.2", "Date of death")),
        ("4.1. First contact with specialised centre", ("4.1", "First contact with specialised centre")),
        ("5.1. Age at onset", ("5.1", "Age at onset")),
        ("5.2. Age at diagnosis", ("5.2", "Age at diagnosis")),
        ("6.1. Diagnosis of the rare disease", ("6.1", "Diagnosis of the rare disease")),
        ("6.2. Genetic diagnosis", ("6.2", "Genetic diagnosis")),
        ("6.3. Undiagnosed case", ("6.3", "Undiagnosed case")),
        ("1.1 Pseudonym", ("1.1", "Pseudonym")),
        ("1. Pseudonym", ("1", "Pseudonym")),
        ("1 Pseudonym", ("1", "Pseudonym")),
        ("I.a. Pseudonym", ("I.a", "Pseudonym")),
        ("I.a Pseudonym", ("I.a", "Pseudonym")),
        ("ii. Pseudonym", ("ii", "Pseudonym")),
        ("ii Pseudonym", ("ii", "Pseudonym")),
    ]
)
def test_parse_ordinal(field_name, result):
    assert parse_ordinal(field_name) == result
