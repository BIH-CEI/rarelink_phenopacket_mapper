from dataclasses import dataclass
from typing import Union, List

from rarelink_phenopacket_mapper.data_standards import CodeSystem
from rarelink_phenopacket_mapper.data_standards.date import Date


@dataclass(slots=True, frozen=True)
class DataField:
    name: str
    section: str
    description: str
    data_type: Union[type, CodeSystem]
    required: bool = True
    specification: str = None
    ordinal: str = None


@dataclass(slots=True, frozen=True)
class DataFieldValue:
    field: DataField
    value: Union[int, float, str, bool, Date, CodeSystem]


@dataclass(slots=True, frozen=True)
class DataModel:
    name: str
    fields: List[DataField]


@dataclass(slots=True)
class DataModelInstance:
    data_model: DataModel
    values: List[DataFieldValue]
