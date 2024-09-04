import os
import argparse
from pathlib import Path


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

    validate(path)


def validate(path: Path) -> bool:
    """
    Validate phenopackets using phenopacket-tools.
    :param path: Path to Phenopackets
    :return: True if the phenopackets are valid, False otherwise
    """
    print(f"{path=}")
    raise NotImplementedError("The function mapping has not been implemented yet")
