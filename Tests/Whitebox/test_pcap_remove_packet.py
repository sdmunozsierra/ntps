"""Whitebox test file for Utils.py"""
import os
from Packet.pcap import PCAP
from pyutils import get_timestamp


def test_remove_packet_from_pcap():
    """Tests removing a packet from pcap file."""
    curr_dir = os.path.dirname(os.path.abspath(__file__))  # Whitebox
    # Create a PCAP object, load PCAP file
    pcap = PCAP("test1", get_timestamp())
    pcap.load(f"{curr_dir}/test1.pcap")

    # Check that PCAP file is not empty
    assert len(pcap.packets) != 0

    # Copy first packet to be used as the packet to be removed
    rm_packet = pcap.packets[0]
    print("printing extracted packet")
    print(rm_packet)
    print(rm_packet.name)

    # Assert that the extracted packet is on the pcap
    assert pcap.packetExists(rm_packet) is True

    # Remove the packet with Assert
    assert pcap.removePacket(rm_packet.name) is True

    # Assert that packet is not in the pcap anymore by using packetExists
    print("Packet in pcap?")
    print(pcap.packetExists(rm_packet))
    assert pcap.packetExists(rm_packet) is False
