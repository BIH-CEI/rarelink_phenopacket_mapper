from typing import Any, Callable


def preprocess_method(value: Any, method: Callable, **kwargs) -> Any:
    """Takes a value and uses a method to preprocess it.

    The method is called with the value as an argument.
    If the method raises an exception, the original value is returned.

    If the method requires additional arguments, they can be passed as keyword arguments in `kwargs`.

    Please write the method such that it is callable as `method(value, **kwargs)`.

    :param value: The value to preprocess.
    :param method: The method to use for preprocessing.
    :param kwargs: Additional arguments for the method.
    :return: The preprocessed value.
    """
    try:
        ret_value = method(value, **kwargs)
    except Exception as e:
        ret_value = value
        print(f"Error while preprocessing value {value} with method {method}. Error message: {e}")

    return ret_value
