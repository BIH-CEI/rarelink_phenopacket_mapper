from rarelink_phenopacket_mapper.data_standards import RarelinkData
from phenopackets import Phenopacket

from rarelink_phenopacket_mapper.data_standards.data_model import DataModel


class PhenopacketMapper:
    def __init__(self, datamodel: DataModel):
        self.datamodel = datamodel

    def map(self, rarelink_data: RarelinkData) -> Phenopacket:
        # TODO: Implement the mapping logic
        pass
