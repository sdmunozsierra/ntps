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
    assert Utils.get_timestamp() is None


    # Test date without time
    # start_date = "01-23-2019"
    # expected = datetime.datetime(2019, 1, 23, 0, 0)
    # assert pl.change_date(start_date) == expected
    #
    # # Test date wit time
    # start_date_time = "01-23-2019:12:55:00"
    # expected = datetime.datetime(2019, 1, 23, 12, 55)
    # assert pl.change_date(start_date_time) == expected
    #
    # # Test unknown date format
    # start_date_unknown = "Unknown format"
    # assert pl.change_date(start_date_unknown) is None
