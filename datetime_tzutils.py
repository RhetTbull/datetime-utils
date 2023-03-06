""" datetime.datetime helper functions for converting to/from UTC and other datetime manipulations"""

__version__ = "1.0.0"

import datetime

__all__ = [
    "datetime_has_tz",
    "datetime_naive_to_local",
    "datetime_naive_to_utc",
    "datetime_remove_tz",
    "datetime_to_new_tz",
    "datetime_tz_to_utc",
    "datetime_utc_to_local",
    "get_local_tz",
    "utc_offset_seconds",
]


def get_local_tz(dt: datetime.datetime) -> datetime.tzinfo:
    """Return local timezone as datetime.timezone tzinfo for naive datetime dt

    Args:
        dt: datetime.datetime object

    Returns:
        local timezone for dt as datetime.timezone

    Raises:
        TypeError if dt is not datetime.datetime object
    """

    if not isinstance(dt, datetime.datetime):
        raise TypeError(f"dt must be type datetime.datetime, not {type(dt)}")

    if datetime_has_tz(dt):
        raise ValueError("dt must be naive datetime.datetime object")
    return dt.astimezone().tzinfo


def datetime_has_tz(dt: datetime.datetime) -> bool:
    """Return True if datetime dt has tzinfo else False

    Args:
        dt: datetime.datetime

    Returns:
        True if dt is timezone aware, else False

    Raises:
        TypeError if dt is not a datetime.datetime object
    """

    if not isinstance(dt, datetime.datetime):
        raise TypeError(f"dt must be type datetime.datetime, not {type(dt)}")

    return dt.tzinfo is not None and dt.tzinfo.utcoffset(dt) is not None


def datetime_tz_to_utc(dt: datetime.datetime) -> datetime.datetime:
    """Convert datetime.datetime object with timezone to UTC timezone

    Args:
        dt: datetime.datetime object

    Returns:
        datetime.datetime in UTC timezone

    Raises:
        TypeError if dt is not datetime.datetime object
        ValueError if dt does not have timezone information
    """

    if not isinstance(dt, datetime.datetime):
        raise TypeError(f"dt must be type datetime.datetime, not {type(dt)}")

    if dt.tzinfo is not None and dt.tzinfo.utcoffset(dt) is not None:
        return dt.astimezone(tz=datetime.timezone.utc)
    else:
        raise ValueError("dt does not have timezone info")


def datetime_remove_tz(dt: datetime.datetime) -> datetime.datetime:
    """Remove timezone from a datetime.datetime object

    Args:
        dt: datetime.datetime object with tzinfo

    Returns:
        dt without any timezone info (naive datetime object)

    Raises:
        TypeError if dt is not a datetime.datetime object
    """

    if not isinstance(dt, datetime.datetime):
        raise TypeError(f"dt must be type datetime.datetime, not {type(dt)}")

    return dt.replace(tzinfo=None)


def datetime_naive_to_utc(dt: datetime.datetime) -> datetime.datetime:
    """Convert naive (timezone unaware) datetime.datetime
        to aware timezone in UTC timezone

    Args:
        dt: datetime.datetime without timezone

    Returns:
        datetime.datetime with UTC timezone

    Raises:
        TypeError if dt is not a datetime.datetime object
        ValueError if dt is not a naive/timezone unaware object
    """

    if not isinstance(dt, datetime.datetime):
        raise TypeError(f"dt must be type datetime.datetime, not {type(dt)}")

    if dt.tzinfo is not None and dt.tzinfo.utcoffset(dt) is not None:
        # has timezone info
        raise ValueError(
            "dt must be naive/timezone unaware: "
            f"{dt} has tzinfo {dt.tzinfo} and offset {dt.tzinfo.utcoffset(dt)}"
        )

    return dt.replace(tzinfo=datetime.timezone.utc)


def datetime_naive_to_local(dt: datetime.datetime) -> datetime.datetime:
    """Convert naive (timezone unaware) datetime.datetime
        to aware timezone in local timezone

    Args:
        dt: datetime.datetime without timezone

    Returns:
        datetime.datetime with local timezone

    Raises:
        TypeError if dt is not a datetime.datetime object
        ValueError if dt is not a naive/timezone unaware object
    """

    if not isinstance(dt, datetime.datetime):
        raise TypeError(f"dt must be type datetime.datetime, not {type(dt)}")

    if dt.tzinfo is not None and dt.tzinfo.utcoffset(dt) is not None:
        # has timezone info
        raise ValueError(
            "dt must be naive/timezone unaware: "
            f"{dt} has tzinfo {dt.tzinfo} and offset {dt.tzinfo.utcoffset(dt)}"
        )

    return dt.replace(tzinfo=get_local_tz(dt))


def datetime_utc_to_local(dt: datetime.datetime) -> datetime.datetime:
    """Convert datetime.datetime object in UTC timezone to local timezone

    Args:
        dt: datetime.datetime object

    Returns:
        datetime.datetime in local timezone

    Raises:
        TypeError if dt is not a datetime.datetime object
        ValueError if dt is not in UTC timezone
    """

    if not isinstance(dt, datetime.datetime):
        raise TypeError(f"dt must be type datetime.datetime, not {type(dt)}")

    if dt.tzinfo is not datetime.timezone.utc:
        raise ValueError(f"{dt} must be in UTC timezone: timezone = {dt.tzinfo}")

    return dt.astimezone(tz=None)


def datetime_to_new_tz(dt: datetime.datetime, offset) -> datetime.datetime:
    """Convert datetime.datetime object from current timezone to new timezone with offset of seconds from UTC

    Args:
        dt: datetime.datetime object

    Returns:
        datetime.datetime object in new timezone

    Raises:
        TypeError if dt is not a datetime.datetime object
        ValueError if dt is not timezone aware
    """

    if not isinstance(dt, datetime.datetime):
        raise TypeError(f"dt must be type datetime.datetime, not {type(dt)}")

    if not datetime_has_tz(dt):
        raise ValueError("dt must be timezone aware")

    time_delta = datetime.timedelta(seconds=offset)
    tz = datetime.timezone(time_delta)
    return dt.astimezone(tz=tz)


def utc_offset_seconds(dt: datetime.datetime) -> int:
    """Return offset in seconds from UTC for timezone aware datetime.datetime object

    Args:
        dt: datetime.datetime object

    Returns:
        offset in seconds from UTC

    Raises:
        ValueError if dt does not have timezone information
        TypeError if dt is not a datetime.datetime object
    """

    if not isinstance(dt, datetime.datetime):
        raise TypeError(f"dt must be type datetime.datetime, not {type(dt)}")

    if dt.tzinfo is not None and dt.tzinfo.utcoffset(dt) is not None:
        return dt.tzinfo.utcoffset(dt).total_seconds()
    else:
        raise ValueError("dt does not have timezone info")
