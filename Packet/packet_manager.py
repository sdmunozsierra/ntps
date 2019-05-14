#from packet import Packet

import os
import sys

fileDir= os.path.dirname(__file__)
sys.path.append(fileDir)

from pcap import PCAP
from queue import Queue


class PacketManager:

    def __init__(self):
        self.queue = Queue(100)
        self.pcap = None
        
    def setQueueSize(self, size):
        self.queue.setSize(size)

    def loadPcap(self, name):
        self.pcap = PCAP(name,0)
        self.pcap.load()
        
    def removeFromPcap(self, packet):
        pcap.removePacket(packet)
        
    def addToQueue(self, packet):
        self.queue.addPacket(packet)

    def getQueuePacket(self, packetName):
        self.queue.getPacket(packetName)

    def getQueuePackets(self):
        return queue.getPackets

    def getPcapPackets(self):
        return self.pcap.getPackets()
