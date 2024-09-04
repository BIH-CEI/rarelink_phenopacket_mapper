import os
import argparse
from pathlib import Path

from rarelink_phenopacket_mapper.utils.create_ipynb_in_code import NotebookBuilder


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

    _quickstart(path)


def _quickstart(path: Path):
    """
    Generate a notebook with some sample code to run the mapping. The notebook is intended to help users get started
    with the mapping process, especially if they are new or unexperienced in writing code.

    :param path: Path to write the notebook to
    """
    builder = NotebookBuilder()
    builder.add_markdown_cell("# RareLink Phenopacket Mapper Quickstart Guide")
    builder.add_code_cell("import rarelink_phenopacket_mapper as rlpm")
    builder.add_markdown_cell("## Select a Data Model or define your own")
    builder.add_code_cell("data_model = rlpm.data_standards.data_models.RARELINK_DATA_MODEL")
    builder.add_markdown_cell("## Create the Phenopacket Mapper object")
    builder.add_code_cell("mapper = rlpm.PhenopacketMapper(data_model)")
    builder.add_markdown_cell("## Load data from a file\n\nOptionally, you can load data directly from the REDCap API.")
    builder.add_code_cell("path_to_data = 'data/rarelink_examples'\ndata = mapper.load_data(path=path_to_data)")
    builder.add_markdown_cell("## Define a mapping from the data model to the Phenopacket schema")
    builder.add_code_cell("# TODO: Define the mapping from the data model to the Phenopacket schema")
    builder.add_markdown_cell("## Perform the mapping")
    builder.add_code_cell("phenopackets = mapper.map(data)")
    builder.add_markdown_cell("## Write the phenopackets to a file")
    builder.add_code_cell("output_path = 'data/phenopacket_examples'\nif mapper.write(phenopackets, output_path):\t"
                          "\n\tprint('Phenopackets written successfully')\nelse:\n\tprint('Error writing phenopackets')")
    builder.add_markdown_cell("## [OPTIONAL] Validate the phenopackets")
    builder.add_code_cell("print('Successful validation:', mapper.validate(phenopackets))\nprint('Successful "
                          "validation (including reading from a file):', rlpm.pipeline.read_validate(output_path))")
    builder.write_to_file(path / 'quickstart.ipynb')
