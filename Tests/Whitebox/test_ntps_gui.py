"""Whitebox test file for Utils.py"""
from ntps.App import ntps


def test_get_timestamp():
    """Test get timestamp with the correct format."""
    gui = ntps.Ui_Main_Dialog()
    assert gui is None
