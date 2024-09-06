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
    data_type: List[Union[type, CodeSystem, str]]
    required: bool = True
    specification: str = None
    ordinal: str = None

    def __str__(self):
        ret = "DataField(\n"
        ret += f"\t\tordinal, section={self.ordinal} {self.section},\n"
        ret += f"\t\tname={self.name},\n"
        ret += f"\t\tdata type={self.data_type}, required={self.required},\n"
        ret += f"\t\tsepcification={self.specification}\n"
        ret += "\t)"
        return ret


@dataclass(slots=True, frozen=True)
class DataFieldValue:
    """This class defines the value of a `DataField` in a `DataModelInstance`"""
    field: DataField
    value: Union[int, float, str, bool, Date, CodeSystem]


@dataclass(slots=True, frozen=True)
class DataModel:
    """This class defines a data model for medical data using `DataField`"""
    data_model_name: str
    fields: List[DataField]
    resources: List[CodeSystem]

    def __str__(self):
        ret = f"DataModel(name={self.data_model_name}\n"
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
