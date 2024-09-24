"""
This module defines the `DataModel` class, which is used to define a data model for medical data. A `DataModel` is a
collection of `DataField` objects, which define the fields of the data model. Each `DataField` has a name, a value set,
a description, a section, a required flag, a specification, and an ordinal. The `DataModel` class also has a list of
`CodeSystem` objects, which are used as resources in the data model.

The `DataFieldValue` class is used to define the value of a `DataField` in a `DataModelInstance`. The
`DataModelInstance` class is used to define an instance of a `DataModel`, i.e. a record in a dataset.
"""

from .data_field import DataField
from .data_field_value import DataFieldValue
from .data_model import DataModel
from .data_model_instance import DataModelInstance
from .data_set import DataSet

__all__ = [
    "DataField",
    "DataFieldValue",
    "DataModel",
    "DataModelInstance",
    "DataSet",
]
