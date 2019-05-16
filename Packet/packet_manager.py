#from packet import Packet

import os
import sys


from PyQt5.QtCore import QObject, pyqtSignal
fileDir= os.path.dirname(__file__)
sys.path.append(fileDir)

from pcap import PCAP
from queue import Queue
from packet import Packet

class PacketManager(QObject):

    queuesignalAdd = pyqtSignal(Packet)

    def __init__(self):
        super().__init__()
        self.queue = Queue(100)
        self.pcap = None
        
    def setQueueSize(self, size):
        self.queue.setSize(size)

    def loadPcap(self, name):
        self.pcap = PCAP(name,0)
        self.pcap.load()
        
    def removeFromPcap(self, packet):
        pcap.removePacket(packet)
        
    def getPcapPacket(self, name):
        pkt =  self.pcap.getPacket(name)
        self.queuesignalAdd.emit(pkt)
        return pkt
    
    def addToQueue(self, packet):
        self.queue.addPacket(packet)
        self.queuesignalAdd.emit(packet)

    def dropFromQueue(self, packet):
        self.queue.dropPacket(packet)

    def forwardFromQueue(self, packet):
        self.queue.forwardPacket(packet)
        
    def getQueuePacket(self, packetName):
        self.queue.getPacket(packetName)

    def getQueuePackets(self):
        return queue.getPackets

    def getPcapPackets(self):
        return self.pcap.getPackets()
