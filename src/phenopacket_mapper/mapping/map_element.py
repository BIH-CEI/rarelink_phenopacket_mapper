from dataclasses import dataclass, field
from typing import Any

from phenopacket_mapper.data_standards import DataModel, DataField

import phenopackets


@dataclass(frozen=True, slots=True)
class MapElement:
    """This class represents the mapping from an element of the ´DataModel´ to a field in the Phenopacket schema"""
    from_field: DataField = field(init=True, repr=True)
    to_field: str = field(init=True, repr=True)
