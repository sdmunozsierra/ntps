"""
Packet class will provide its information to the classes that need it.
"""
from pyutils import get_timestamp
# import os
# import sys
# fileDir= os.path.dirname(__file__)
# sys.path.append(fileDir)

from Packet.layer import Layer


class Packet:
    def __init__(self, newname, rawlayers):
        self.name = newname
        self.timestamp = get_timestamp()

        self.layers = list()
        pos = 0
        for rlayer in rawlayers:
            layer = Layer(rlayer.payload, rlayer.name, rlayer.name, pos, rlayer.summary())
            self.layers.append(layer)
            pos += 1


    def getName(self):
        return self.name

    def getLayers(self):
        return self.layers


class TestPacket:
    """Test a packet with no layers."""

    def __init__(self, newname):
        self.name = newname
        self.timestamp = get_timestamp()

    def getName(self):
        return self.name
