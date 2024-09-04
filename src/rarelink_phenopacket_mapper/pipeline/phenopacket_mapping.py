from typing import List

from phenopackets import Phenopacket

from rarelink_phenopacket_mapper.data_standards.data_model import DataModel, DataModelInstance


class PhenopacketMapper:
    def __init__(self, datamodel: DataModel):
        self.datamodel = datamodel

    def map(self, rarelink_data: List[DataModelInstance]) -> Phenopacket:
        # TODO: Implement the mapping logic
        pass
