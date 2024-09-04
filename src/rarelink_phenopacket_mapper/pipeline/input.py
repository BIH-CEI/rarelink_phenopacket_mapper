from pathlib import Path
from typing import Literal, List, Union

from rarelink_phenopacket_mapper.data_standards import DataModel, DataModelInstance
from rarelink_phenopacket_mapper.data_standards.data_models import RARELINK_DATA_MODEL


def _read_csv(path, data_model) -> List[DataModelInstance]:
    # TODO
    raise NotImplementedError


def _read_excel(path, data_model) -> List[DataModelInstance]:
    # TODO
    raise NotImplementedError


def read_file(
        path: Union[str, Path],
        data_model: DataModel = RARELINK_DATA_MODEL,
        file_type: Literal['csv', 'excel', 'unknown'] = 'unknown',
) -> List[DataModelInstance]:
    """Reads a dataset in the RareLink format and returns a list of DataModelInstances

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


def read_redcap_api() -> List[DataModelInstance]:
    # TODO
    raise NotImplementedError
