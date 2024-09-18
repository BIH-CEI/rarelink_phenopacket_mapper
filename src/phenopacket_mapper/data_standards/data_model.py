"""
This module defines the `DataModel` class, which is used to define a data model for medical data. A `DataModel` is a
collection of `DataField` objects, which define the fields of the data model. Each `DataField` has a name, a value set,
a description, a section, a required flag, a specification, and an ordinal. The `DataModel` class also has a list of
`CodeSystem` objects, which are used as resources in the data model.

The `DataFieldValue` class is used to define the value of a `DataField` in a `DataModelInstance`. The
`DataModelInstance` class is used to define an instance of a `DataModel`, i.e. a record in a dataset.
"""

from dataclasses import dataclass
from pathlib import Path
from types import MappingProxyType
from typing import Union, List, Literal, Dict
import warnings

from phenopacket_mapper.data_standards import CodeSystem
from phenopacket_mapper.data_standards.date import Date
from phenopacket_mapper.data_standards.value_set import ValueSet


@dataclass(slots=True, frozen=True)
class DataField:
    """This class defines fields used in the definition of a `DataModel`

    A dataa field is the equivalent of a column in a table. It has a name, a value set, a description, a section, a
    required flag, a specification, and an ordinal.

    :ivar name: Name of the field
    :ivar value_set: Value set of the field
    :ivar description: Description of the field
    :ivar section: Section of the field (Only applicable if the data model is divided into sections)
    :ivar required: Required flag of the field
    :ivar specification: Text specification of the field (a description of the value set and field)
    :ivar ordinal: Ordinal of the field (E.g. 1.1, 1.2, 2.1, etc.)
    """
    name: str
    value_set: ValueSet
    description: str = ''
    section: str = ''
    required: bool = True
    specification: str = None
    ordinal: str = None

    def __str__(self):
        ret = "DataField(\n"
        ret += f"\t\tsection: {self.section},\n"
        ret += f"\t\tordinal, name: ({self.ordinal},  {self.name}),\n"
        ret += f"\t\tvalue_set: {self.value_set}, required: {self.required},\n"
        ret += f"\t\tspecification: {self.specification}\n"
        ret += "\t)"
        return ret


@dataclass(slots=True, frozen=True)
class DataFieldValue:
    """This class defines the value of a `DataField` in a `DataModelInstance`

    Equivalent to a cell value in a table.

    :ivar field: DataField: The `DataField` to which this value belongs and which defines the value set for the field.
    :ivar value: The value of the field.
    """
    field: DataField
    value: Union[int, float, str, bool, Date, CodeSystem]

    def validate(self) -> bool:
        """Validates the data model instance based on data model definition

        This method checks if the instance is valid based on the data model definition. It checks if all required fields
        are present, if the values are in the value set, etc.

        :return: True if the instance is valid, False otherwise
        """
        if self.field.required and self.value is None:
            warnings.warn(f"Field {self.field.name} is required but has no value")
            return False
        if self.value is not None and self.field.value_set:
            if self.value in self.field.value_set:
                return True
        warnings.warn(f"Value {self.value} is not in the value set of field {self.field.name}")
        return False


@dataclass(slots=True, frozen=True)
class DataModel:
    """This class defines a data model for medical data using `DataField`

    A data model can be used to import data and map it to the Phenopacket schema. It is made up of a list of `DataField`

    :ivar data_model_name: Name of the data model
    :ivar fields: List of `DataField` objects
    :ivar resources: List of `CodeSystem` objects
    """
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

    def load_data(
            self,
            path: Union[str, Path],
            compliance: Literal['soft', 'hard'] = 'soft'
    ) -> List['DataModelInstance']:
        """Loads data from a file using a DataModel definition

        :param path: Path to the file containing the data
        :param compliance: Compliance level to use when loading the data. If 'soft', the data will be loaded even if it
                           does not comply with the data model definition. If 'hard', the data will be loaded only if it
                           complies with the data model definition.
        :return: A list of `DataModelInstance` objects
        """
        from phenopacket_mapper.pipeline import load_data_using_data_model
        return load_data_using_data_model(path, self, compliance)

    @staticmethod
    def from_file(
            data_model_name: str,
            resources: List[CodeSystem],
            path: Union[str, Path],
            file_type: Literal['csv', 'excel', 'unknown'] = 'unknown',
            column_names: Dict[str, str] = MappingProxyType({
                DataField.name.__name__: 'data_field_name',
                DataField.section.__name__: 'data_model_section',
                DataField.description.__name__: 'description',
                DataField.value_set.__name__: 'value_set',
                DataField.required.__name__: 'required',
                DataField.specification.__name__: 'specification',
                DataField.ordinal.__name__: 'ordinal'
            }),
            parse_value_sets: bool = False,
            remove_line_breaks: bool = False,
            parse_ordinals: bool = True,
    ) -> 'DataModel':
        """Reads a Data Model from a file

        :param data_model_name: Name to be given to the `DataModel` object
        :param resources: List of `CodeSystem` objects to be used as resources in the `DataModel`
        :param path: Path to Data Model file
        :param file_type: Type of file to read, either 'csv' or 'excel'
        :param column_names: A dictionary mapping from each field of the `DataField` (key) class to a column of the file
                            (value). Leaving a value empty (`''`) will leave the field in the `DataModel` definition empty.
        :param parse_value_sets: If True, parses the string to a ValueSet object, can later be used to check
                            validity of the data. Optional, but highly recommended.
        :param remove_line_breaks: Whether to remove line breaks from string values
        :param parse_ordinals: Whether to extract the ordinal number from the field name. Warning: this can overwrite values
                                 Ordinals could look like: "1.1.", "1.", "I.a.", or "ii.", etc.
        """
        from phenopacket_mapper.pipeline import read_data_model
        return read_data_model(
            data_model_name,
            resources,
            path,
            file_type,
            column_names,
            parse_value_sets,
            remove_line_breaks,
            parse_ordinals
        )

    @staticmethod
    def load_data_using_data_model(
            path: Union[str, Path],
            data_model: 'DataModel',
            compliance: Literal['soft', 'hard'] = 'soft',
    ) -> List['DataModelInstance']:
        """Loads data from a file using a DataModel definition

        :param path: Path to  formatted csv or excel file
        :param data_model: DataModel to use for reading the file
        :param compliance: Compliance level to enforce when reading the file. If 'soft', the file can have extra fields
                            that are not in the DataModel. If 'hard', the file must have all fields in the DataModel.
        :return: List of DataModelInstances
        """
        return data_model.load_data(path, compliance)


@dataclass(slots=True)
class DataModelInstance:
    """This class defines an instance of a `DataModel`, i.e. a record in a dataset

    This class is used to define an instance of a `DataModel`, i.e. a record or row in a dataset.

    :ivar data_model: The `DataModel` object that defines the data model for this instance
    :ivar values: A list of `DataFieldValue` objects, each adhering to the `DataField` definition in the `DataModel`
    """
    data_model: DataModel
    values: List[DataFieldValue]

    def __post_init__(self):
        self.validate()

    def validate(self) -> bool:
        """Validates the data model instance based on data model definition

        This method checks if the instance is valid based on the data model definition. It checks if all required fields
        are present, if the values are in the value set, etc.

        :return: True if the instance is valid, False otherwise
        """
        for v in self.values:
            if not v.validate():
                return False
        return True
