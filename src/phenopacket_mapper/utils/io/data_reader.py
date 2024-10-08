from pathlib import Path
from typing import Union, Tuple, List, Iterable

import pandas as pd


class DataReader:
    def __init__(
            self,
            path: Union[str, Path],
    ):
        """Initializes the data reader.

        :param path: The path to the data.
        """
        if isinstance(path, str):
            path = Path(path)
        self.path = path
        self.data, self.iterable = self._read()




    def _read(self) -> Tuple[Union[pd.DataFrame, List], Iterable]:
        """Reads the data.

        :return: The data.
        """
        file_extension = self.path.suffix[1:]
        # TODO: add support for folder of json or xml files for non tabular
        if file_extension == 'csv':
            df = pd.read_csv(self.path)
            return df, [row for row in df.iterrows()]
        elif file_extension == 'xlsx':
            df = pd.read_excel(self.path)
            return df, [row for row in df.iterrows()]
        else:
            raise ValueError(f'Unknown file type with extension {file_extension}')