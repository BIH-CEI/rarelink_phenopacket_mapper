from dataclasses import dataclass, replace, field
from typing import List


@dataclass(slots=True, frozen=True)
class CodeSystem:
    """
    Data class for a CodeSystem
    """
    name: str
    namespace_prefix: str
    url: str = None
    iri_prefix: str = None
    version: str = "0.0.0"
    """List typical alternative abbreviations or names for the resource, to better parse its usage (e.g. 'HPO' for the
    Human Phenotype Ontology, even if its name space prefix is commonly 'HP')"""
    synonyms: List[str] = field(default_factory=lambda: [])

    def set_version(self, value) -> 'CodeSystem':
        return replace(self, version=value)


SNOMED_CT = CodeSystem(
    name="SNOMED CT",
    namespace_prefix="SCT",
    url="http://snomed.info/sct",
    synonyms=["SNOMED"]
)
HPO = CodeSystem(
    name="Human Phenotype Ontology",
    namespace_prefix="HP",
    url="http://www.human-phenotype-ontology.org",
    iri_prefix="http://purl.obolibrary.org/obo/HP_",
    synonyms=["HPO"]
)
MONDO = CodeSystem(
    name="Monarch Disease Ontology",
    namespace_prefix="MONDO",
    url="http://purl.obolibrary.org/obo/mondo.owl"
)
OMIM = CodeSystem(
    name="Online Mendelian Inheritance",
    namespace_prefix="OMIM",
    url="https://omim.org/"
)
ORDO = CodeSystem(
    name="Orphanet",
    namespace_prefix="ORPHA",
    url="http://www.orpha.net/"
)
LOINC = CodeSystem(
    name="Logical Observation Identifiers Names and Codes",
    namespace_prefix="LOINC",
    url="https://loinc.org/"
)

HGVS = CodeSystem(
    name="Human Genome Variation Society",
    namespace_prefix="HGVS",
    url="http://varnomen.hgvs.org/"
)

ICD9 = CodeSystem(
    name="International Classification of Diseases",
    namespace_prefix="ICD9",
    url="https://www.who.int/classifications/icd/en/"
)

ICD10_CM = CodeSystem(
    name="International Classification of Diseases",
    namespace_prefix="ICD10-CM",
    url="https://www.who.int/classifications/icd/en/"
)

ICD10_GM = CodeSystem(
    name="International Classification of Diseases",
    namespace_prefix="ICD10-GM",
    url="https://www.who.int/classifications/icd/en/"
)

HGNC = CodeSystem(
    name="HUGO Gene Nomenclature Committee",
    namespace_prefix="HGNC",
    url="https://www.genenames.org/"
)
