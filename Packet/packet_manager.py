"""
Packet class will provide its information to the classes that need it.
"""

import os
import sys

from ntps.Packet import pcap
from ntps.Packet import queue

# fileDir= os.path.dirname(__file__)
# sys.path.append(fileDir)


class PacketManager:

    def __init__(self):
        self.queue = queue.Queue(100)
        self.pcap = None

    def setQueueSize(self, size):
        self.queue.setSize(size)

    def loadPcap(self, name):
        self.pcap = pcap.PCAP(name, 0)
        self.pcap.load()

    def removeFromPcap(self, packet):
        self.pcap.removePacket(packet)

    def getPcapPacket(self, name):
        return self.pcap.getPacket(name)

    def addToQueue(self, packet):
        self.queue.addPacket(packet)

    def getQueuePacket(self, packetName):
        self.queue.getPacket(packetName)

    def getQueuePackets(self):
        return self.queue.getPackets

    def getPcapPackets(self):
        return self.pcap.getPackets()
