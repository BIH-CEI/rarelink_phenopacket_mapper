from pathlib import Path
from typing import List, Union

from phenopackets.schema.v2 import Phenopacket


def write(phenopackets: List[Phenopacket], output_path: Union[str, Path]):
    """
    Write a list of phenopackets to a file
    :param phenopackets: List of phenopackets
    :param output_path: the path to write the phenopackets to
    """
    raise NotImplementedError
