from typing import Tuple
import re


def parse_ordinal(field_name_str: str) -> Tuple[str, str]:
    """
    Parsing `DataField.name` string to separate strings containing the ordinal and the name respectively

    This method is meant as part of reading in a `DataModel` from a file, where data model fields might have an ordinal
    attached to them (e.g., "1.1. Pseudonym"), which this method can then neatly separate into ordinal="1.1." and
    name="Pseudonym".

    >>> parse_ordinal("1.1. Pseudonym")
    ('1.1', 'Pseudonym')

    >>> parse_ordinal("1. Pseudonym")
    ('1', 'Pseudonym')

    >>> parse_ordinal("I.a. Pseudonym")
    ('I.a', 'Pseudonym')

    >>> parse_ordinal("ii. Pseudonym")
    ('ii', 'Pseudonym')

    :param field_name_str: name of the field, containing an ordinal, to parse
    :returns: a tuple containing the ordinal and the name
    """
    # Regex to extract the section number and field name
    match = re.match(r"([0-9]+(?:\.[0-9]+)*|[Iivxlc]+\.[a-z]*|[a-z]*)\.?\s*(.+)", field_name_str, re.IGNORECASE)

    if match:
        # Extract the field number and description
        ordinal = match.group(1).strip()
        field_name = match.group(2).strip()

        if ordinal[-1] == '.':
            ordinal = ordinal[0:-1]

        return ordinal, field_name
    else:
        return '', field_name_str  # since this is more for optics, do not raise error and just do "nothing"
