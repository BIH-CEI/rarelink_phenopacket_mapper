import argparse
from pathlib import Path

from rarelink_phenopacket_mapper.cli.validate import validate


def main(args):
    """This method launches the mapping command"""
    arg_parser = argparse.ArgumentParser(
        prog='mapping',
        description='executes the pipeline mapping a dataset in the RareLink format to the Phenopacket schema'
    )

    arg_parser.add_argument('-p', '--path', type=str,
                            help='Path to RareLink formatted csv or excel file')

    arg_parser.add_argument('-o', '--output', type=str,
                            help='Path to write Phenopackets to')

    arg_parser.add_argument('-v', '--validate', action='store_true',
                            help='Validate phenopackets using phenopacket-tools after creation')

    args = arg_parser.parse_args()

    if args.path:
        path = Path(args.path)
    else:
        raise AttributeError("Path argument is misssing")

    if args.output:
        output = Path(args.output)
    else:
        raise AttributeError("Output argument is misssing")

    if args.validate:
        validate_ = True
    else:
        validate_ = False

    mapping(path, output, validate_)


def mapping(path: Path, output: Path, validate_: bool):
    print(f"{path=}, {output=}, {validate_=}")
    if validate_:
        validate(path=output)
    raise NotImplementedError("The function mapping has not been implemented yet")
