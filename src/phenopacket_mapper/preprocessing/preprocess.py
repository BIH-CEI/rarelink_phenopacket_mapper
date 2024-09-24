import warnings
from typing import Any, Union, Dict, Callable

from phenopacket_mapper.preprocessing import preprocess_dict, preprocess_method


def preprocess(
        value: Any,
        mapping: Union[Dict, Callable],
        **kwargs
) -> Any:
    """Preprocess a value before mapping to a Phenopacket.

    Relies on `preprocess_dict` and `preprocess_method` to preprocess using a dictionary or method, respectively. Please
    consult the documentation for these functions for more information.
    """
    if isinstance(mapping, dict):
        return preprocess_dict(value, mapping)
    elif isinstance(mapping, Callable):
        return preprocess_method(value, mapping, **kwargs)

    warnings.warn(f"Mapping type {type(mapping)} in preprocessing not supported. Returning original value.")
    return value
