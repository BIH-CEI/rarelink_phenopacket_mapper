"""
This module defines the `DataModel` class, which is used to define a data model for medical data. A `DataModel` is a
collection of `DataField` objects, which define the fields of the data model. Each `DataField` has a name, a value set,
a description, a section, a required flag, a specification, and an ordinal. The `DataModel` class also has a list of
`CodeSystem` objects, which are used as resources in the data model.

The `DataFieldValue` class is used to define the value of a `DataField` in a `DataModelInstance`. The
`DataModelInstance` class is used to define an instance of a `DataModel`, i.e. a record in a dataset.
"""

from dataclasses import dataclass, field
from pathlib import Path
from types import MappingProxyType
from typing import Union, List, Literal, Dict, Optional, Any, Callable, Tuple
import warnings

import pandas as pd

from phenopacket_mapper.data_standards import CodeSystem
from phenopacket_mapper.data_standards.date import Date
from phenopacket_mapper.data_standards.value_set import ValueSet
from phenopacket_mapper.preprocessing import preprocess, preprocess_method


@dataclass(slots=True, frozen=True)
class DataField:
    """This class defines fields used in the definition of a `DataModel`

    A dataa field is the equivalent of a column in a table. It has a name, a value set, a description, a section, a
    required flag, a specification, and an ordinal.

    The string for the `id` field is generated from the `name` field using the `str_to_valid_id` function from the
    `phenopacket_mapper.utils` module. This attempts to convert the `name` field. Sometimes this might not work as
    desired, in which case the `id` field can be set manually.

    Naming rules for the `id` field:
    - The `id` field must be a valid Python identifier
    - The `id` field must start with a letter or the underscore character
    - The `id` field must cannot start with a number
    - The `id` field can only contain lowercase alpha-numeric characters and underscores (a-z, 0-9, and _ )
    - The `id` field cannot be any of the Python keywords (e.g. `in`, `is`, `not`, `class`, etc.).
    - The `id` field must be unique within a `DataModel`

    If the `value_set` is a single type, it can be passed directly as the `value_set` parameter.

    e.g.:
    >>> DataField(name="Field 1", specification=int)
    DataField(name='Field 1', specification=ValueSet(elements=[<class 'int'>], name='', description=''), id='field_1', description='', section='', required=True, ordinal='')

    :ivar name: Name of the field
    :ivar specification: Value set of the field, if the value set is only one type, can also pass that type directly
    :ivar id: The identifier of the field, adhering to the naming rules stated above
    :ivar description: Description of the field
    :ivar section: Section of the field (Only applicable if the data model is divided into sections)
    :ivar required: Required flag of the field
    :ivar ordinal: Ordinal of the field (E.g. 1.1, 1.2, 2.1, etc.)
    """
    name: str = field()
    specification: Union[ValueSet, type, List[type]] = field()
    id: str = field(default=None)
    description: str = field(default='')
    section: str = field(default='')
    required: bool = field(default=True)
    ordinal: str = field(default='')

    def __post_init__(self):
        if not self.id:
            from phenopacket_mapper.utils import str_to_valid_id
            object.__setattr__(self, 'id', str_to_valid_id(self.name))

        if isinstance(self.specification, type):
            object.__setattr__(self, 'specification', ValueSet(elements=[self.specification]))
        if isinstance(self.specification, list):
            if all(isinstance(e, type) for e in self.specification):
                object.__setattr__(self, 'specification', ValueSet(elements=self.specification))

    def __str__(self):
        ret = "DataField(\n"
        ret += f"\t\tid: {self.id},\n"
        ret += f"\t\tsection: {self.section},\n"
        ret += f"\t\tordinal, name: ({self.ordinal},  {self.name}),\n"
        ret += f"\t\tvalue_set: {self.specification}, required: {self.required},\n"
        ret += f"\t\tspecification: {self.specification}\n"
        ret += "\t)"
        return ret


    def __eq__(self, other):
        if not isinstance(other, DataField):
            return False
        return (self.id == other.id and self.specification == other.specification
                and self.required == other.required)


@dataclass(slots=True)
class DataFieldValue:
    """This class defines the value of a `DataField` in a `DataModelInstance`

    Equivalent to a cell value in a table.

    :ivar row_no: The id of the value, i.e. the row number
    :ivar field: DataField: The `DataField` to which this value belongs and which defines the value set for the field.
    :ivar value: The value of the field.
    """
    row_no: Union[str, int]
    field: DataField
    value: Union[int, float, str, bool, Date, CodeSystem]

    def validate(self) -> bool:
        """Validates the data model instance based on data model definition

        This method checks if the instance is valid based on the data model definition. It checks if all required fields
        are present, if the values are in the value set, etc.

        :return: True if the instance is valid, False otherwise
        """
        if self.field.required and self.value is None:  # no value
            warnings.warn(f"Field {self.field.name} is required but has no value")
            return False
        elif self.value is not None and self.field.specification:
            if Any in self.field.specification:  # value set allows any
                return True
            elif self.value in self.field.specification:  # raw value (likely a primitive) is in the value set
                return True
            else:  # check if the value matches one of the types in the value set
                for e in self.field.specification:
                    if isinstance(e, type):
                        cur_type = e
                        if cur_type is type(self.value):
                            return True
                    elif isinstance(e, CodeSystem):
                        cs = e
                        from phenopacket_mapper.data_standards import Coding
                        if isinstance(self.value, Coding) and self.value.system == cs:
                            return True

        warnings.warn(f"Value {self.value} of type {type(self.value)} is not in the value set of field "
                      f"{self.field.name} (row {self.row_no})")
        return False


@dataclass(slots=True, frozen=True)
class DataModel:
    """This class defines a data model for medical data using `DataField`

    A data model can be used to import data and map it to the Phenopacket schema. It is made up of a list of `DataField`

    Given that all `DataField` objects in a `DataModel` have unique names, the `id` field is generated from the `name`.
    E.g.: `DataField(name='Date of Birth', ...)` will have an `id` of `'date_of_birth'`. The `DataField` objects can
    be accessed using the `id` as an attribute of the `DataModel` object. E.g.: `data_model.date_of_birth`. This is
    useful in the data reading and mapping processes.

    >>> data_model = DataModel("Test data model", (DataField(name="Field 1", specification=ValueSet()),))
    >>> data_model.field_1
    DataField(name='Field 1', specification=ValueSet(elements=[], name='', description=''), id='field_1', description='', section='', required=True, ordinal='')

    :ivar data_model_name: Name of the data model
    :ivar fields: List of `DataField` objects
    :ivar resources: List of `CodeSystem` objects
    """
    data_model_name: str = field()
    fields: Tuple[DataField, ...] = field()
    resources: List[CodeSystem] = field(default_factory=list)

    def __post_init__(self):
        if len(self.fields) != len(set([f.id for f in self.fields])):
            raise ValueError("All fields in a DataModel must have unique identifiers")

    def __getattr__(self, var_name: str) -> DataField:
        for f in self.fields:
            if f.id == var_name:
                return f
        raise AttributeError(f"'DataModel' object has no attribute '{var_name}'")

    def __str__(self):
        ret = f"DataModel(name={self.data_model_name}\n"
        for _field in self.fields:
            ret += f"\t{str(_field)}\n"
        ret += "---\n"
        for res in self.resources:
            ret += f"\t{str(res)}\n"
        ret += ")"
        return ret

    def __iter__(self):
        return iter(self.fields)

    def get_field(self, field_id: str, default: Optional = None) -> Optional[DataField]:
        """Returns a DataField object by its id

        :param field_id: The id of the field
        :param default: The default value to return if the field is not found
        :return: The DataField object
        """
        for f in self.fields:
            if f.id == field_id:
                return f
        if default or default is None:
            return default
        raise ValueError(f"Field with id {field_id} not found in DataModel")

    def get_field_ids(self) -> List[str]:
        """Returns a list of the ids of the DataFields in the DataModel"""
        return [f.id for f in self.fields]

    def load_data(
            self,
            path: Union[str, Path],
            compliance: Literal['lenient', 'strict'] = 'lenient',
            **kwargs
    ) -> 'DataSet':
        """Loads data from a file using a DataModel definition

        To call this method, pass the column name for each field in the DataModel as a keyword argument. This is done
        by passing the field id followed by '_column'. E.g. if the DataModel has a field with id 'date_of_birth', the
        column name in the file should be passed as 'date_of_birth_column'. The method will raise an error if any of
        the fields are missing.

        E.g.:
        ```python
        data_model = DataModel("Test data model", [DataField(name="Field 1", value_set=ValueSet())])
        data_model.load_data("data.csv", field_1_column="column_name_in_file")
        ```

        :param path: Path to the file containing the data
        :param compliance: Compliance level to use when loading the data.
        :param kwargs: Dynamically passed parameters that match {id}_column for each item
        :return: A list of `DataModelInstance` objects
        """
        column_names = dict()
        for f in self.fields:
            column_param = f"{f.id}_column"
            if column_param not in kwargs:
                raise TypeError(f"load_data() missing 1 required argument: '{column_param}'")
            else:
                column_names[f.id] = kwargs[column_param]

        from phenopacket_mapper.pipeline import load_data_using_data_model
        return load_data_using_data_model(
            path=path,
            data_model=self,
            column_names=column_names,
            compliance=compliance
        )

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
                DataField.specification.__name__: 'value_set',
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
            column_names: Dict[str, str],
            compliance: Literal['lenient', 'strict'] = 'lenient',
    ) -> 'DataSet':
        """Loads data from a file using a DataModel definition

        :param path: Path to  formatted csv or excel file
        :param data_model: DataModel to use for reading the file
        :param column_names: A dictionary mapping from the id of each field of the `DataField` to the name of a
                            column in the file
        :param compliance: Compliance level to enforce when reading the file. If 'lenient', the file can have extra fields
                            that are not in the DataModel. If 'strict', the file must have all fields in the DataModel.
        :return: List of DataModelInstances
        """
        from phenopacket_mapper.pipeline import load_data_using_data_model
        return load_data_using_data_model(
            path=path,
            data_model=data_model,
            column_names=column_names,
            compliance=compliance
        )


@dataclass(slots=True)
class DataModelInstance:
    """This class defines an instance of a `DataModel`, i.e. a record in a dataset

    This class is used to define an instance of a `DataModel`, i.e. a record or row in a dataset.

    :ivar row_no: The id of the instance, i.e. the row number
    :ivar data_model: The `DataModel` object that defines the data model for this instance
    :ivar values: A list of `DataFieldValue` objects, each adhering to the `DataField` definition in the `DataModel`
    :ivar compliance: Compliance level to enforce when validating the instance. If 'lenient', the instance can have extra
                        fields that are not in the DataModel. If 'strict', the instance must have all fields in the
                        DataModel.
    """
    row_no: Union[int, str]
    data_model: DataModel
    values: List[DataFieldValue]
    compliance: Literal['lenient', 'strict'] = 'lenient'

    def __post_init__(self):
        self.validate()

    def validate(self) -> bool:
        """Validates the data model instance based on data model definition

        This method checks if the instance is valid based on the data model definition. It checks if all required fields
        are present, if the values are in the value set, etc.

        :return: True if the instance is valid, False otherwise
        """
        error_msg = f"Instance values do not comply with their respective fields' valuesets. (row {self.row_no})"
        for v in self.values:
            if not v.validate():
                if self.compliance == 'strict':
                    raise ValueError(error_msg)
                elif self.compliance == 'lenient':
                    warnings.warn(error_msg)
                    return False
                else:
                    raise ValueError(f"Compliance level {self.compliance} is not valid")

        is_required = set(f.id for f in self.data_model.fields if f.required)
        fields_present = set(v.field.id for v in self.values)

        if len(missing_fields := (is_required - fields_present)) > 0:
            error_msg = (f"Required fields are missing in the instance. (row {self.row_no}) "
                         f"\n(missing_fields={', '.join(missing_fields)})")
            if self.compliance == 'strict':
                raise ValueError(error_msg)
            elif self.compliance == 'lenient':
                warnings.warn(error_msg)
                return False
            else:
                raise ValueError(f"Compliance level {self.compliance} is not valid")
        return True

    def __iter__(self):
        return iter(self.values)

    def __getattr__(self, var_name: str) -> DataFieldValue:
        fields = [v.field.id for v in self.values]
        if var_name in fields:
            return self.values[fields.index(var_name)]
        raise AttributeError(f"'DataModelInstance' object has no attribute '{var_name}'")


@dataclass(slots=True, frozen=True)
class DataSet:
    """This class defines a dataset as defined by a `DataModel`

    This class is used to define a dataset as defined by a `DataModel`. It is a collection of `DataModelInstance`
    objects.

    :ivar data_model: The `DataModel` object that defines the data model for this dataset
    :ivar data: A list of `DataModelInstance` objects, each adhering to the `DataField` definition in the `DataModel`
    """
    data_model: 'DataModel' = field()
    data: List[DataModelInstance] = field()

    @property
    def height(self):
        return len(self.data)

    @property
    def width(self):
        return len(self.data_model.fields)

    @property
    def data_frame(self) -> pd.DataFrame:
        column_names = [f.id for f in self.data_model.fields]
        data_dict = {c: list() for c in column_names}
        for instance in self.data:
            for f in self.data_model.fields:
                field_id = f.id
                value: Any = None
                try:
                    dfv: DataFieldValue = getattr(instance, field_id)
                    value = dfv.value
                except AttributeError:
                    pass
                finally:
                    data_dict[field_id].append(value)
        return pd.DataFrame(data_dict, columns=column_names)

    def __iter__(self):
        return iter(self.data)

    def preprocess(
            self,
            fields: Union[str, DataField, List[Union[str, DataField]]],
            mapping: Union[Dict, Callable],
            **kwargs
    ):
        """Preprocesses a field in the dataset

        Preprocessing happens in place, i.e. the values in the dataset are modified directly.

        If fields is a list of fields, the mapping must be a method that can handle a list of values being passed as
        value to it. E.g.:
        ```python
        def preprocess_method(values, method, **kwargs):
        field1, field2 = values
        # do something with values
        return "preprocessed_values" + kwargs["arg1"] + kwargs["arg2"]

        dataset.preprocess(["field_1", "field_2"], preprocess_method, arg1="value1", arg2="value2")
        ```

        :param fields: Data fields to be preprocessed, will be passed onto `mapping`
        :param mapping: A dictionary or method to use for preprocessing
        """
        if not isinstance(fields, list):
            fields = [fields]

        field_ids = list()
        for f in fields:
            if isinstance(field, str):
                field_ids.append(f)
            elif isinstance(f, DataField):
                field_ids.append(f.id)
            else:
                raise ValueError(f"Field {field} is not of type str or DataField")

        if len(field_ids) == 0:
            raise ValueError("No fields to preprocess")
        elif len(field_ids) == 1:
            field_id = field_ids[0]
            for instance in self.data:
                for v in instance.values:
                    if v.field.id == field_id:
                        v.value = preprocess(v.value, mapping, **kwargs)
        else:
            if isinstance(mapping, dict):
                raise ValueError("Mapping dictionary cannot be used to preprocess multiple fields")
            elif isinstance(mapping, Callable):
                values = dict()
                for instance in self.data:
                    for field_id in field_ids:
                        for v in instance.values:
                            if v.field.id == field_id:
                                values[field_id] = v.value

                preprocess_method(values, mapping, **kwargs)

    def head(self, n: int = 5):
        if self.data_frame is not None:
            return self.data_frame.head(n)
        else:
            warnings.warn("No data frame object available for this dataset")


if __name__ == "__main__":
    df = DataField(name="Field 1", specification=int)
    print(df.specification == ValueSet([int]))