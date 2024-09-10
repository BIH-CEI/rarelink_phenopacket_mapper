import pytest

from phenopacket_mapper.utils.parsing import parse_coding
from phenopacket_mapper.data_standards import code_system, Coding


@pytest.fixture()
def resources():
    return [
        code_system.SNOMED_CT,
        code_system.ORDO,
        code_system.ICD10_GM,
        code_system.HGVS,
        code_system.OMIM,
        code_system.HPO,
        code_system.HGNC
    ]


@pytest.mark.parametrize("coding_str, expected", [
    ("SNOMED:404684003", Coding(code="404684003", system=code_system.SNOMED_CT)),
    ("SCT:1148601009", Coding(code="1148601009", system=code_system.SNOMED_CT)),
    ("ORPHA:330001", Coding(code="330001", system=code_system.ORDO)),
    ("ICD10-GM:G82.21", Coding(code="G82.21", system=code_system.ICD10_GM)),
    ("HP:0000790", Coding(code="0000790", system=code_system.HPO)),
    ("HPO:0000790", Coding(code="0000790", system=code_system.HPO)),
    ("OMIM:113900", Coding(code="113900", system=code_system.OMIM)),
    ("HGVS:NC_000023.11:g.32325690G>A", Coding(code="NC_000023.11:g.32325690G>A", system=code_system.HGVS)),
    ("HGVS:NM_000492.3:c.1521_1523delCTT", Coding(code="NM_000492.3:c.1521_1523delCTT", system=code_system.HGVS)),
    ("HGVS:NP_000483.3:p.Phe508del", Coding(code="NP_000483.3:p.Phe508del", system=code_system.HGVS)),
    ("HGVS:NM_000546.5:c.169_170delAG", Coding(code="NM_000546.5:c.169_170delAG", system=code_system.HGVS)),
    ("HGVS:NP_000537.3:p.Arg57fs", Coding(code="NP_000537.3:p.Arg57fs", system=code_system.HGVS)),
    ("HGVS:NM_001354689.2:c.925_926insG", Coding(code="NM_001354689.2:c.925_926insG", system=code_system.HGVS)),
    ("HGVS:NM_004006.2:c.516_518dupAAG", Coding(code="NM_004006.2:c.516_518dupAAG", system=code_system.HGVS)),
    ("HGVS:NM_001126112.2:c.1000_1200inv", Coding(code="NM_001126112.2:c.1000_1200inv", system=code_system.HGVS)),
    ("HGVS:NC_000023.11:g.32315474_32316876del", Coding(code="NC_000023.11:g.32315474_32316876del",
                                                        system=code_system.HGVS)),
    ("HGVS:NM_004006.2:c.672_673delA", Coding(code="NM_004006.2:c.672_673delA", system=code_system.HGVS)),
    ("HGVS:NP_004997.1:p.Gly225fs", Coding(code="NP_004997.1:p.Gly225fs", system=code_system.HGVS)),
    ("HGVS:NM_000314.4:c.1691G>A", Coding(code="NM_000314.4:c.1691G>A", system=code_system.HGVS)),
    ("HGVS:NP_000305.3:p.Arg564His", Coding(code="NP_000305.3:p.Arg564His", system=code_system.HGVS)),
    ("HGNC:310", Coding(code="310", system=code_system.HGNC)),
])
def test_parse_coding(resources, coding_str, expected):
    assert parse_coding(coding_str, resources) == expected
