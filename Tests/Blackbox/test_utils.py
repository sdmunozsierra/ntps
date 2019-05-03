"""Backbox test file for Utils.py"""
# import sys
# sys.path.append('..')
# import sys
# sys.path.append('../../')
from freezegun import freeze_time
from ntps import Utils


@freeze_time("2019-04-04 04:00:00")
def test_get_timestamp():
    """Test get timestamp with the correct format."""
    # Time is frozen at 2019-04-04 04:00:00

    # Test get_timestamp output
    timestamp = Utils.get_timestamp()
    assert timestamp == "04:00:00"
