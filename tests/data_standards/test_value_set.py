import pytest

from phenopacket_mapper.data_standards import Coding, code_system, Date
from phenopacket_mapper.data_standards.value_set import ValueSet


@pytest.mark.parametrize("value, is_in, value_set", [
    ('a', False, ValueSet(elements=[])),
    ('a', False, ValueSet(elements=['A', 'b', 'c'])),
    (Date, False, ValueSet(elements=['date', 'Date'])),
    ('a', True, ValueSet(elements=['a', 'b', 'c'])),
    ('test test 123', True, ValueSet(elements=['test test 123', 'b', 'c'])),
    (3, True, ValueSet(elements=[3, 19, 7])),
    (
            Coding(system=code_system.SNOMED_CT, code='404684003'),
            True,
            ValueSet(elements=[Coding(system=code_system.SNOMED_CT, code='404684003'), 1, 'a'])
    ),
    (
            code_system.HPO,
            True,
            ValueSet(elements=[
                code_system.HPO, Coding(system=code_system.HPO, code="1"),
                Coding(system=code_system.SNOMED_CT, code='404684003')
            ])
    ),
    (False, False, ValueSet(elements=[0, 1])),
    (True, False, ValueSet(elements=[0, 1])),
    (True, True, ValueSet(elements=[True, False])),
    (False, True, ValueSet(elements=[True, False])),
    (0.117, True, ValueSet(elements=[0.117, 1.0])),
    (str, True, ValueSet(elements=[str, int])),
    (Date, True, ValueSet(elements=[Date, int])),
    (Date(year=2024, month=9, day=18), True, ValueSet(elements=[Date(year=2024, month=9, day=18), 'date'])),
])
def test_in_valueset(value, is_in, value_set):
    if is_in:
        assert value in value_set
    else:
        assert value not in value_set
