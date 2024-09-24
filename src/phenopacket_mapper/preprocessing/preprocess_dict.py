from typing import Any, Dict


def preprocess_dict(value: Any, mapping_dict: Dict) -> Any:
    """Takes a value and uses a mapping dictionary to preprocess it.

    If the value is in the mapping dictionary, the corresponding value is returned.
    If the value is not in the mapping dictionary, the original value is returned.

    :param value: The value to preprocess.
    :param mapping_dict: A dictionary containing the mapping rules.
    :return: The preprocessed value.
    """
    try:
        ret_value = mapping_dict[value]
    except KeyError:
        ret_value = value
        print(f"Value {value} not found in mapping dictionary.")

    return ret_value
