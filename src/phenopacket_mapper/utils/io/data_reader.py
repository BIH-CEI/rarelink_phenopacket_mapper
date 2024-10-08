from pathlib import Path
from typing import Union, Tuple, List, Iterable

import pandas as pd

from phenopacket_mapper.utils.io import read_json, read_xml


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

        :return: The data and an iterable representation of the data.
        """
        if self.path.is_file():
            file_extension = self.path.suffix[1:]
            if file_extension == 'csv':
                df = pd.read_csv(self.path)
                return df, [row for row in df.iterrows()]
            elif file_extension == 'xlsx':
                df = pd.read_excel(self.path)
                return df, [row for row in df.iterrows()]
            else:
                raise ValueError(f'Unknown file type with extension {file_extension}')
        elif self.path.is_dir():
            # collect list of all files in the folder
            files: List[Path] = [file for file in self.path.iterdir() if file.is_file()]
            file_extension = list(set([file.suffix[1:] for file in files]))
            if len(file_extension) > 1:
                raise ValueError(f"Cannot read files of different types: {file_extension}")
            elif len(file_extension) == 0:
                raise ValueError(f"No files found in the directory specified: {self.path}")

            file_extension = file_extension[0]

            if file_extension.lower() == 'json':
                jsons = [read_json(file) for file in files]
                return jsons, jsons
            elif file_extension.lower() == 'xml':
                xmls = [read_xml(file) for file in files]
                return xmls, xmls
            else:
                raise ValueError(f"File extension {file_extension} not recognized for files in the specified directory"
                                 f": {self.path}.")
