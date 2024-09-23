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


NCBITaxon = CodeSystem(
    name='NCBI organismal classification', 
    namespace_prefix='NCBITaxon', 
    url='https://www.ncbi.nlm.nih.gov/taxonomy',
    version="2024-07-03"
)

GENO = CodeSystem(
    name='GENO: The Genotype Ontology', 
    namespace_prefix='GENO', 
    url='http://www.genoontology.org/',
    version="2023-10-08"
)

SO = CodeSystem(
    name='Sequence types and features ontology', 
    namespace_prefix='SO', 
    url='http://www.sequenceontology.org/',
    version="2.6"
)

ICD10CM = CodeSystem(
    name='International Classification of Diseases, Tenth Revision, Clinical Modification', 
    namespace_prefix='ICD10CM', 
    url='https://www.cdc.gov/nchs/icd/icd10cm.htm',
    version="2024-09-01"
)

SNOMED = CodeSystem(
    name='SNOMED CT', 
    namespace_prefix='SNOMED', 
    url='https://www.snomed.org/snomed-ct',
    version="2024-09-01"
)

ICD11 = CodeSystem(
    name='International Classification of Diseases, Eleventh Revision', 
    namespace_prefix='icd11', 
    url='https://icd.who.int/en',
    version="2024-09-01"
)

HL7FHIR = CodeSystem(
    name='Health Level 7 Fast Healthcare Interoperability Resources', 
    namespace_prefix='HL7FHIR', 
    url='https://www.hl7.org/fhir/',
    version="v4.0.1"
)

GA4GH = CodeSystem(
    name='Global Alliance for Genomics and Health', 
    namespace_prefix='ga4gh', 
    url='https://www.ga4gh.org/',
    version="v2.0"
)

ISO3166 = CodeSystem(
    name='ISO 3166-1:2020(en) alpha-2 and alpha-3 country codes', 
    namespace_prefix='iso3166', 
    url='https://www.iso.org/iso-3166-country-codes.html',
    version="2020(en)"
)

ICF = CodeSystem(
    name='International Classification of Functioning, Disability and Health (ICF)', 
    namespace_prefix='icf', 
    url='https://www.who.int/classifications/icf/en/',
    version="1.0.2"
)
MONDO = CodeSystem(
    name="Monarch Disease Ontology",
    namespace_prefix="MONDO",
    url="http://purl.obolibrary.org/obo/mondo.owl",
    version="2024-09-03"
)
ORDO = CodeSystem(
    name="Orphanet Rare Disease Ontology",
    namespace_prefix="ORPHA",
    url="http://www.orpha.net/",
    version="2024-09-12"
)
OMIM = CodeSystem(
    name="Online Mendelian Inheritance",
    namespace_prefix="OMIM",
    url="https://omim.org/", 
    version="2024-09-12"
)
LOINC = CodeSystem(
    name="Logical Observation Identifiers Names and Codes",
    namespace_prefix="LOINC",
    url="https://loinc.org/",
    version="2.78"
)
HGVS = CodeSystem(
    name="Human Genome Variation Society",
    namespace_prefix="HGVS",
    url="http://varnomen.hgvs.org/", 
    version="21.0.0"
)
HGNC = CodeSystem(
    name="HUGO Gene Nomenclature Committee",
    namespace_prefix="HGNC",
    url="https://www.genenames.org/",
    version="2024-08-23"
)
HPO = CodeSystem(
    name="Human Phenotype Ontology",
    namespace_prefix="HP",
    url="http://www.human-phenotype-ontology.org",
    iri_prefix="http://purl.obolibrary.org/obo/HP_",
    synonyms=["HPO"],
    version="2024-08-13"
)
UO = CodeSystem(
    name="Units of Measurement Ontology",
    namespace_prefix="UO",
    url="http://www.ontobee.org/ontology/UO",
    version="2023-05-25"
)
NCIT = CodeSystem(
    name = "NCI Thesaurus OBO Edition",
    namespace_prefix = "NCIT",
    url = "https://ncit.nci.nih.gov/",
    version="24.04e"
)



