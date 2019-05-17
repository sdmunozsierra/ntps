"""Backbox test file for Utils.py"""
import os
from freezegun import freeze_time
from scapy.packet import Packet
from ntps import pyutils


# Time is frozen at 2019-04-04 04:00:00
@freeze_time("2019-04-04 04:00:00")
def test_get_timestamp():
    """Test get timestamp with the correct format."""

    # Test get_timestamp output
    timestamp = pyutils.get_timestamp()
    assert timestamp == "04:00:00"


def test_extract_hook():
    """Test extract hook name from a path."""
    test_path = "blah/blah/blah/hook_name.py"
    hook_name = pyutils.extract_hook_name(test_path)
    assert hook_name == "hook_name"


def test_check_file_exists():
    """Using this file to check if the file actually exists."""
    curr_file = os.path.dirname(os.path.abspath(__file__))
    curr_file = "{}{}".format(curr_file, '/test_utils.py')
    exists = pyutils.check_file_exists(curr_file)
    assert exists is True


def test_load_packet():
    """Check that a binary packet is transformed into a string."""
    bin_pkt = 'E\x00\x00\x14\x00\x01\x00\x00@\x00|\xe7\x7f\x00\x00\x01\x7f\x00\x00\x01'
    expected_pkt = str(b'E\x00\x00\x14\x00\x01\x00\x00@\x00|\xc3\xa7\x7f\x00\x00\x01\x7f\x00\x00\x01')
    transformed_pkt = pyutils.load_packet(bin_pkt)
    assert transformed_pkt == expected_pkt


def test_unload_packet():
    """Check that a string packet is transformed into a Packet."""
    string_pkt = str(b'E\x00\x00\x14\x00\x01\x00\x00@\x00|\xc3\xa7\x7f\x00\x00\x01\x7f\x00\x00\x01')
    expected_pkt = Packet(string_pkt)
    transformed_pkt = pyutils.unload_packet(string_pkt)
    assert transformed_pkt == expected_pkt
