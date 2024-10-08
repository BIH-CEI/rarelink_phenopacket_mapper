"""This module handles the input and output of data."""

from .input import read_data_model, read_phenopackets, read_phenopacket_from_json, load_data_using_data_model
from .output import write

__all__ = [
    'read_data_model',
    'read_phenopackets',
    'read_phenopacket_from_json',
    'load_data_using_data_model',

    'write',
]
