from dataclasses import dataclass, field
from typing import Union

from phenopacket_mapper.data_standards.value_set import ValueSet


@dataclass(slots=True, frozen=True)
class DataField:
    """This class defines fields used in the definition of a `DataModel`

    A dataa field is the equivalent of a column in a table. It has a name, a value set, a description, a section, a
    required flag, a specification, and an ordinal.

    The string for the `id` field is generated from the `name` field using the `str_to_valid_id` function from the
    `phenopacket_mapper.utils` module. This attempts to convert the `name` field. Sometimes this might not work as
    desired, in which case the `id` field can be set manually.

    Naming rules for the `id` field:
    - The `id` field must be a valid Python identifier
    - The `id` field must start with a letter or the underscore character
    - The `id` field must cannot start with a number
    - The `id` field can only contain lowercase alpha-numeric characters and underscores (a-z, 0-9, and _ )
    - The `id` field cannot be any of the Python keywords (e.g. `in`, `is`, `not`, `class`, etc.).
    - The `id` field must be unique within a `DataModel`

    If the `value_set` is a single type, it can be passed directly as the `value_set` parameter.

    e.g.:
    >>> DataField(name="Field 1", value_set=int)
    DataField(name='Field 1', value_set=ValueSet(elements=[<class 'int'>], name='', description=''), id='field_1', description='', section='', required=True, specification='', ordinal='')

    :ivar name: Name of the field
    :ivar value_set: Value set of the field, if the value set is only one type, can also pass that type directly
    :ivar id: Id of the field, adhering to the naming rules stated above
    :ivar description: Description of the field
    :ivar section: Section of the field (Only applicable if the data model is divided into sections)
    :ivar required: Required flag of the field
    :ivar specification: Text specification of the field (a description of the value set and field)
    :ivar ordinal: Ordinal of the field (E.g. 1.1, 1.2, 2.1, etc.)
    """
    name: str = field()
    value_set: Union[ValueSet, type] = field()
    id: str = field(default=None)
    description: str = field(default='')
    section: str = field(default='')
    required: bool = field(default=True)
    specification: str = field(default='')
    ordinal: str = field(default='')

    def __post_init__(self):
        if not self.id:
            from phenopacket_mapper.utils import str_to_valid_id
            object.__setattr__(self, 'id', str_to_valid_id(self.name))

        if isinstance(self.value_set, type):
            object.__setattr__(self, 'value_set', ValueSet(elements=[self.value_set]))

    def __str__(self):
        ret = "DataField(\n"
        ret += f"\t\tid: {self.id},\n"
        ret += f"\t\tsection: {self.section},\n"
        ret += f"\t\tordinal, name: ({self.ordinal},  {self.name}),\n"
        ret += f"\t\tvalue_set: {self.value_set}, required: {self.required},\n"
        ret += f"\t\tspecification: {self.specification}\n"
        ret += "\t)"
        return ret
