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


rarelink_data_model = DataModel(
    name="RareLink",
    fields=[
        # Section 1: Formal Criteria
        # 1.1 Pseudonym
        DataField(
            name="Pseudonym",
            section="1. Formal Criteria",
            description="The (local) patient-related Identification code",
            data_type=str,
        ),
        # 1.2 Date of admission
        DataField(
            name="Date of admission",
            section="1. Formal Criteria",
            description="The date of the patient’s admission to the hospital",
            data_type=Date,
            specification="ISO 8601 date string, YYYY-MM-DD",
        ),
    ]
)
