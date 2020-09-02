# datetime_utils

## What is datetime_utils
A handful of small utility methods I find useful for dealing with [datetime.datetime](https://docs.python.org/3/library/datetime.html#module-datetime) objects and timezones.

## Installation

Just copy datetime_utils.py to your source tree then

`import datetime_utils`

## Synopsis

```python
>>> import datetime_utils
>>> import datetime
>>> dt = datetime.datetime(2019,12,1)
>>> datetime_utils.get_local_tz(dt)
datetime.timezone(datetime.timedelta(days=-1, seconds=57600), 'PST')
>>> datetime_utils.datetime_has_tz(dt)
False
>>> dt = datetime_utils.datetime_naive_to_local(dt)
>>> dt
datetime.datetime(2019, 12, 1, 0, 0, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=57600), 'PST'))
>>> datetime_utils.datetime_has_tz(dt)
True
>>> utc = datetime_utils.datetime_tz_to_utc(dt)
>>> utc
datetime.datetime(2019, 12, 1, 8, 0, tzinfo=datetime.timezone.utc)
>>> dt = datetime_utils.datetime_remove_tz(dt)
>>> dt
datetime.datetime(2019, 12, 1, 0, 0)
>>> utc = datetime_utils.datetime_naive_to_utc(dt)
>>> utc
datetime.datetime(2019, 12, 1, 0, 0, tzinfo=datetime.timezone.utc)
>>> local = datetime_utils.datetime_utc_to_local(utc)
>>> local
datetime.datetime(2019, 11, 30, 16, 0, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=57600), 'PST'))
>>> 
```
