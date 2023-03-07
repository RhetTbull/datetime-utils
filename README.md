# datetime_tzutils

## What is datetime_tzutils

A handful of small utility methods I find useful for dealing with
[datetime.datetime](https://docs.python.org/3/library/datetime.html#module-datetime)
objects and timezones. Some of these are just a couple of lines but they're easy to
get wrong so I find it useful to package them into a tested module. I also find it
makes code more readable and less repetitive.

datetime_tzutils is a pure Python module with no dependencies.

Includes:

- `datetime_has_tz(dt: datetime.datetime) -> bool`: returns True if the datetime has a timezone
- `datetime_naive_to_local(dt: datetime.datetime) -> datetime.datetime`: converts a naive datetime to the local timezone
- `datetime_naive_to_utc(dt: datetime.datetime) -> datetime.datetime`: converts a naive datetime to UTC
- `datetime_remove_tz(dt: datetime.datetime) -> datetime.datetime:`: removes the timezone from a datetime
- `datetime_to_new_tz(dt: datetime.datetime, offset) -> datetime.datetime`: converts a datetime to a new timezone
- `datetime_tz_to_utc(dt: datetime.datetime) -> datetime.datetime`: converts a datetime with a timezone to UTC
- `datetime_utc_to_local(dt: datetime.datetime) -> datetime.datetime`: converts a UTC datetime to the local timezone
- `get_local_tz(dt: datetime.datetime) -> datetime.tzinfo`: returns the local timezone for a given datetime
- `utc_offset_seconds(dt: datetime.datetime) -> int`: returns the UTC offset in seconds for a given datetime

## Installation

`pip install datetime_tzutils`

## Synopsis

```python
>>> import datetime_tzutils
>>> import datetime
>>> dt = datetime.datetime(2019,12,1)
>>> datetime_tzutils.get_local_tz(dt)
datetime.timezone(datetime.timedelta(days=-1, seconds=57600), 'PST')
>>> datetime_tzutils.datetime_has_tz(dt)
False
>>> dt = datetime_tzutils.datetime_naive_to_local(dt)
>>> dt
datetime.datetime(2019, 12, 1, 0, 0, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=57600), 'PST'))
>>> datetime_tzutils.datetime_has_tz(dt)
True
>>> utc = datetime_tzutils.datetime_tz_to_utc(dt)
>>> utc
datetime.datetime(2019, 12, 1, 8, 0, tzinfo=datetime.timezone.utc)
>>> dt = datetime_tzutils.datetime_remove_tz(dt)
>>> dt
datetime.datetime(2019, 12, 1, 0, 0)
>>> utc = datetime_tzutils.datetime_naive_to_utc(dt)
>>> utc
datetime.datetime(2019, 12, 1, 0, 0, tzinfo=datetime.timezone.utc)
>>> local = datetime_tzutils.datetime_utc_to_local(utc)
>>> local
datetime.datetime(2019, 11, 30, 16, 0, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=57600), 'PST'))
>>> 
```

## Source Code

The source code is available on [GitHub](https://github.com/RhetTbull/datetime-utils)

## Testing

datetime_tzutils has been tested with Python 3.9, 3.10, and 3.11 on Linux, macOS, and Windows.

100% test coverage with `pytest`:

- `pip install -r requirements_dev.txt`
- `python -m pytest --cov=datetime_tzutils --cov-report=term-missing`

## Contributing

Contributions are welcome. Please open an issue or submit a pull request.

The tests are written with pytest and require a couple of extra packages. Install them with:

`pip install -r requirements_dev.txt`

## License

MIT License
