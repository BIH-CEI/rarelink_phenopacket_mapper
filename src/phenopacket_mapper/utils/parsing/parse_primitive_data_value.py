from typing import Literal, Union


def parse_primitive_data_value(
        value_str: str
) -> Union[str, bool, int, float]:
    """Parses an int, float, bool, or string from a string value.

    Relies on the inbuilt Python type conversion functions to parse the value_str.

    :param value_str: The string value to be parsed.
    :return: The parsed value as an int, float, bool, or string.
    """
    # 1. Check if the value_str is a string
    if not isinstance(value_str, str):
        raise ValueError(f"Value must be a string, not {type(value_str)}")
    # 2. Remove spaces
    value_str = value_str.replace(" ", "")
    # 3. Check if the value_str is an int
    try:
        return int(value_str)
    except ValueError:
        pass
    # 4. Check if the value_str is a float
    try:
        return float(value_str)
    except ValueError:
        pass
    # 5. Check if the value_str is a bool
    if value_str.lower() == "true" or value_str.lower() == "t":
        return True
    if value_str.lower() == "false" or value_str.lower() == "f":
        return False
    # 6. Return the value_str as a string (definitely not an int, float, or bool, but is a string)
    return value_str
