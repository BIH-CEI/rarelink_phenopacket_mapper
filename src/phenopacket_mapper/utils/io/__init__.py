"""This module handles the input and output of data."""

from .read_json import read_json
from .read_xml import read_xml
from .data_reader import DataReader
from .input import read_data_model, read_phenopackets, read_phenopacket_from_json, load_data_using_data_model
from .output import write

__all__ = [
    'read_json',
    'read_xml',
    'DataReader',
    'read_data_model',
    'read_phenopackets',
    'read_phenopacket_from_json',
    'load_data_using_data_model',

    'write',
]
