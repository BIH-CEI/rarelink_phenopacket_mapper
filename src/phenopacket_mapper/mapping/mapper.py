import warnings
from dataclasses import field, dataclass
from pathlib import Path
from typing import List, Union

from phenopackets import Phenopacket

from phenopacket_mapper.data_standards.DataModel2PhenopacketSchema import DataModel2PhenopacketSchema
from phenopacket_mapper.data_standards.data_model import DataSet
from phenopacket_mapper.mapping import PhenopacketElement


@dataclass(frozen=True, slots=True)
class PhenopacketMapper:
    """Class to map data to Phenopackets

    """
    data_set: DataSet = field()
    elements: List[PhenopacketElement] = field()

    def __post_init__(self):
        dm = self.data_set.data_model
        for e in self.elements:
            for f in e.fields:
                if f.from_field not in dm:
                    raise AttributeError(f"The mapping definition contains an invalid step. "
                                         f"{f.from_field} is not in the data model underlying the passed data set."
                                         f" (The data model includes the fields: {dm.get_field_ids()})")

    def map(self, mapping_: DataModel2PhenopacketSchema, data: DataSet) -> List[Phenopacket]:
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


def mapping(path: Path, output: Path, validate_: bool, datamodel: DataModel = ERDRI_CDS):
    """Executes the pipeline mapping a dataset in the  format to the Phenopacket schema

    :param path: Path to  formatted csv or excel file
    :param output: Path to write Phenopackets to
    :param validate_: Validate phenopackets using phenopacket-tools after creation
    :param datamodel: DataModel to use for the mapping, defaults to 
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
