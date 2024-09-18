from dataclasses import dataclass
from datetime import datetime
from typing import Tuple, Union, Literal


def _check_invalid_padd_zeros(value: int, places: int = 2, valid_range: Tuple[int, int] = (0, 9999)) -> str:
    """Helper method to preprocess date sub values

    This method is used to aid the Date class initialization by checking if the value is None or outside legal bounds
    and raising an error if it is. Otherwise, it returns the value as a string with the specified number of places,
    padded with zeros.

    :param value: the value to be checked for validity
    :param places: the number of digits the value should be padded to
    :return: the value as a string, padded with zeros
    """
    if value is None:
        raise ValueError("Value cannot be None")
    if valid_range[1] < value or value < valid_range[0]:
        raise ValueError(f"Value cannot be outside the valid range [{valid_range[0]}-{valid_range[1]}]")
    return f'{value:0{places}d}'


@dataclass
class Date:
    """Data class for Date

    This class defines a date object with many useful utility functions, especially for conversions from and to specific
    string formats.

    :ivar year: the year of the date
    :ivar month: the month of the date
    :ivar day: the day of the date
    :ivar hour: the hour of the date
    :ivar minute: the minute of the date
    :ivar second: the second of the date
    """
    year: int
    month: int
    day: int
    hour: int
    minute: int
    second: int

    def __init__(
            self,
            year: int = 0, month: int = 0, day: int = 0,
            hour: int = 0, minute: int = 0, second: int = 0
    ):
        """
        Constructor for Date class

        Initializes the fields and their string representations, padding them with zeros if necessary. If no values are
        provided, the fields are initialized to 0.

        :param year: year 0-9999
        :param month: 1 - 12
        :param day: 1 - 31
        :param hour:
        :param minute:
        :param second:
        """
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
        self.year_str = _check_invalid_padd_zeros(year)
        self.month_str = _check_invalid_padd_zeros(month, valid_range=(0, 12))
        self.day_str = _check_invalid_padd_zeros(day, valid_range=(0, 31))
        self._check_invalid_day_month_combinations()
        self.hour_str = _check_invalid_padd_zeros(hour, valid_range=(0, 23))
        self.minute_str = _check_invalid_padd_zeros(minute, valid_range=(0, 59))
        self.second_str = _check_invalid_padd_zeros(second, valid_range=(0, 59))

    def _check_invalid_day_month_combinations(self):
        # check month specific day month combinations
        if self.month == 2:
            if self.year % 4 == 0 and self.day > 29:  # leap year
                raise ValueError(f"Invalid day for February in a leap year: {self.day}.")
            elif self.day > 28:
                raise ValueError(f"Invalid day for February in a non-leap year: {self.day}.")
        elif self.month in [1, 3, 5, 7, 8, 10, 12]:
            if self.day > 31:
                raise ValueError(f"Invalid day for month {self.month}: {self.day}.")
        elif self.month in [4, 6, 9, 11]:
            if self.day > 30:
                raise ValueError(f"Invalid day for month {self.month}: {self.day}.")

    def iso_8601_datestring(self) -> str:
        """
        Returns the date in ISO 8601 format

        Example: “2021-06-02T16:52:15Z”
        Format: “{year}-{month}-{day}T{hour}:{min}:{sec}[.{frac_sec}]Z”
        Definition: The format for this is “{year}-{month}-{day}T{hour}:{min}:{sec}[.{frac_sec}]Z” where {year} is
                    always expressed using four digits while {month}, {day}, {hour}, {min}, and {sec} are zero-padded to
                    two digits each. The fractional seconds, which can go up to 9 digits (i.e. up to 1 nanosecond
                    resolution), are optional. The “Z” suffix indicates the timezone (“UTC”); the timezone is required.
        """
        return (self.year_str + "-" + self.month_str + "-" + self.day_str + "T"
                + self.hour_str + ":" + self.minute_str + ":" + self.second_str + "Z")

    def formatted_string(self, fmt: str) -> str:
        """
        Returns the date in the specified format

        :param fmt: the format as a string to return the date in
        :return: the date in the specified format
        """
        # days, months, and years
        if fmt.lower() == "yyyy-mm-dd":
            return f"{self.year_str}-{self.month_str}-{self.day_str}"
        elif fmt.lower() == "yyyy/mm/dd":
            return f"{self.year_str}/{self.month_str}/{self.day_str}"
        elif fmt.lower() == "mm/dd/yyyy":
            return f"{self.month_str}/{self.day_str}/{self.year_str}"
        elif fmt.lower() == "mm-dd-yyyy":
            return f"{self.month_str}-{self.day_str}-{self.year_str}"
        elif fmt.lower() == "dd/mm/yyyy":
            return f"{self.day_str}/{self.month_str}/{self.year_str}"
        elif fmt.lower() == "dd.mm.yyyy":
            return f"{self.day_str}.{self.month_str}.{self.year_str}"
        elif fmt.lower() == "dd-mm-yyyy":
            return f"{self.day_str}-{self.month_str}-{self.year_str}"
        # months and years
        elif fmt.lower() == "yyyy-mm":
            return f"{self.year_str}-{self.month_str}"
        elif fmt.lower() == "yyyy/mm":
            return f"{self.year_str}/{self.month_str}"
        elif fmt.lower() == "yyyy.mm":
            return f"{self.year_str}.{self.month_str}"
        elif fmt.lower() == "mm.yyyy":
            return f"{self.month_str}.{self.year_str}"
        elif fmt.lower() == "mm-yyyy":
            return f"{self.month_str}-{self.year_str}"
        elif fmt.lower() == "mm/yyyy":
            return f"{self.month_str}/{self.year_str}"
        # just years
        elif fmt.lower() == "yyyy":
            return f"{self.year_str}"
        # hours, minutes, seconds, years, months, days
        elif fmt.lower() == "yyyy-mm-dd hh:mm:ss":
            return (f"{self.year_str}-{self.month_str}-{self.day_str} "
                    f"{self.hour_str}:{self.minute_str}:{self.second_str}")
        elif fmt.lower() == "iso" or fmt.lower() == "iso8601":
            return self.iso_8601_datestring()
        else:
            # Use strftime for standard formats
            try:
                dt = datetime(
                    year=self.year,
                    month=self.month,
                    day=self.day,
                    hour=self.hour,
                    minute=self.minute,
                    second=self.second
                )
                return dt.strftime(fmt)
            except ValueError as e:
                raise ValueError(f"Invalid format string '{fmt}': {e}")

    def __repr__(self):
        return self.iso_8601_datestring()

    def __str__(self):
        return self.iso_8601_datestring()

    @staticmethod
    def from_datetime(dt: datetime) -> 'Date':
        """
        Create a Date object from a datetime object

        :param dt: the datetime object to create the Date object from
        :return: the Date object created from the datetime object
        """
        return Date(
            year=dt.year,
            month=dt.month,
            day=dt.day,
            hour=dt.hour,
            minute=dt.minute,
            second=dt.second
        )

    @staticmethod
    def from_iso_8601(iso_8601: str) -> Union['Date', None]:
        """
        Create a Date object from an ISO 8601 formatted string

        :param iso_8601: the ISO 8601 formatted string to create the Date object from
        :return: the Date object created from the ISO 8601 formatted string
        """
        try:
            date, time = iso_8601[:-1].split('T')
            year, month, day = date.split('-')
            hour, minute, second = time.split(':')
            return Date(
                year=int(year),
                month=int(month),
                day=int(day),
                hour=int(hour),
                minute=int(minute),
                second=int(second)
            )
        except:
            return None

    @staticmethod
    def parse_date(
            date_str: str,
            default_first: Literal["day", "month"] = "day",
            compliance: Literal['soft', 'hard'] = 'soft',
    ) -> 'Date':
        """Parse a date string into a Date object

        There is a lot of variation in how dates are formatted, and this function attempts to handle as many of them as
        possible. The function will first attempt to parse the date string as an ISO 8601 formatted string. If that fails,
        it will attempt to parse the date string as a date string with separators.

        In this process it is sometimes
        unknowable whether 01-02-2024 is January 2nd or February 1st, so the function will use the `default_first` parameter
        to determine this. If the `default_first` parameter is set to "day", the function will assume that the day comes
        first, and if it is set to "month", the function will assume that the month comes first. If the `default_first`

        :param date_str: the date string to parse
        :param default_first: the default unit to use if it is unclear which unit comes first between day and month
        :param compliance: the compliance level of the parser
        :return: the Date object created from the date string
        """
        from phenopacket_mapper.utils.parsing import parse_date
        return parse_date(
            date_str=date_str,
            default_first=default_first,
            compliance=compliance
        )
