"""Test datetime_tzutils.py"""

import datetime
import pytest
import pytz
import tzlocal

import datetime_tzutils


def test_get_local_tz():
    dt = datetime.datetime(2020, 12, 1, 21, 10, 00)
    tz = datetime_tzutils.get_local_tz(dt)
    tz_offset = tzlocal.get_localzone().utcoffset(dt)
    assert tz == datetime.timezone(offset=tz_offset)


def test_get_local_tz_dst():
    dt = datetime.datetime(2020, 9, 1, 21, 10, 00)
    tz = datetime_tzutils.get_local_tz(dt)
    tz_offset = tzlocal.get_localzone().utcoffset(dt)
    assert tz == datetime.timezone(offset=tz_offset)


def test_get_local_tz_error():
    """Test get_local_tz raises ValueError if dt is timezone aware"""
    tz = datetime.timezone(offset=datetime.timedelta(seconds=-28800))
    dt = datetime.datetime(2020, 9, 1, 21, 10, 00, tzinfo=tz)
    with pytest.raises(ValueError):
        datetime_tzutils.get_local_tz(dt)


def test_datetime_has_tz():
    tz = datetime.timezone(offset=datetime.timedelta(seconds=-28800))
    dt = datetime.datetime(2020, 9, 1, 21, 10, 00, tzinfo=tz)
    assert datetime_tzutils.datetime_has_tz(dt)


def test_not_datetime_has_tz():
    dt = datetime.datetime(2020, 9, 1, 21, 10, 00)
    assert not datetime_tzutils.datetime_has_tz(dt)


def test_datetime_tz_to_utc():
    tz = pytz.timezone("US/Pacific")
    dt = tz.localize(datetime.datetime(2020, 12, 1, 22, 6, 0))
    utc = datetime_tzutils.datetime_tz_to_utc(dt)
    assert utc == datetime.datetime(2020, 12, 2, 6, 6, 0, tzinfo=datetime.timezone.utc)


def test_datetime_tz_to_utc_dst():
    tz = pytz.timezone("US/Pacific")
    dt = tz.localize(datetime.datetime(2020, 5, 1, 22, 6, 0))
    utc = datetime_tzutils.datetime_tz_to_utc(dt)
    assert utc == datetime.datetime(2020, 5, 2, 5, 6, 0, tzinfo=datetime.timezone.utc)


def test_datetime_remove_tz():
    tz = datetime.timezone(offset=datetime.timedelta(seconds=-25200))
    dt = datetime.datetime(2020, 9, 1, 22, 6, 0, tzinfo=tz)
    dt = datetime_tzutils.datetime_remove_tz(dt)
    assert dt == datetime.datetime(2020, 9, 1, 22, 6, 0)
    assert not datetime_tzutils.datetime_has_tz(dt)


def test_datetime_naive_to_utc():
    dt = datetime.datetime(2020, 9, 1, 12, 0, 0)
    utc = datetime_tzutils.datetime_naive_to_utc(dt)
    assert utc == datetime.datetime(2020, 9, 1, 12, 0, 0, tzinfo=datetime.timezone.utc)


def test_datetime_naive_to_local():
    dt = datetime.datetime(2020, 9, 1, 12, 0, 0)
    tz_offset = tzlocal.get_localzone().utcoffset(dt)
    tz = datetime.timezone(offset=tz_offset)
    local = datetime_tzutils.datetime_naive_to_local(dt)
    assert local == datetime.datetime(2020, 9, 1, 12, 0, 0, tzinfo=tz)


def test_datetime_utc_to_local():
    utc = datetime.datetime(2020, 9, 1, 19, 0, 0, tzinfo=datetime.timezone.utc)
    dt = datetime_tzutils.datetime_utc_to_local(utc)
    tz = tzlocal.get_localzone()
    assert dt == datetime.datetime(2020, 9, 1, 12, 0, 0, tzinfo=tz)


def test_datetime_utc_to_local_error_not_utc():
    """Assert ValueError is raised if dt is not UTC timezone"""
    utc = datetime.datetime(
        2020,
        9,
        1,
        19,
        0,
        0,
        tzinfo=datetime.timezone(offset=datetime.timedelta(seconds=-25200)),
    )
    with pytest.raises(ValueError):
        datetime_tzutils.datetime_utc_to_local(utc)


def test_datetime_to_new_tz():
    """Test datetime_to_new_tz"""
    tz = datetime.timezone(offset=datetime.timedelta(seconds=-25200))
    dt = datetime.datetime(2021, 10, 1, 0, 30, 0, tzinfo=tz)
    dt_new = datetime_tzutils.datetime_to_new_tz(dt, 0)
    assert dt_new == datetime.datetime(
        2021, 10, 1, 7, 30, 0, tzinfo=datetime.timezone.utc
    )

    dt_new = datetime_tzutils.datetime_to_new_tz(dt, 3600)
    tz_new = datetime.timezone(offset=datetime.timedelta(seconds=3600))
    assert dt_new == datetime.datetime(2021, 10, 1, 8, 30, 0, tzinfo=tz_new)


def test_datetime_to_new_tz_value_error():
    """Test datetime_to_new_tz with invalid dt"""
    dt = datetime.datetime(2021, 10, 1, 0, 30, 0)
    with pytest.raises(ValueError):
        dt_new = datetime_tzutils.datetime_to_new_tz(dt, 0)


def test_datetime_to_new_tz_type_error():
    """Test datetime_to_new_tz with invalid dt"""
    with pytest.raises(TypeError):
        dt_new = datetime_tzutils.datetime_to_new_tz("test", 0)


def test_utc_offset_seconds():
    dt_utc = datetime.datetime(2021, 9, 1, 0, 0, 0, 0, tzinfo=datetime.timezone.utc)
    assert datetime_tzutils.utc_offset_seconds(dt_utc) == 0

    dt_pdt = datetime.datetime(
        2021, 9, 1, 0, 0, 0, 0, tzinfo=datetime.timezone(datetime.timedelta(hours=-7))
    )
    assert datetime_tzutils.utc_offset_seconds(dt_pdt) == -25200


@pytest.mark.parametrize(
    "method",
    [
        "datetime_has_tz",
        "datetime_naive_to_local",
        "datetime_naive_to_utc",
        "datetime_remove_tz",
        "datetime_tz_to_utc",
        "datetime_utc_to_local",
        "get_local_tz",
        "utc_offset_seconds",
    ],
)
def test_type_error(method):
    """Test TypeError is raised if method is not a datetime method"""
    with pytest.raises(TypeError):
        getattr(datetime_tzutils, method)("test")


@pytest.mark.parametrize(
    "method",
    ["datetime_tz_to_utc", "utc_offset_seconds"],
)
def test_value_error_naive(method):
    """Test ValueError raised if naive datetime passed to method"""
    with pytest.raises(ValueError):
        getattr(datetime_tzutils, method)(datetime.datetime(2021, 9, 1, 0, 0, 0, 0))


@pytest.mark.parametrize(
    "method",
    ["datetime_naive_to_local", "datetime_naive_to_utc"],
)
def test_value_error_not_naive(method):
    """Test ValueError raised if timezone aware datetime passed to method"""
    with pytest.raises(ValueError):
        getattr(datetime_tzutils, method)(
            datetime.datetime(2021, 9, 1, 0, 0, 0, 0, tzinfo=datetime.timezone.utc)
        )
