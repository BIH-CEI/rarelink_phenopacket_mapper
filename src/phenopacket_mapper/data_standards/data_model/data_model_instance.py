from dataclasses import dataclass
from typing import Union, List, Literal
import warnings

from . import DataModel, DataFieldValue


@dataclass(slots=True)
class DataModelInstance:
    """This class defines an instance of a `DataModel`, i.e. a record in a dataset

    This class is used to define an instance of a `DataModel`, i.e. a record or row in a dataset.

    :ivar row_no: The id of the instance, i.e. the row number
    :ivar data_model: The `DataModel` object that defines the data model for this instance
    :ivar values: A list of `DataFieldValue` objects, each adhering to the `DataField` definition in the `DataModel`
    :ivar compliance: Compliance level to enforce when validating the instance. If 'soft', the instance can have extra
                        fields that are not in the DataModel. If 'hard', the instance must have all fields in the
                        DataModel.
    """
    row_no: Union[int, str]
    data_model: DataModel
    values: List[DataFieldValue]
    compliance: Literal['soft', 'hard'] = 'soft'

    def __post_init__(self):
        self.validate()

    def validate(self) -> bool:
        """Validates the data model instance based on data model definition

        This method checks if the instance is valid based on the data model definition. It checks if all required fields
        are present, if the values are in the value set, etc.

        :return: True if the instance is valid, False otherwise
        """
        error_msg = f"Instance values do not comply with their respective fields' valuesets. (row {self.row_no})"
        for v in self.values:
            if not v.validate():
                if self.compliance == 'hard':
                    raise ValueError(error_msg)
                elif self.compliance == 'soft':
                    warnings.warn(error_msg)
                    return False
                else:
                    raise ValueError(f"Compliance level {self.compliance} is not valid")

        is_required = set(f.id for f in self.data_model.fields if f.required)
        fields_present = set(v.field.id for v in self.values)

        if len(missing_fields := (is_required - fields_present)) > 0:
            error_msg = (f"Required fields are missing in the instance. (row {self.row_no}) "
                         f"\n(missing_fields={', '.join(missing_fields)})")
            if self.compliance == 'hard':
                raise ValueError(error_msg)
            elif self.compliance == 'soft':
                warnings.warn(error_msg)
                return False
            else:
                raise ValueError(f"Compliance level {self.compliance} is not valid")
        return True

    def __iter__(self):
        return iter(self.values)

    def __getattr__(self, var_name: str) -> DataFieldValue:
        fields = [v.field.id for v in self.values]
        if var_name in fields:
            return self.values[fields.index(var_name)]
        raise AttributeError(f"'DataModelInstance' object has no attribute '{var_name}'")