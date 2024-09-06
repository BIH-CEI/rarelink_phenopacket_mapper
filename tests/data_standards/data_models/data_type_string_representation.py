from typing import List, Any

import pytest

from rarelink_phenopacket_mapper.data_standards import Date
from rarelink_phenopacket_mapper.data_standards.code_system import HPO, SNOMED_CT, ICD9
from rarelink_phenopacket_mapper.data_standards.data_models import parse_string_type_representation
from rarelink_phenopacket_mapper.data_standards.data_models.data_type_string_representation import \
    _parse_single_string_type_repr


@pytest.fixture
def resources():
    return [
        HPO,
        SNOMED_CT,
        ICD9
    ]


@pytest.mark.parametrize(
    "type_str, result", [
        ("str", [str]),  # single primitive
        ("integer", [int]),  # single primitive
        ("integer, bool", [int, bool]),  # 2 primitive, white space
        ("integer,bool", [int, bool]),  # 2 primitive, no white space
        (" integer ,   bool ", [int, bool]),  # 2 primitive, multiple white spaces
        ("integer,bool, string", [int, bool, str]),  # multiple primitives space and no soace
        ("integer, bool, string", [int, bool, str]),  # multiple primitives
        ("Int, bOoL, StRInG", [int, bool, str]),  # multiple primitives spongebob case
        ("INT, BOOLEAN, STR", [int, bool, str]),  # multiple primitives upper case
        ("", [Any]),  # empty string
        (" ", [Any]),  # empty string
        ("               ", [Any]),  # empty string
        (None, [Any]),  # empty string
        ("icd9", [ICD9]),  # single resource
        ("icd9, hpo", [ICD9, HPO]),  # multiple resources
        ("hpo, sct, str", [HPO, SNOMED_CT, str]),  # mix resources and primitives
        ("hPo, SNOmed, strinG", [HPO, SNOMED_CT, str]),  # mix resources and primitives, strange upper and lower
        ("date", [Date]),
        ("date, snomed, hpo", [Date, SNOMED_CT, HPO]),
        ("integer, boolean, string, date, HP", [int, bool, str, Date, HPO]),
    ]
)
def test_parse_string_type_representation(type_str, result, resources):
    assert parse_string_type_representation(type_str, resources) == result


@pytest.mark.parametrize(
    "type_str, result", [
        ("str", str),  # single primitive
        ("integer", int),  # single primitive
        ("integer ", int),  # white space
        (" integer   ", int),  # multiple white spaces
        ("Int", int),  # spongebob case
        ("bOoL", bool),  # spongebob case
        ("StRInG", str),  # spongebob case
        ("INT", int),  # primitive upper case
        ("BOOLEAN", bool),  # primitive upper case
        ("STR", str),  # primitive upper case
        # no need to check for empty strings because this is a helper and the bigger method checks and is tested
        ("icd9", ICD9),  # single resource
        ("hpo", HPO),  # single resources
        ("date", Date),  # date
    ]
)
def test__parse_single_string_type_repr(type_str, result, resources):
    assert _parse_single_string_type_repr(type_str, resources) == result
