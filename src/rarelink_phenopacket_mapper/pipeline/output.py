from pathlib import Path
from typing import List, Union

from phenopackets.schema.v2 import Phenopacket


def write(phenopackets: List[Phenopacket], output_path: Union[str, Path]):
    raise NotImplementedError
