"""Backbox test file for Utils.py"""
import os
from freezegun import freeze_time
from ntps import pyutils


# Time is frozen at 2019-04-04 04:00:00
@freeze_time("2019-04-04 04:00:00")
def test_get_timestamp():
    """Test get timestamp with the correct format."""

    # Test get_timestamp output
    timestamp = pyutils.get_timestamp()
    assert timestamp == "04:00:00"


def test_check_file_exists():
    """Using this file to check if the file actually exists."""
    curr_file = os.path.realpath('test_utils.py')
    print(curr_file)
    print("HI")
    exists = pyutils.check_file_exists(curr_file)
    print(exists)
    assert True is False
