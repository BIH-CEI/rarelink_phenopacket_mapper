from dataclasses import dataclass
from typing import Union, Literal, List

from rarelink_phenopacket_mapper.data_standards import CodeSystem


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
