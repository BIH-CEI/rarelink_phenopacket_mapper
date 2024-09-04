from dataclasses import dataclass


@dataclass(slots=True)
class CodeSystem:
    """
    Data class for CodeSystem
    """
    name: str
    namespace_prefix: str
    url: str = None
    iri_prefix: str = None
    _version: str = "0.0.0"

    @property
    def version(self) -> str:
        return self._version

    @version.setter
    def version(self, value: str):
        self._version = value


SNOMED_CT = CodeSystem(
    name="SNOMED CT",
    namespace_prefix="SCT",
    url="http://snomed.info/sct"
)
HPO = CodeSystem(
    name="Human Phenotype Ontology",
    namespace_prefix="HP",
    url="http://www.human-phenotype-ontology.org",
    iri_prefix="http://purl.obolibrary.org/obo/HP_"
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
ORPHA = CodeSystem(
    name="Orphanet",
    namespace_prefix="ORPHA",
    url="http://www.orpha.net/"
)
LOINC = CodeSystem(
    name="Logical Observation Identifiers Names and Codes",
    namespace_prefix="LOINC",
    url="https://loinc.org/"
)
