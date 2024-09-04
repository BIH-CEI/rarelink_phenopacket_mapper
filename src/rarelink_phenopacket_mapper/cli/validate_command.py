import os
import argparse
from pathlib import Path

from rarelink_phenopacket_mapper.pipeline import read_phenopackets
from rarelink_phenopacket_mapper.pipeline.validate import validate


def main(args):
    """Validate Command: syntactically validates phenopackets using phenopacket-tools.

    Run `validate -h` for help."""
    arg_parser = argparse.ArgumentParser(
        prog='validate',
        description='syntactically validates phenopackets using phenopacket-tools'
    )

    arg_parser.add_argument('-p', '--path', type=str,
                            help='Path to Phenopackets')

    args = arg_parser.parse_args()

    if args.path:
        path = Path(args.path)
    else:
        path = Path(os.getcwd())

    phenopackets = read_phenopackets(path)

    validate(phenopackets)
