import argparse

from phenopacket_mapper.cli.quickstart_command import main as quickstart_main
from phenopacket_mapper.cli.mapping_command import main as mapping_main
from phenopacket_mapper.cli.validate_command import main as validate_main


def main():
    """Main entry point for the RareLink Phenopacket Mapper (rlpm) CLI.

    Run `rlpm -h` to see the available commands and further information.
    """
    parser = argparse.ArgumentParser(
        prog='rlpm',
        description='RareLink Phenopacket Mapper (rlpm) CLI tool.'
    )

    # Define subcommands
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Quickstart command
    parser_quickstart = subparsers.add_parser('quickstart', help='Generate a notebook with sample code.')
    parser_quickstart.add_argument('-p', '--path', type=str, help='Path the notebook should be written to')

    # Mapping command
    parser_mapping = subparsers.add_parser('mapping', help='Execute the mapping.')
    parser_mapping.add_argument('-p', '--path', type=str, help='Path to RareLink formatted csv or excel file')
    parser_mapping.add_argument('-o', '--output', type=str, help='Path to write Phenopackets to')
    parser_mapping.add_argument('-v', '--validate', action='store_true',
                                help='Validate phenopackets using phenopacket-tools after creation')

    # Validate command
    parser_validate = subparsers.add_parser('validate', help='Validate phenopackets.')
    parser_validate.add_argument('-p', '--path', type=str, help='Path to Phenopackets')

    args = parser.parse_args()

    # Route the command to the appropriate function
    if args.command == 'quickstart':
        quickstart_main(args)
    elif args.command == 'mapping':
        mapping_main(args)
    elif args.command == 'validate':
        validate_main(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
