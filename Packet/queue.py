"""
PCAP class will provide its information to the classes that need it.
"""

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
        index = packets.index(packet)
        if(index == 0):
            packet = packets.pop([0])
            InterceptionInterface.sendPacket(packet)
            pcap.addPacket(packet)
            
        else:
            while(index >= 0):
                packet = packets.pop([0])
                InterceptionInterface.sendPacket()
                pcap.addPacket(packet)
                index = index - 1

    def dropPacket(self, packet):
        packets.remove(packet)

    def addPacket(self, packet):
        if(len(packets) >= size):
            return
        else:
            packets.append(packet)

    def getPackets(self):
        return packets

    def getPacket(self,packetName):
        for packet in packets:
            if(packet.getName() == packetName):
                retrun packet

        return None
    def getSize(self):
        return this.size
