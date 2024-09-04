import os
import argparse
from pathlib import Path


def main():
    """This method launches the quickstart command"""
    arg_parser = argparse.ArgumentParser(
        prog='quickstart',
        description='generate a notebook with some sample code to run the mapping. By default writes it to the current'
                    'working directory.'
    )

    arg_parser.add_argument('-p', '--path', type=str, action='store_true',
                            help='Path the notebook should be written to')

    args = arg_parser.parse_args()

    if args.path:
        path = Path(args.path)
    else:
        path = Path(os.getcwd())

    quickstart(path)


def quickstart(path: Path):
    print(f"{path=}")
    raise NotImplementedError('Has not been implemented yet')


if __name__ == "__main__":
    main()
