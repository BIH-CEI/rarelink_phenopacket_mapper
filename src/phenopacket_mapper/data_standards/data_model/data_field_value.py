from dataclasses import dataclass
from typing import Union, Any
import warnings

from . import DataField
from phenopacket_mapper.data_standards import CodeSystem
from phenopacket_mapper.data_standards.date import Date


@dataclass(slots=True, frozen=True)
class DataFieldValue:
    """This class defines the value of a `DataField` in a `DataModelInstance`

    Equivalent to a cell value in a table.

    :ivar row_no: The id of the value, i.e. the row number
    :ivar field: DataField: The `DataField` to which this value belongs and which defines the value set for the field.
    :ivar value: The value of the field.
    """
    row_no: Union[str, int]
    field: DataField
    value: Union[int, float, str, bool, Date, CodeSystem]

    def validate(self) -> bool:
        """Validates the data model instance based on data model definition

        This method checks if the instance is valid based on the data model definition. It checks if all required fields
        are present, if the values are in the value set, etc.

        :return: True if the instance is valid, False otherwise
        """
        if self.field.required and self.value is None:  # no value
            warnings.warn(f"Field {self.field.name} is required but has no value")
            return False
        elif self.value is not None and self.field.value_set:
            if Any in self.field.value_set:  # value set allows any
                return True
            elif self.value in self.field.value_set:  # raw value (likely a primitive) is in the value set
                return True
            else:  # check if the value matches one of the types in the value set
                for e in self.field.value_set:
                    if isinstance(e, type):
                        cur_type = e
                        if cur_type is type(self.value):
                            return True
                    elif isinstance(e, CodeSystem):
                        cs = e
                        from phenopacket_mapper.data_standards import Coding
                        if isinstance(self.value, Coding) and self.value.system == cs:
                            return True

        warnings.warn(f"Value {self.value} of type {type(self.value)} is not in the value set of field "
                      f"{self.field.name} (row {self.row_no})")
        return False