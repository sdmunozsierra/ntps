"""
PCAP class will provide its information to the classes that need it.
"""
from scapy.all import sendp

from Packet import packet
from Packet import pcap
import datetime


class Queue:
    packets = list()
    size = 100

    def __init__(self, size):
        self.size = size
        date = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
        self.pcap = pcap.PCAP(date, 0)

    def setSize(self, newSize):
        self.size = newSize

    def forwardPacket(self, packetname):
        for packet in self.packets:
            if(packet.name == packetname):
                forwardpacket = packet
                break

        index = self.packets.index(forwardpacket)
        if(index == 0):
            pkt = self.packets.pop(0)
            self.pcap.addPacket(pkt)
            self.pcap.save()
            sendp(pkt)
            return
        else:
            while(index >= 0):
                pkt = packets.pop(0)
                self.pcap.addPacket(pkt)
                self.pcap.save()
                sendp(pkt)
                index = index - 1

    def dropPacket(self, packetname):
        #self.packets.remove(packet)
        for packet in self.packets:
            if(packet.name == name):
                self.packets.remove(packet)
                break


    def addPacket(self, packet):
        if(len(self.packets) >= self.size):
            return False
        
        #self.packets.append(packet)

        #pcapfile = rdpcap(self.name)
        #i = 1
        #for packet in pcapfile:
        #    self.rawpackets.append(packet)

        i = 0
        test = list()
        #self.packets[1].show()
        #while i < len(self.rawpackets):
        test.append(list(self.expand(packet)))
            i += 1

        #i = 0
        
        pktname = "Frame " + str(i+1) + ": "
        layers = list()
        for layer in test[0]:
            pktname += layer.name + " "
            layers.append(layer)
        #print(pktname)
        #print(pktname)
        testpkt = Packet(pktname, layers, self.rawpackets[i])
        #testpkt = packet.TestPacket(pktname)
        print(testpkt.name)
        #print(testpkt.getName())
        self.packets.append(testpkt)

        #print("?")
  
        return True

    def expand(self,x):
        yield x
        while x.payload:
            #print(x.payload)
            x = x.payload
            yield x
        #print("!")
        
    
    def getPackets(self):
        return self.packets

    def getPacket(self, packetName):
        for packet in self.packets:
            if(packet.getName() == packetName):
                return packet
        return None

    def getSize(self):
        return self.size
