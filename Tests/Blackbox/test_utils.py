"""Backbox test file for Utils.py"""
from freezegun import freeze_time
from ntps import pyutils


# Time is frozen at 2019-04-04 04:00:00
@freeze_time("2019-04-04 04:00:00")
def test_get_timestamp():
    """Test get timestamp with the correct format."""

    # Test get_timestamp output
    timestamp = pyutils.get_timestamp()
    assert timestamp == "04:00:00"
