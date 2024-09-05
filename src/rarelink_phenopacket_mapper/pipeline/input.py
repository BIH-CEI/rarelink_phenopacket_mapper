from pathlib import Path
from types import MappingProxyType
from typing import Literal, List, Union, Dict

import pandas as pd
from phenopackets.schema.v2 import Phenopacket

from rarelink_phenopacket_mapper.data_standards import DataModel, DataModelInstance, DataField
from rarelink_phenopacket_mapper.data_standards.data_models import RARELINK_DATA_MODEL


def _read_csv(path: Path, data_model: DataModel) -> List[DataModelInstance]:
    """Helper function for `read_file`: csv file type

    :param path: Path to RareLink formatted csv file
    :param data_model: DataModel to use for reading the file
    :return: List of DataModelInstances
    """
    # TODO
    raise NotImplementedError


def _read_excel(path, data_model) -> List[DataModelInstance]:
    """Helper function for `read_file`: excel file types

    :param path: Path to RareLink formatted excel file
    :param data_model: DataModel to use for reading the file
    :return: List of DataModelInstances
    """
    # TODO
    raise NotImplementedError


def read_file(
        path: Union[str, Path],
        data_model: DataModel = RARELINK_DATA_MODEL,
        file_type: Literal['csv', 'excel', 'unknown'] = 'unknown',
) -> List[DataModelInstance]:
    """Reads a csv file in using a DataModel definition and returns a list of DataModelInstances

    :param path: Path to RareLink formatted csv or excel file
    :param file_type: Type of file to read, either 'csv' or 'excel'
    :param data_model: DataModel to use for reading the file
    :return: List of DataModelInstances
    """
    if file_type == 'unknown':
        file_type = path.suffix[1:]

    if file_type == 'csv':
        return _read_csv(path, data_model)
    elif file_type == 'excel':
        return _read_excel(path, data_model)
    else:
        raise ValueError(f"Unknown file type: {file_type}")


def read_data_model(
        name: str,
        path: Union[str, Path],
        file_type: Literal['csv', 'excel', 'unknown'] = 'unknown',
        column_names: Dict[str, str] = MappingProxyType({
            'name': 'name',
            'section': '',
            'description': 'description',
            'data_type': 'data_type',
            'required': 'required',
            'specification': '',
            'ordinal': ''
        }),
) -> DataModel:
    """Reads a Data Model from a file

    :param name: Name to be given to the `DataModel` object
    :param path: Path to Data Model file
    :param file_type: Type of file to read, either 'csv' or 'excel'
    :param column_names: A dictionary mapping from each field of the `DataField` (key) class to a column of the file
                        (value). Leaving a value empty (`''`) will leave the field in the `DataModel` definition empty.
    """
    if isinstance(column_names, MappingProxyType):
        inv_column_names = dict(column_names)
    if file_type == 'unknown':
        file_type = path.suffix[1:]

    if file_type == 'csv':
        df = pd.read_csv(path)
    elif file_type == 'excel':
        df = pd.read_excel(path)
    else:
        raise ValueError('Unknown file type')

    # Change NaN values to None
    df = df.where(pd.notnull(df), None)
    # invert column names
    inv_column_names = {v: k for k, v in column_names.items()}

    # remove empty assignments
    inv_column_names = {k: inv_column_names[k] for k in list(filter(lambda x: x != '', inv_column_names.keys()))}

    # check that column_names.keys() is a subsets of the columns in the file
    df_columns = list(df)
    print(f"{df_columns=}")
    keep = []
    for col_n in inv_column_names.keys():
        if col_n in df_columns:
            keep.append(col_n)

    inv_column_names = {k: inv_column_names[k] for k in keep}

    if len(inv_column_names) == 0:
        raise ValueError("The column names dictionary that was passed is invalid.")

    for col in inv_column_names.keys():
        print(f"Column {col} maps to DataField.{inv_column_names[col]}")

    column_names = {v: k for k, v in inv_column_names.items()}

    data_fields = []
    for i in range(len(df)):
        data_fields.append(
            DataField(
                name=df.loc[i, column_names.get('name', '')],
                section=df.loc[i, column_names.get('section', '')],
                data_type=df.loc[i, column_names.get('data_type', '')],
                description=df.loc[i, column_names.get('description', '')],
                required=bool(df.loc[i, column_names.get('required', '')]),
                specification=df.loc[i, column_names.get('specification', '')],
            )
        )

    return DataModel(name=name, fields=data_fields)


def read_redcap_api(data_model: DataModel) -> List[DataModelInstance]:
    """Reads data from REDCap API and returns a list of DataModelInstances

    :param data_model: DataModel to use for reading the file
    :return: List of DataModelInstances
    """
    # TODO
    raise NotImplementedError


def read_phenopackets(path: Path) -> List[Phenopacket]:
    """Reads Phenopackets from a file

    :param path: Path to Phenopackets file
    :return: List of Phenopackets
    """
    # TODO
    raise NotImplementedError
