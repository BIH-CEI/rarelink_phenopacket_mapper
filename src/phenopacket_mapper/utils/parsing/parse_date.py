from datetime import datetime
from typing import Literal, re

from phenopacket_mapper.data_standards import Date


def parse_date(
        date_str: str,
        compliance: Literal['soft', 'hard'] = 'soft'
) -> Date:
    """Parse a date string into a Date object

    :param date_str: the date string to parse
    :param compliance: the compliance level of the parser
    :return: the Date object created from the date string
    """
    formats = [
        "%Y-%m-%d %H:%M:%S",  # Full date with time
        "%Y-%m-%d",           # Full date without time
        "%d/%m/%Y",           # Day-first format
        "%d.%m.%Y",           # Day-first format with dots
        "%d-%m-%Y",           # Day-first format with dashes
        "%Y-%m",              # Year and month
        "%m-%Y",              # Month and year
        "%Y"                  # Year only
    ]

    for fmt in formats:
        try:
            dt = datetime.strptime(date_str, fmt)
            return Date(
                year=dt.year,
                month=dt.month,
                day=dt.day,
                hour=dt.hour,
                minute=dt.minute,
                second=dt.second
            )
        except ValueError:
            continue

    raise ValueError(f"Date string does not match any supported format: {date_str}")
