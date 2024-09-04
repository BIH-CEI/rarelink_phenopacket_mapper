from dataclasses import dataclass
from datetime import datetime


def _preprocess(value: int, places: int = 2) -> str:
    if value is None:
        raise ValueError("Value cannot be None")
    if value < 0:
        raise ValueError("Value cannot be negative")
    return f'{value:0{places}d}'


@dataclass(slots=True)
class Date:
    """
    Data class for Date
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
        self.year = year
        self.year_str = _preprocess(year, 4)
        self.month = month
        self.month_str = _preprocess(month)
        self.day = day
        self.day_str = _preprocess(day)
        self.hour = hour
        self.hour_str = _preprocess(hour)
        self.minute = minute
        self.minute_str = _preprocess(minute)
        self.second = second
        self.second_str = _preprocess(second)

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
        """
        if fmt.lower() == "yyyy-mm-dd":
            return f"{self.year_str}-{self.month_str}-{self.day_str}"
        elif fmt.lower() == "yyyy-mm":
            return f"{self.year_str}-{self.month_str}"
        elif fmt.lower() == "yyyy":
            return f"{self.year_str}"
        elif fmt.lower() == "yyyy-mm-dd hh:mm:ss":
            return (f"{self.year_str}-{self.month_str}-{self.day_str} "
                    f"{self.hour_str}:{self.minute_str}:{self.second_str}")

    def __repr__(self):
        return self.iso_8601_datestring()

    def __str__(self):
        return self.iso_8601_datestring()

    @staticmethod
    def from_datetime(dt: datetime) -> 'Date':
        """
        Create a Date object from a datetime object
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
    def from_iso_8601(iso_8601: str) -> 'Date':
        """
        Create a Date object from an ISO 8601 formatted string
        """
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
