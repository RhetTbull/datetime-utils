import pytest

def test_get_local_tz():
    import datetime
    import os

    import datetime_utils
    
    os.environ["TZ"] = "US/Pacific"

    dt = datetime.datetime(2020,9,1,21,10,00)
    tz = datetime_utils.get_local_tz(dt)
    assert tz == datetime.timezone(offset=datetime.timedelta(seconds=-25200))

    dt = datetime.datetime(2020,12,1,21,10,00)
    tz = datetime_utils.get_local_tz(dt)
    assert tz == datetime.timezone(offset=datetime.timedelta(seconds=-28800))



