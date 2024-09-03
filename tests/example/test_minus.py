import pytest
import rarelink_phenopacket_mapper


@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 0),
    (1, 2, -1),
    (2, 1, 1),
    (2, 2, 0),
    (0, 0, 0),
    (-1, -1, 0),
    (10, -1, 11),
])
def test_minus(a, b, expected):
    assert rarelink_phenopacket_mapper.example.minus.minus(a, b) == expected
