# datetime_tzutils

## What is datetime_tzutils

A handful of small utility methods I find useful for dealing with [datetime.datetime](https://docs.python.org/3/library/datetime.html#module-datetime) objects and timezones. Some of these are really just one-liners but they're easy to get wrong so I find it useful to package them into a tested module.

Includes:

- datetime_has_tz()
- datetime_naive_to_local()
- datetime_naive_to_utc()
- datetime_remove_tz()
- datetime_to_new_tz()
- datetime_tz_to_utc()
- datetime_utc_to_local()
- get_local_tz()
- utc_offset_seconds()

## Installation

Just copy datetime_tzutils.py to your source tree then

`import datetime_tzutils`

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

## Testing

100% test coverage with `pytest`:

- `pip install -r requirements_dev.txt`
- `python -m pytest`
