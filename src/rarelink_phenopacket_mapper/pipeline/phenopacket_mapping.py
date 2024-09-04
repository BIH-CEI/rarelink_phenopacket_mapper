from rarelink_phenopacket_mapper.data_standards import RarelinkData
from phenopackets import Phenopacket

from rarelink_phenopacket_mapper.data_standards.rarelink_data import DataModel


class PhenoPacketMapper:
    def __init__(self, datamodel: DataModel):
        self.datamodel = datamodel

    def map(self, rarelink_data: RarelinkData) -> Phenopacket:
        # TODO: Implement the mapping logic
        pass
