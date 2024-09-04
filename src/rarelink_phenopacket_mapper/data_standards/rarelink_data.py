from dataclasses import dataclass
from typing import Union, Literal, List

from rarelink_phenopacket_mapper.data_standards import CodeSystem
from rarelink_phenopacket_mapper.data_standards.date import Date


@dataclass(slots=True)
class RarelinkData:
    """
    Data class for Rarelink data
    """


@dataclass(slots=True)
class DataField:
    name: str
    section: str
    description: str
    data_type: Union[type, CodeSystem]
    required: bool = True
    specification: str = None
    ordinal: str = None


@dataclass(slots=True)
class DataModel:
    name: str
    fields: List[DataField]


RARELINK_DATAMODEL = DataModel(
    name="RareLink",
    fields=[
        # Section 1: Formal Criteria
        # 1.1 Pseudonym
        DataField(
            ordinal="1.1",
            name="Pseudonym",
            section="Formal Criteria",
            description="The (local) patient-related Identification code",
            data_type=str,
        ),
        # 1.2 Date of admission
        DataField(
            ordinal="1.2",
            name="Date of admission",
            section="Formal Criteria",
            description="The date of the patient’s admission to the hospital",
            data_type=Date,
            specification="ISO 8601 date string, YYYY-MM-DD",
        ),
        # 2. Personal Information
        # 2.1 Date of birth
        # 2.2 Sex at birth
        # 2.3 Karyotypic Sex
        # 2.4 Gender Identity
        # 3. Patient Status
        # 3.1 Vital Status
        # 3.2 Date of Death
        # 3.3 Cause of Death
        # 3.4 Age Category
        # 3.6 Undiagnosed Rare Disease Case
        # 5. Disease
        # 5.1 Disease
        # 5.2 Verification Status
        # 5.3 Age at Onset
        # 5.4 Date of Onset
        # 5.6 Date of Diagnosis
        # 5.7 Body Site
        # 5.8 Clinical Status
        # 6. Genotype and Phenotype
        # 6.1 Genetic Findings
        # 6.1.1 Genomic Diagnosis
        # 6.1.2 Progress Status of Interpretation
        # 6.1.3 Interpretation Status
        # 6.1.5 Reference Genome
        # 6.1.6 Genomic Mutation String
        # 6.1.7 Genomic DNA Change
        # 6.1.8 Sequence DNA Change
        # 6.1.9 Amiono Acid Change
        # 6.1.10 Gene
        # 6.1.11 Zygositiy
        # 6.1.14 Clinical Significance [ACMG]
        # 6.1.15 Therapeutic Actionability
        # 6.2 Phenotypic Feature
        # 6.2.1 Phenotypic Feature
        # 6.2.2 Determination Date
        # 6.2.3 Status
        # 6.2.4 Modifier
        # 6.3 Family History
        # 6.3.1 Propositus/-a
        # 6.3.2 Relationship of the individual to the index case / propositus/a
        # 6.3.3 Consanguinity
        # 6.3.4 Family Member Relationship
        # 6.3.5 Family Member Record Status
        # 6.3.6 Family Member Sex
        # 6.3.7 Family Member Age
        # 6.3.8 Family Member Date of Birth
        # 6.3.9 Family Member Deceased
        # 6.3.10 Family Member Cause of Death
        # 6.3.11 Family Member Decesased Age
        # 6.3.12 Family Member Disease
    ]
)
