from dataclasses import dataclass, field
from typing import List
import warnings

import pandas as pd

from . import DataFieldValue, DataModelInstance, DataModel


@dataclass(slots=True, frozen=True)
class DataSet:
    """This class defines a dataset as defined by a `DataModel`

    This class is used to define a dataset as defined by a `DataModel`. It is a collection of `DataModelInstance`
    objects.

    :ivar data_model: The `DataModel` object that defines the data model for this dataset
    :ivar data: A list of `DataModelInstance` objects, each adhering to the `DataField` definition in the `DataModel`
    :ivar data_frame: A pandas DataFrame representation of the dataset
    """
    data_model: DataModel = field()
    data: List[DataModelInstance] = field()

    @property
    def height(self):
        return len(self.data)

    @property
    def width(self):
        return len(self.data_model.fields)

    @property
    def data_frame(self) -> pd.DataFrame:
        column_names = [f.id for f in self.data_model.fields]
        data_dict = {c: list() for c in column_names}
        for instance in self.data:
            for f in self.data_model.fields:
                field_id = f.id
                try:
                    dfv: DataFieldValue = getattr(instance, field_id)
                    value = dfv.value
                except AttributeError:
                    value = None
                finally:
                    data_dict[field_id].append(value)
        return pd.DataFrame(data_dict, columns=column_names)

    def __iter__(self):
        return iter(self.data)

    def head(self, n: int = 5):
        if self.data_frame is not None:
            return self.data_frame.head(n)
        else:
            warnings.warn("No data frame object available for this dataset")