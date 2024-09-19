from dataclasses import dataclass, replace, field
from typing import List


@dataclass(slots=True, frozen=True)
class CodeSystem:
    """Data class for a CodeSystem

    A `CodeSystem` is a resource that defines a set of codes and their meanings. It could be a terminology, an ontology,
    a nomenclature, etc. Popular examples include SNOMED CT, HPO, MONDO, OMIM, ORDO, LOINC, etc.

    This class is necessary to fill the resources parameter in the Phenopacket later.

    :ivar name: The name of the CodeSystem
    :ivar namespace_prefix: The namespace prefix of the CodeSystem
    :ivar url: The URL of the CodeSystem
    :ivar iri_prefix: The IRI prefix of the CodeSystem
    :ivar version: The version of the CodeSystem
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

    def __eq__(self, other):
        """Check if two CodeSystems are equal based on their name, namespace prefix, and version.

        Right now this method ignores the version, this may be subject to change in the future."""
        if not isinstance(other, CodeSystem):
            return False
        return self.namespace_prefix == other.namespace_prefix or self.namespace_prefix in other.synonyms

    def __str__(self):
        return f"CodeSystem(name={self.name}, name space prefix={self.namespace_prefix}, version={self.version})"

    def __repr__(self):
        return str(self)

    def __contains__(self, item):
        from phenopacket_mapper.data_standards import Coding
        if isinstance(item, Coding):
            return self == item.system


SNOMED_CT = CodeSystem(
    name="SNOMED CT",
    namespace_prefix="SNOMED",
    url="http://snomed.info/sct",
    synonyms=["SCT"]
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
    url="https://www.who.int/classifications/icd/en/",
    synonyms=["icd-9"]
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
