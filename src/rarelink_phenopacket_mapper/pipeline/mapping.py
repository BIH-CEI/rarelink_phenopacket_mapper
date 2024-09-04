from pathlib import Path
from typing import List, Union

from phenopackets import Phenopacket

from rarelink_phenopacket_mapper.cli import validate
from rarelink_phenopacket_mapper.data_standards.data_model import DataModel, DataModelInstance
from rarelink_phenopacket_mapper.data_standards.data_models import RARELINK_DATA_MODEL
from rarelink_phenopacket_mapper.pipeline import read_file


class PhenopacketMapper:
    def __init__(self, datamodel: DataModel):
        self.data_model = datamodel

    def load_data(self, path: Union[str, Path]) -> List[DataModelInstance]:
        return read_file(path=path, data_model=self.data_model)

    def map(self, rarelink_data: List[DataModelInstance]) -> List[Phenopacket]:
        # TODO: Implement the mapping logic
        raise NotImplementedError

    def write(self, phenopackets: List[Phenopacket], output_path: Union[str, Path]) -> bool:
        raise NotImplementedError


def mapping(path: Path, output: Path, validate_: bool, datamodel: DataModel = RARELINK_DATA_MODEL):
    """Executes the pipeline mapping a dataset in the RareLink format to the Phenopacket schema

    :param path: Path to RareLink formatted csv or excel file
    :param output: Path to write Phenopackets to
    :param validate_: Validate phenopackets using phenopacket-tools after creation
    :param datamodel: DataModel to use for the mapping, defaults to RareLink
    """
    print(f"{path=}, {output=}, {validate_=}")
    mapper = PhenopacketMapper(datamodel=datamodel)
    if validate_:
        validate(path=output)
    raise NotImplementedError("The function mapping has not been implemented yet")
