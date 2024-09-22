from dataclasses import dataclass, field

from phenopacket_mapper.data_standards import DataField


@dataclass(frozen=True, slots=True)
class MapField:
    """This class represents the mapping from a field of the ´DataModel´ to a field in a Phenopacket schema element

    :ivar from_field: The ´DataField´ from which the value is to map
    :ivar to_field: string name (e.g. "id") of the field in the phenopacket element (e.g. ´phenopackets.Phenopacket´)
                    to map to
    """
    from_field: DataField = field(init=True, repr=True)
    to_field: str = field(init=True, repr=True)
