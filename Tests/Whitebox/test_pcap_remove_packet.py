"""Whitebox test file for Utils.py"""
from ntps.Packet import packet


def test_get_timestamp():
    """Test get timestamp with the correct format."""
    a_packet = packet.TestPacket("packet1")
    assert a_packet is not None
    assert a_packet.getName() == "packet1"
    assert a_packet.name == "packet1"
