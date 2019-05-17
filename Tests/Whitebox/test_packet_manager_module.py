"""Whitebox test file for Utils.py"""
from ntps.Packet.packet_manager import PacketManager


def test_get_timestamp():
    """Test get timestamp with the correct format."""
    pacman = PacketManager()
