import os
import argparse
from pathlib import Path


def main(args):
    """Quickstart command: Generate notebook with sample code to run the mapping.

    This method launches the quickstart command, which generates a notebook with some sample code to run the mapping.
    The quickstart notebook is intended to help users get started with the mapping process, especially if they are new
    or unexperienced in writing code.

    Run `quickstart -h` for help."""
    arg_parser = argparse.ArgumentParser(
        prog='quickstart',
        description='generate a notebook with some sample code to run the mapping. By default writes it to the current'
                    'working directory.'
    )

    arg_parser.add_argument('-p', '--path', type=str,
                            help='Path the notebook should be written to')

    args = arg_parser.parse_args()

    if args.path:
        path = Path(args.path)
    else:
        path = Path(os.getcwd())

    quickstart(path)


def quickstart(path: Path):
    """
    Generate a notebook with some sample code to run the mapping. The notebook is intended to help users get started
    with the mapping process, especially if they are new or unexperienced in writing code.

    :param path: Path to write the notebook to
    """
    print(f"{path=}")
    raise NotImplementedError('Has not been implemented yet')
