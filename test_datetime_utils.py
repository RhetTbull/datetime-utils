"""Test datetime_utils.py"""

import datetime

import pytz
import tzlocal

import datetime_utils


def test_get_local_tz_dst():
    dt = datetime.datetime(2020, 9, 1, 21, 10, 00)
    tz = datetime_utils.get_local_tz(dt)
    tz_offset = tzlocal.get_localzone().utcoffset(dt)
    assert tz == datetime.timezone(offset=tz_offset)


def test_get_local_tz():
    dt = datetime.datetime(2020, 12, 1, 21, 10, 00)
    tz = datetime_utils.get_local_tz(dt)
    tz_offset = tzlocal.get_localzone().utcoffset(dt)
    assert tz == datetime.timezone(offset=tz_offset)


def test_datetime_has_tz():
    tz = datetime.timezone(offset=datetime.timedelta(seconds=-28800))
    dt = datetime.datetime(2020, 9, 1, 21, 10, 00, tzinfo=tz)
    assert datetime_utils.datetime_has_tz(dt)


def test_not_datetime_has_tz():
    dt = datetime.datetime(2020, 9, 1, 21, 10, 00)
    assert not datetime_utils.datetime_has_tz(dt)


def test_datetime_tz_to_utc():
    tz = pytz.timezone("US/Pacific")
    dt = tz.localize(datetime.datetime(2020, 12, 1, 22, 6, 0))
    utc = datetime_utils.datetime_tz_to_utc(dt)
    assert utc == datetime.datetime(2020, 12, 2, 6, 6, 0, tzinfo=datetime.timezone.utc)


def test_datetime_tz_to_utc_dst():
    tz = pytz.timezone("US/Pacific")
    dt = tz.localize(datetime.datetime(2020, 5, 1, 22, 6, 0))
    utc = datetime_utils.datetime_tz_to_utc(dt)
    assert utc == datetime.datetime(2020, 5, 2, 5, 6, 0, tzinfo=datetime.timezone.utc)


def test_datetime_remove_tz():
    tz = datetime.timezone(offset=datetime.timedelta(seconds=-25200))
    dt = datetime.datetime(2020, 9, 1, 22, 6, 0, tzinfo=tz)
    dt = datetime_utils.datetime_remove_tz(dt)
    assert dt == datetime.datetime(2020, 9, 1, 22, 6, 0)
    assert not datetime_utils.datetime_has_tz(dt)


def test_datetime_naive_to_utc():
    dt = datetime.datetime(2020, 9, 1, 12, 0, 0)
    utc = datetime_utils.datetime_naive_to_utc(dt)
    assert utc == datetime.datetime(2020, 9, 1, 12, 0, 0, tzinfo=datetime.timezone.utc)


def test_datetime_naive_to_local():
    dt = datetime.datetime(2020, 9, 1, 12, 0, 0)
    tz_offset = tzlocal.get_localzone().utcoffset(dt)
    tz = datetime.timezone(offset=tz_offset)
    local = datetime_utils.datetime_naive_to_local(dt)
    assert local == datetime.datetime(2020, 9, 1, 12, 0, 0, tzinfo=tz)


def test_datetime_utc_to_local():
    utc = datetime.datetime(2020, 9, 1, 19, 0, 0, tzinfo=datetime.timezone.utc)
    dt = datetime_utils.datetime_utc_to_local(utc)
    tz = tzlocal.get_localzone()
    assert dt == datetime.datetime(2020, 9, 1, 12, 0, 0, tzinfo=tz)


def test_datetime_to_new_tz():
    """Test datetime_to_new_tz"""
    tz = datetime.timezone(offset=datetime.timedelta(seconds=-25200))
    dt = datetime.datetime(2021, 10, 1, 0, 30, 0, tzinfo=tz)
    dt_new = datetime_utils.datetime_to_new_tz(dt, 0)
    assert dt_new == datetime.datetime(
        2021, 10, 1, 7, 30, 0, tzinfo=datetime.timezone.utc
    )

    dt_new = datetime_utils.datetime_to_new_tz(dt, 3600)
    tz_new = datetime.timezone(offset=datetime.timedelta(seconds=3600))
    assert dt_new == datetime.datetime(2021, 10, 1, 8, 30, 0, tzinfo=tz_new)


def test_utc_offset_seconds():
    dt_utc = datetime.datetime(2021, 9, 1, 0, 0, 0, 0, tzinfo=datetime.timezone.utc)
    assert datetime_utils.utc_offset_seconds(dt_utc) == 0

    dt_pdt = datetime.datetime(
        2021, 9, 1, 0, 0, 0, 0, tzinfo=datetime.timezone(datetime.timedelta(hours=-7))
    )
    assert datetime_utils.utc_offset_seconds(dt_pdt) == -25200
