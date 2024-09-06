from pathlib import Path
from typing import List, Union

from phenopackets import Phenopacket

from phenopacket_mapper.data_standards.DataModel2PhenopacketSchema import DataModel2PhenopacketSchema
from phenopacket_mapper.data_standards.data_model import DataModel, DataModelInstance
from phenopacket_mapper.data_standards.data_models import RARELINK_DATA_MODEL
from phenopacket_mapper.pipeline import read_file, validate


class PhenopacketMapper:
    """Class to map data using a DataModel to Phenopackets

    This class is central to the pipeline for mapping data from a DataModel to Phenopackets.
    A dataset can be mapped from its tabular format to the Phenopacket schema in a few simple steps:
    1. Define the DataModel for the dataset, if it does not exist yet
    2. Load the data from the dataset
    3. Define the mapping from the DataModel to the Phenopacket schema
    4. Perform the mapping
    5. Write the Phenopackets to a file
    6. Optionally validate the Phenopackets
    """
    def __init__(self, datamodel: DataModel):
        self.data_model = datamodel

    def load_data(self, path: Union[str, Path]) -> List[DataModelInstance]:
        """Load data from a file using the DataModel
        
        Will raise an error if the file type is not recognized or the file does not follow the DataModel

        :param path: Path to the file to load
        :return: List of DataModelInstances
        """
        return read_file(path=path, data_model=self.data_model)

    def map(self, mapping_: DataModel2PhenopacketSchema, data: List[DataModelInstance]) -> List[Phenopacket]:
        """Map data from the DataModel to Phenopackets

        The mapping is based on the definition of the DataModel and the DataModel2PhenopacketSchema mapping.

        If successful, a list of Phenopackets will be returned

        :param mapping_: Mapping from the DataModel to the Phenopacket schema, defined in DataModel2PhenopacketSchema
        :param data: List of DataModelInstances created from the data using the DataModel
        :return: List of Phenopackets
        """
        # TODO: Implement the mapping logic
        raise NotImplementedError

    def write(self, phenopackets: List[Phenopacket], output_path: Union[str, Path]) -> bool:
        """Write Phenopackets to a file

        :param phenopackets: List of Phenopackets to write
        :param output_path: Path to write the Phenopackets to
        :return: True if successful, False otherwise
        """
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
    data = mapper.load_data(path=path)
    # TODO: Define the mapping from the data model to the Phenopacket schema
    phenopackets = mapper.map(data)
    if mapper.write(phenopackets, output):
        print('Phenopackets written successfully')
    else:
        print('Error writing phenopackets')
    if validate_:
        validate(phenopackets)
    raise NotImplementedError("The function mapping has not been implemented yet")
