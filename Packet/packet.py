"""
Packet class will provide its information to the classes that need it.
"""
from pyutils import get_timestamp


class Packet:

    def __init__(self, name, layers):
        self.name = name
        self.timestamp = get_timestamp()
        self.layers = layers

    def getName(self):
        return self.name

    def getLayers(self):
        return self.layers
