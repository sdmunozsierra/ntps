"""Whitebox test file for hook.py"""
import os
import sys
from ntps.Hook import hook
from ntps.pyutils import check_file_exists, load_packet
from scapy.packet import Packet
import pickle


def test_run_hook():
    """Test hook class."""
    test_hook = hook.TestHook("dummy", "description", True)

    # Check that there is a hook to be ran
    curr_dir = os.path.dirname(os.path.abspath(__file__))  # Whitebox
    curr_file = os.path.dirname(curr_dir)  # Tests
    curr_file = os.path.dirname(curr_file)  # ntps
    sample_hook_path = "{}{}".format(curr_file, "/Hooks/DNSsport.py")
    assert check_file_exists(sample_hook_path) is True

    orig_pkt = 'E\x00\x00\x14\x00\x01\x00\x00@\x00|\xe7\x7f\x00\x00\x01\x7f\x00\x00\x01'
    pkt = load_packet(orig_pkt)
    print("Original packet: {}".format(pkt))

    output = test_hook.run(sample_hook_path, pkt)

    print("Raw output: {}".format(output))
    print()
    # print("decoded output 1: {}".format(output.decode("utf-8").strip()))
    # print()

    # Translate
    no_escapes = output.decode('unicode_escape').strip()
    # pkt_decoded = pkt_decoded.translate()
    # no_escapes = no_escapes[3:]
    # no_escapes = no_escapes[:-1]
    print("decoded output 1.5: {}".format(no_escapes))

    assert orig_pkt == orig_pkt
    assert orig_pkt == str(no_escapes)

    # pkt_decoded = output.decode("utf-8").strip()
    # pkt_decoded = str(pkt_decoded)
    # pkt_decoded = pkt_decoded.decode("utf-8")
    # pkt_decoded = pkt_decoded[3:]
    # pkt_decoded = pkt_decoded[:-1]
    # print("decoded output 2: {}".format(pkt_decoded))
    # print()

    # pkt_decoded = Packet(pkt_decoded)
    # print("Retreived packet: {}".format(str(pkt_decoded.payload)))

    print(type(no_escapes))
    no_escapes = Packet(no_escapes)
    print("Retreived packet: {}".format(str(no_escapes.payload)))

    assert output is not None
    assert True is False

    """Ignore the following as it is to remember to never give up."""
    # Get sample packet to be send through hook
    # pkt = 'E\x00\x00\x14\x00\x01\x00\x00@\x00|\xe7\x7f\x00\x00\x01\x7f\x00\x00\x01'
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
    # pkt = Packet(pkt)
    # pkt = str(pkt.payload)

    # SEND PCAP IS ERROR
    # pcap = rdpcap(sample_pcap_path)
    # test_hook.run(sample_hook_path, pcap)

    # Send pcap sample path 'works' but complains that a String
    # test_hook.run(sample_hook_path, sample_pcap_path)

    # test_hook.run(sample_hook_path, pkt)
