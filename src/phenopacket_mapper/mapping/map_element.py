from dataclasses import dataclass, field

from phenopacket_mapper.data_standards import DataModel, DataField


@dataclass(frozen=True)
class MapElement:
    data_model: DataModel = field(init=True, repr=False)
    from_field: DataField = field(init=True, repr=True)
    to_field: str = field(init=True, repr=True)