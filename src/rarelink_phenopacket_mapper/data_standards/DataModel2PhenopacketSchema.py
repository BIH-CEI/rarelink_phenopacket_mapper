from dataclasses import dataclass

from rarelink_phenopacket_mapper.data_standards import DataModel


@dataclass
class DataModel2PhenopacketSchema:
    def __init__(self, datamodel: DataModel):
        self.data_model = datamodel