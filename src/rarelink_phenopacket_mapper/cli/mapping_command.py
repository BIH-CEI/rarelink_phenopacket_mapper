import argparse
from pathlib import Path

from rarelink_phenopacket_mapper.cli.validate_command import validate
from rarelink_phenopacket_mapper.data_standards.data_models import RARELINK_DATA_MODEL
from rarelink_phenopacket_mapper.data_standards.data_model import DataModel
from rarelink_phenopacket_mapper.pipeline.mapping import PhenopacketMapper


def main(args):
    """Mapping command: Executes the pipeline mapping a dataset in the RareLink format to the Phenopacket schema

    This method launches the mapping command, which executes the pipeline mapping a dataset in the RareLink format to
    the Phenopacket schema.

    The mapping command is intended to remove the necessity of writing code to run the mapping while
    slightly reducing the flexibility of the mapping process. For more options we recommend performing the mapping
    programmatically.

    Run `mapping -h` for help.
    """
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
