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
    curr_file = os.path.dirname(os.path.abspath(__file__))
    curr_file = "{}{}".format(curr_file, '/test_utils.py')
    exists = pyutils.check_file_exists(curr_file)
    assert exists is True
