"""
Packet class will provide its information to the classes that need it.
"""

import os
import sys

from PyQt5.QtCore import QObject, pyqtSignal

from Packet import queue
from Packet import pcap
from Packet import packet

class PacketManager(QObject):

    queuesignalAdd = pyqtSignal(packet.Packet)

    def __init__(self):
        super().__init__()
        self.queue = queue.Queue(100)
        self.pcap = None

    def setQueueSize(self, size):
        self.queue.setSize(size)

    def loadPcap(self, name):
        self.pcap = pcap.PCAP(name, 0)
        self.pcap.load()

    def removeFromPcap(self, packetname):
        self.pcap.removePacket(packetname)

    def getPcapPackets(self):
        return self.pcap.getPackets
        
    def getPcapPacket(self, name):
        #pkt = self.pcap.getPacket(name)
        #self.queuesignalAdd.emit(pkt)
        #return pkt
        return self.pcap.getPacket(name)

    def addToQueue(self, packet):
        if self.queue.addPacket(packet):
            self.queuesignalAdd.emit(packet)

    def dropFromQueue(self, packetname):
        self.queue.dropPacket(packetname)

    def forwardFromQueue(self, packetname):
        self.queue.forwardPacket(packetname)
        
    def getQueuePacket(self, packetName):
        self.queue.getPacket(packetName)

    def getQueuePackets(self):
        return self.queue.getPackets

    def getPcapPackets(self):
        return self.pcap.getPackets()
