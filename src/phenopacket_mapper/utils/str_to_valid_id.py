def str_to_valid_id(s: str) -> str:
    """Converts a string to a valid id

    This function converts a string to a valid id by replacing spaces with underscores and removing all other
    non-alphanumeric characters.

    :param s: The string to convert to a valid id
    :return: The valid id
    """
    if s is None or not isinstance(s, str) or len(s) == 0:
        raise ValueError("The input string must be a non-empty string.")

    if not s[0].isalpha():
        s = f"_{s}"
    return s.lower().replace(' ', '_')
