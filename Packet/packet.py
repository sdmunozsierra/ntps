"""
Packet class will provide its information to the classes that need it.
"""
import time


class Packet:

    def __init__(self, name):
        self.name = name
        self.timestamp = None
