"""
PCAP class will provide its information to the classes that need it.
"""
from scapy.all import sendp

from packet import Packet, PCAP
import datetime

class Queue:
    packets = list()
    size = 100


    def __init__(self, size):
        self.size = size
        date = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")

        self.pcap = PCAP(date, 0)
    def setSize(self, newSize):
        self.size = newSize

    def forwardPacket(self, packet):
        # index = self.packets.index(packet)
        # if(index == 0):
        sendp(self.packets.pop(0))
        return
        # else:
        #     while(index >= 0):
        #         InterceptionInterface.sendPacket(packets.pop([0]))
        #         index = index - 1

    def dropPacket(self, packet):
        self.packets.remove(packet)

    def addPacket(self, packet):
        if(len(self.packets) >= self.size):
            return
        else:
            self.packets.append(packet)

    def getPackets(self):
        return self.packets

    def getPacket(self, packetName):
        for packet in self.packets:
            if(packet.getName() == packetName):
                return packet
        return None

    def getSize(self):
        return self.size
