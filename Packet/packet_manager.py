"""
Packet class will provide its information to the classes that need it.
"""

import os
import sys

from ntps.Packet import pcap
from ntps.Packet import queue
from ntps.Packet import packet
from PyQt5.QtCore import QObject, pyqtSignal


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

    def removeFromPcap(self, packet):
        self.pcap.removePacket(packet)

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

    def forwardFromQueue(self, packet):
        self.queue.forwardPacket(packet)

    
        
    def getQueuePacket(self, packetName):
        self.queue.getPacket(packetName)

    def getQueuePackets(self):
        return self.queue.getPackets

    def getPcapPackets(self):
        return self.pcap.getPackets()
