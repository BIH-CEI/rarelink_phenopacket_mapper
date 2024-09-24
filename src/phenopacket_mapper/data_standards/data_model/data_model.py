from dataclasses import dataclass, field
from pathlib import Path
from types import MappingProxyType
from typing import Union, List, Literal, Dict, Optional

from phenopacket_mapper.data_standards import CodeSystem
from . import DataSet, DataField
from phenopacket_mapper.data_standards.value_set import ValueSet


@dataclass(slots=True, frozen=True)
class DataModel:
    """This class defines a data model for medical data using `DataField`

    A data model can be used to import data and map it to the Phenopacket schema. It is made up of a list of `DataField`

    Given that all `DataField` objects in a `DataModel` have unique names, the `id` field is generated from the `name`.
    E.g.: `DataField(name='Date of Birth', ...)` will have an `id` of `'date_of_birth'`. The `DataField` objects can
    be accessed using the `id` as an attribute of the `DataModel` object. E.g.: `data_model.date_of_birth`. This is
    useful in the data reading and mapping processes.

    >>> data_model = DataModel("Test data model", [DataField(name="Field 1", value_set=ValueSet())])
    >>> data_model.field_1
    DataField(name='Field 1', value_set=ValueSet(elements=[], name='', description=''), id='field_1', description='', section='', required=True, specification='', ordinal='')

    :ivar data_model_name: Name of the data model
    :ivar fields: List of `DataField` objects
    :ivar resources: List of `CodeSystem` objects
    """
    data_model_name: str = field()
    fields: List[DataField] = field()
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
        for field in self.fields:
            ret += f"\t{str(field)}\n"
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
            compliance: Literal['soft', 'hard'] = 'soft',
            **kwargs
    ) -> DataSet:
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
            column_names: Dict[str, str],
            compliance: Literal['soft', 'hard'] = 'soft',
    ) -> DataSet:
        """Loads data from a file using a DataModel definition

        :param path: Path to  formatted csv or excel file
        :param data_model: DataModel to use for reading the file
        :param column_names: A dictionary mapping from the id of each field of the `DataField` to the name of a
                            column in the file
        :param compliance: Compliance level to enforce when reading the file. If 'soft', the file can have extra fields
                            that are not in the DataModel. If 'hard', the file must have all fields in the DataModel.
        :return: List of DataModelInstances
        """
        from phenopacket_mapper.pipeline import load_data_using_data_model
        return load_data_using_data_model(
            path=path,
            data_model=data_model,
            column_names=column_names,
            compliance=compliance
        )
