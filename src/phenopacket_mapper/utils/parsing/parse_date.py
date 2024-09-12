from datetime import datetime
from typing import Literal

from phenopacket_mapper.data_standards import Date
from phenopacket_mapper.utils.parsing import parse_int


def parse_date(
        date_str: str,
        compliance: Literal['soft', 'hard'] = 'soft'
) -> Date:
    """Parse a date string into a Date object

    :param date_str: the date string to parse
    :param compliance: the compliance level of the parser
    :return: the Date object created from the date string
    """
    separators = ['-', '/', '.']
    # check length
    if len(date_str) < 4:
        raise ValueError(f"Invalid date string '{date_str}': too short")

    iso_result = Date.from_iso_8601(date_str)

    if iso_result is not None:
        return iso_result

    contains_separators = any([s in date_str for s in separators])

    if contains_separators:
        date_str = date_str.replace('/', '-').replace('.', '-')
        units = date_str.split('-')

        # figure out which units are which
        if len(units) == 1 and len(units[0]) == 4:  # just a year
            return Date(year=parse_int(units[0]))
        elif len(units) == 2:
            if len(units[0]) == 4:  # year and month
                return Date(year=parse_int(units[0]), month=parse_int(units[1]))
            else:  # month and year
                return Date(year=parse_int(units[1]), month=parse_int(units[0]))
        elif len(units) == 3:
            if len(units[0]) == 4:
                # figure out if the day is second or third
                return Date(year=parse_int(units[0]), month=parse_int(units[1]), day=parse_int(units[2]))
            elif len(units[1]) == 4:
                return Date(year=parse_int(units[2]), month=parse_int(units[0]), day=parse_int(units[1]))
            elif len(units[2]) == 4:
                return Date(year=parse_int(units[1]), month=parse_int(units[2]), day=parse_int(units[0]))
    else:
        if compliance == 'hard':
            raise ValueError(f"Invalid date string '{date_str}': no separators found")
        else:
            return date_str


if __name__ == "__main__":
    print(parse_date("1934-03-31T00:00:00Z"))
    print(parse_date("01.05.2002"))
