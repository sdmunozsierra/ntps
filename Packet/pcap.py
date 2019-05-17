"""
PCAP class will provide its information to the classes that need it.
"""
import os
from scapy.all import *

from Packet import packet


import subprocess

class PCAP:

    def __init__(self, name, timestamp):
        self.rawpackets = list()
        self.packets = list()
        #filepath = "{}{}{}".format("/", self.name, ".pcap")

        self.name = name
        self.timestamp = timestamp
        #self.load()


    def setName(self, newname):
        self.name = newname

    def addPacket(self, packet):
        self.rawpackets.append(packet)

    def removePacket(self, packet):
        self.rawpackets.remove(packet)

    def save(self):
        # TODO: save to file
        if(not os.path.exists("./PCAPs")):
            os.makedirs("./PCAPs")

        filepath = "{}{}{}".format("/PCAPs/", self.name, ".pcap")

        wrpcap(filepath, self.packets)
        #file = open(filepath, 'w')
        #file.write("Hello")
        #file.close()

    def load(self):
        # TODO: Trnsform info to packets
        pcapfile = rdpcap(self.name)
        i = 1
        for packet in pcapfile:
            self.rawpackets.append(packet)

        i = 0
        test = list()
        #self.packets[1].show()
        while i < len(self.rawpackets):
            test.append(list(self.expand(self.rawpackets[i])))
            i += 1

        i = 0
        while i < len(self.rawpackets):
            pktname = "Frame " + str(i+1) + ": "
            layers = list()
            for layer in test[i]:
                pktname += layer.name + " "
                layers.append(layer)
            #print(pktname)
            #print(pktname)
            testpkt = packet.Packet(pktname, layers)

            #print(testpkt.name)
            #print(testpkt.getName())
            self.packets.append(testpkt)

            i += 1

        #print("?")
        pass

    def expand(self,x):
        yield x
        while x.payload:
            #print(x.payload)
            x = x.payload
            yield x
        #print("!")

    def getPackets(self):
        return self.packets

    def getPacket(self,name):
        for packet in self.packets:
            if(packet.name == name):
                return packet

        return None

#pcap = PCAP("test", 0)
#pcap.save()
#pcap.load()



#for packet in pcap.packets:
#    for layer in packet:




#packets = sniff(iface = conf.iface, count = 10)
#for pkt in packets:
#    pkt.show()
