from pathlib import Path
from typing import Union, Tuple, List, Iterable, Literal
import io

import pandas as pd

from phenopacket_mapper.utils.io import read_json, read_xml


class DataReader:
    def __init__(
            self,
            file: Union[str, Path, io.IOBase],
            encoding: str = 'utf-8',
            file_extension: Literal['csv', 'xlsx', 'json', 'xml'] = None
    ):
        """Initializes the data reader.

        :param file: a `str`, :class:`Path` or :class:`io.IOBase` to read from. If `str` or :class:`Path`, then the
        input is interpreted as a path to a local file.
        :param encoding: The encoding to use when reading the file. Default is 'utf-8'.
        :param file_extension: The file extension of the file to read. If `None`, the file extension is inferred from the
        file path. Default is `None`.
        """
        if isinstance(file, str):
            self.path = Path(file)
            self.file = open(self.path, "r", encoding=encoding)
        elif isinstance(file, Path):
            self.path = file
            self.file = open(self.path, "r", encoding=encoding)
        elif isinstance(file, io.IOBase):
            if isinstance(file, (io.TextIOWrapper, io.TextIOBase)):
                pass
            elif isinstance(file, (io.BytesIO, io.BufferedIOBase)):
                self.file = io.TextIOWrapper(file, encoding=encoding)

        self.data, self.iterable = self._read()




    def _read(self) -> Tuple[Union[pd.DataFrame, List], Iterable]:
        """Reads the data.

        :return: The data and an iterable representation of the data.
        """
        # change this to work with self.file
        if self.file.is_file():
            file_extension = self.file.suffix[1:]
            if file_extension == 'csv':
                df = pd.read_csv(self.file)
                return df, [row for row in df.iterrows()]
            elif file_extension == 'xlsx':
                df = pd.read_excel(self.file)
                return df, [row for row in df.iterrows()]
            else:
                raise ValueError(f'Unknown file type with extension {file_extension}')
        elif self.file.is_dir():
            # collect list of all files in the folder
            files: List[Path] = [file for file in self.file.iterdir() if file.is_file()]
            file_extension = list(set([file.suffix[1:] for file in files]))
            if len(file_extension) > 1:
                raise ValueError(f"Cannot read files of different types: {file_extension}")
            elif len(file_extension) == 0:
                raise ValueError(f"No files found in the directory specified: {self.file}")

            file_extension = file_extension[0]

            if file_extension.lower() == 'json':
                jsons = [read_json(file) for file in files]
                return jsons, jsons
            elif file_extension.lower() == 'xml':
                xmls = [read_xml(file) for file in files]
                return xmls, xmls
            else:
                raise ValueError(f"File extension {file_extension} not recognized for files in the specified directory"
                                 f": {self.file}.")
