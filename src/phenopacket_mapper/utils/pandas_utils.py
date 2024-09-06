from typing import Any

import pandas as pd


def loc_default(df: pd.DataFrame, row_index: int, column_name: str, default: Any = '') -> Any:
    """Safely performs loc on a `pd.DataFrame`, returns default value if something goes wrong

    :param df: the dataframe
    :param row_index: index of the row
    :param column_name: name of the column
    :param default: default value to return if some error occurs
    :return: Value at the row and column specified
    """
    try:
        return df.loc[row_index, column_name]
    except Exception as e:
        print(e)
        return default
