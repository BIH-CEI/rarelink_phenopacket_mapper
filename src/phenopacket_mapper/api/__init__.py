"""
This package is intended to expose the PhenopacketMapper API to the user.
"""

import abc
import typing


class DataModelDefiner(metaclass=abc.ABCMeta):
    """
    Take some data model definition and try to load it into data model.

    E.g. protobuf model "definer".
    """
    pass


class DataModel(metaclass=abc.ABCMeta):
    """
    Value class.
    The fields:
     - label, version
     - a root `DataNode`, it must be there (not `Optional`)
     - resources (maybe generate dynamically, or keep as a list)

    We want to be able to (de)serialize this.
    """
    pass


class DataNode(metaclass=abc.ABCMeta):
    """
    This is very much like Jackson (Java) `TreeNode`,
    because it can be many things.

    The common things may include
    - label
    - maybe it knows about the parent (optional) and children

    We want to be able to (de)serialize this.
    """
    pass


class DataInstance:
    pass


class Transformation(metaclass=abc.ABCMeta):
    """

    """
    pass


class Mapper:

    def __init__(
        self,
        transformation: Transformation,
    ):
        pass

    def transform_dataset(
        self,
        data_set: typing.Iterable[DataInstance],
    ) -> typing.Iterator[DataInstance]:
        return map(lambda item: self.transform(item), data_set)

    def transform(self, item: DataInstance) -> DataInstance:
        # TODO: implement
        pass
