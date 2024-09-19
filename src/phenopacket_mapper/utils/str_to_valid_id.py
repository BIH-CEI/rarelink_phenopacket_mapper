import keyword
import re


def str_to_valid_id(s: str) -> str:
    """Converts a string to a valid id

    This function converts a string to a valid id by replacing spaces with underscores and removing all other
    non-alphanumeric characters.

    :param s: The string to convert to a valid id
    :return: The valid id
    """
    if s is None or not isinstance(s, str) or len(s) == 0:
        raise ValueError("The input string must be a non-empty string.")

    s = re.sub(r'\W|^(?=\d)', '_', s)

    if not s[0].isalpha() and s[0] != '_':
        s = f"_{s}"

    while '__' in s:
        s = s.replace('__', '_')

    s = s.lower()

    if keyword.iskeyword(s):
        s += '_'

    if len(s) == 0:
        raise ValueError("The input string must be a non-empty string after removal of invalid characters.")

    return s
