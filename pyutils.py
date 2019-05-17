"""
Utility methods and helper methods used around the project.
"""
import datetime
import time
from pathlib import Path
from scapy.packet import Packet


def get_timestamp():
    """Gets a current timestamp with a global format."""
    # Create a timestamp
    timestamp = time.time()
    # Format the timestamp
    timestamp = datetime.datetime.fromtimestamp(timestamp).strftime(
        '%H:%M:%S')
    return timestamp


def extract_hook_name(filepath):
    # if not check_file_exists(filepath):
    #     return  # Maybe raise error
    pre_hook_name = filepath.split('/')
    hook_name = pre_hook_name[-1]
    hook_name = hook_name[:-3]
    print("Extracted hook {}".format(hook_name))
    return hook_name


def check_file_exists(filepath):
    """Checks if the file exists."""
    # print("Checking if filepath {} is a file".format(filepath))
    filepath = "{}".format(filepath)
    fl = Path(filepath)
    if fl.is_file():
        return True
    return False


def create_packet(binary_packet):
    """Loads a packet to be sent via subprocess."""
    return Packet(binary_packet)


def load_packet(binary_packet):
    """Loads a packet to be sent via subprocess."""
    pkt = Packet(binary_packet)
    pkt = str(pkt.payload)
    return pkt


def unload_packet(string_packet):
    """Unloads packet to be read after subprocess."""
    return Packet(string_packet)


def retreive_packet():
    pass
