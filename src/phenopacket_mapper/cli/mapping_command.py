from pathlib import Path


def main(args):
    """Mapping command: Executes the pipeline mapping a dataset in the  format to the Phenopacket schema

    This method launches the mapping command, which executes the pipeline mapping a dataset in the  format to
    the Phenopacket schema.

    The mapping command is intended to remove the necessity of writing code to run the mapping while
    slightly reducing the flexibility of the mapping process. For more options we recommend performing the mapping
    programmatically.

    Run `pm mapping -h` for help.
    """
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

    # mapping(path, output, validate_)
    raise NotImplementedError
