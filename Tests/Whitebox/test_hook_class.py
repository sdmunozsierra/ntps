"""Whitebox test file for hook.py"""
from ntps.Hook import hook
from pyutils import check_file_exists
from scapy.all import *
import os
from io import BytesIO
import pickle
from binascii import hexlify


def test_run_hook():
    """Test hook class."""
    test_hook = hook.TestHook("dummy", "description", True)

    # Check that there is a hook to be ran
    curr_dir = os.path.dirname(os.path.abspath(__file__))  # Whitebox
    curr_file = os.path.dirname(curr_dir)  # Tests
    curr_file = os.path.dirname(curr_file)  # ntps
    sample_hook_path = "{}{}".format(curr_file, "/Hooks/DNSsport.py")
    assert check_file_exists(sample_hook_path) is True

    # Check if pcap path exists
    sample_pcap_path = "{}{}".format(curr_dir, "/test1.pcap")
    assert check_file_exists(sample_pcap_path) is True

    # Get sample packet to be send through hook
    pkt = 'E\x00\x00\x14\x00\x01\x00\x00@\x00|\xe7\x7f\x00\x00\x01\x7f\x00\x00\x01'
    # pkt = pkt.encode("utf-8")  # Tried
    # pkt = "{}".format(pkt)
    # pkt = str(pkt)
    # pkt = str(pkt).encode()
    # pkt = pkt.encode()
    # pkt = str().encode(pkt)
    # pkt = bytes(bytearray(pkt))
    # pkt = BytesIO(pkt)
    # pkt = BytesIO(pkt.encode())
    # test run hook
    # pkt = pickle.dumps(pkt)
    # pkt = hexlify(str(pkt))
    # pkt = hexlify(pkt).encode()
    # pkt = IP(pkt)
    pkt = Packet(pkt)
    pkt = str(pkt.payload)


    ## SEND PCAP IS ERROR
    # pcap = rdpcap(sample_pcap_path)
    # test_hook.run(sample_hook_path, pcap)

    ## Send pcap sample path 'works' but complains that a String
    # test_hook.run(sample_hook_path, sample_pcap_path)

    test_hook.run(sample_hook_path, pkt)

    assert True is False
