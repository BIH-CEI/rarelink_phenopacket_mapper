import pytest

from phenopacket_mapper.data_standards import HPO, SNOMED_CT, Date
from phenopacket_mapper.data_standards.code_system import ICD9
from phenopacket_mapper.data_standards.value_set import ValueSet
from phenopacket_mapper.utils.parsing import parse_value_set


@pytest.fixture
def resources():
    return [
        HPO,
        SNOMED_CT,
        ICD9
    ]


@pytest.mark.parametrize("value_set_str, expected", [
    # TYPES
    # date
    ("date", ValueSet(elements=[Date])),
    ("Date", ValueSet(elements=[Date])),
    ("mm/dd/yyyy", ValueSet(elements=[Date])),
    ("dd.mm.yyyy", ValueSet(elements=[Date])),
    ("yyyy", ValueSet(elements=[Date])),
    # terminologies
    ("hp", ValueSet(elements=[HPO])),
    ("hpo, SCT", ValueSet(elements=[HPO, SNOMED_CT])),
    ("hp, SNOMED", ValueSet(elements=[HPO, SNOMED_CT])),
    ("icd9", ValueSet(elements=[ICD9])),
    # primitive types
    ("float", ValueSet(elements=[float])),
    ("float, int", ValueSet(elements=[float, int])),
    ("int, str, boolean", ValueSet(elements=[int, str, bool])),
    # mix of types
    ("hp, str, dd-mm-yyyy", ValueSet(elements=[HPO, str, Date])),
    ("integer, float, bool, sct, date", ValueSet(elements=[int, float, bool, SNOMED_CT, Date])),

    # VALUES
    # int values
    ("0, 1, 2, 3", ValueSet(elements=[0, 1, 2, 3])),
    ("-1, 0, 1", ValueSet(elements=[-1, 0, 1])),
    # float values
    ("0.0, 1.0, 2.0", ValueSet(elements=[0.0, 1.0, 2.0])),
    ("-1.0, 0.0, 1.0", ValueSet(elements=[-1.0, 0.0, 1.0])),
    # bool values
    ("True, False", ValueSet(elements=[True, False])),
    ("true, false", ValueSet(elements=[True, False])),
    ("TRUE, FALSE", ValueSet(elements=[True, False])),
    ("tRuE, FaLsE", ValueSet(elements=[True, False])),
    ("T, F", ValueSet(elements=[True, False])),
    ("t, f", ValueSet(elements=[True, False])),
    # str values
    ("yes, no, undecided", ValueSet(elements=["yes", "no", "undecided"])),
    ("positive, negative, unsure, not filled", ValueSet(elements=["positive", "negative", "unsure", "not filled"])),
    ("a, b, c, d, e", ValueSet(elements=["a", "b", "c", "d", "e"])),
    # date values
    ("01/01/2000, 01/01/2010, 01/01/2020", ValueSet(elements=[
        Date(day=1, month=1, year=2000),
        Date(day=1, month=1, year=2010),
        Date(day=1, month=1, year=2020),
    ])),
    ("01.01.2000, 07.12.2020, 12.9.2024", ValueSet(elements=[
        Date(day=1, month=1, year=2000),
        Date(day=7, month=12, year=2020),
        Date(day=12, month=9, year=2024),
    ])),
    ("2000, 2020, 2021", ValueSet(elements=[Date(year=2000), Date(year=2020), Date(year=2021)])),

    # MIX OF EVERYTHING
    (
            "hp, 0, 1, 2, 3, float, true, false, yes, no, 01/01/2000",
            ValueSet(elements=[HPO, 0, 1, 2, 3, float, True, False, "yes", "no", Date(day=1, month=1, year=2000)])
    ),
    # Erdri examples
    (
            "alive, dead, lost in follow-up, opted-out",
            ValueSet(elements=["alive", "dead", "lost in follow-up", "opted-out"])
    ),
    (
            "antenatal, at birth, dd/mm/yyyy, undetermined",
            ValueSet(elements=["antenatal", "at birth", Date, "undetermined"])
    ),
])
def test_parse_value_set_(value_set_str, expected, resources):
    assert parse_value_set(value_set_str, resources=resources) == expected
