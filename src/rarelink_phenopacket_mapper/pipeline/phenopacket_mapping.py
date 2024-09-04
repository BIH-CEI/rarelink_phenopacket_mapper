from pathlib import Path
from typing import List, Union

from phenopackets import Phenopacket

from rarelink_phenopacket_mapper.data_standards.data_model import DataModel, DataModelInstance
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
