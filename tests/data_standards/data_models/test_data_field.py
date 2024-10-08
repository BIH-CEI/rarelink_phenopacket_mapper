import pytest

from phenopacket_mapper.data_standards import DataField


def test_data_field_constructor():
    assert DataField(name="name", )