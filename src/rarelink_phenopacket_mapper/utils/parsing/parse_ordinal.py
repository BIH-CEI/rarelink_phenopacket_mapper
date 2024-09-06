from typing import Tuple


def parse_ordinal(field_name_str: str) -> Tuple[str, str]:
    """
    Parsing `DataField.name` string to separate strings containing the ordinal and the name respectively

    This method is meant as part of reading in a `DataModel` from a file, where data model fields might have an ordinal
    attached to them (e.g., "1.1. Pseudonym"), which this method can then neatly separate into ordinal="1.1." and
    name="Pseudonym".

    >>>parse_ordinal("1.1. Pseudonym")
    ("1.1.", "Pseudonym")

    >>>parse_ordinal("1. Pseudonym")
    ("1.", "Pseudonym")

    >>>parse_ordinal("I.a. Pseudonym")
    ("I.a.", "Pseudonym")

    >>>parse_ordinal("ii. Pseudonym")
    ("ii.", "Pseudonym")
    """
    return "a", "b"
