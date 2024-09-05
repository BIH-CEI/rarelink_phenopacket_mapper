from dataclasses import dataclass
from typing import Union, List

from rarelink_phenopacket_mapper.data_standards import CodeSystem
from rarelink_phenopacket_mapper.data_standards.date import Date


@dataclass(slots=True, frozen=True)
class DataField:
    """This class defines fields used in the definition of a `DataModel`"""
    name: str
    section: str
    description: str
    data_type: Union[type, CodeSystem]
    required: bool = True
    specification: str = None
    ordinal: str = None


@dataclass(slots=True, frozen=True)
class DataFieldValue:
    """This class defines the value of a `DataField` in a `DataModelInstance`"""
    field: DataField
    value: Union[int, float, str, bool, Date, CodeSystem]


@dataclass(slots=True, frozen=True)
class DataModel:
    """This class defines a data model for medical data using `DataField`"""
    name: str
    fields: List[DataField]
    resources: List[CodeSystem]

    def __str__(self):
        ret = f"DataModel(name={self.name}\n"
        for field in self.fields:
            ret += f"\t{str(field)}\n"
        ret += "---\n"
        for res in self.resources:
            ret += f"\t{str(res)}\n"
        ret += ")"
        return ret


@dataclass(slots=True)
class DataModelInstance:
    """This class defines an instance of a `DataModel`, i.e. a record in a dataset"""
    data_model: DataModel
    values: List[DataFieldValue]
