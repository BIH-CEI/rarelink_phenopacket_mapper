import os
import argparse
from pathlib import Path

from rarelink_phenopacket_mapper.pipeline import read_phenopackets
from rarelink_phenopacket_mapper.pipeline.validate import validate


def main(args):
    """Validate Command: syntactically validates phenopackets using phenopacket-tools.

    Run `validate -h` for help."""
    if args.path:
        path = Path(args.path)
    else:
        path = Path(os.getcwd())

    phenopackets = read_phenopackets(path)

    validate(phenopackets)
