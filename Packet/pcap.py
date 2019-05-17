"""
PCAP class will provide its information to the classes that need it.
"""
import os
from scapy.all import *

from ntps.Packet import packet


import subprocess

class PCAP:

    def __init__(self, name, timestamp):
        self.packets = list()
        self.testpackets = list()
        #filepath = "{}{}{}".format("/", self.name, ".pcap")

        self.name = name
        self.timestamp = timestamp
        #self.load()


    def setName(self, newname):
        self.name = newname

    def addPacket(self, packet):
        self.packets.append(packet)

    def removePacket(self, packet):
        self.packets.remove(packet)

    def save(self):
        # TODO: save to file
        if(not os.path.exists("./PCAPs")):
            os.makedirs("./PCAPs")

        filepath = "{}{}{}".format("/PCAPs/", self.name, ".pcap")

        wrpcap(filepath, self.packets)
        #file = open(filepath, 'w')
        #file.write("Hello")
        #file.close()

    def load(filepath):
        # TODO: Transform info to packets
        pcapfile = rdpcap(filepath)
        i = 1
        for packet in pcapfile:
            self.packets.append(packet)

        i = 0
        test = list()
        #self.packets[1].show()
        while i < len(self.packets):
            test.append(list(self.expand(self.packets[i])))
            i += 1

        i = 0
        while i < len(self.packets):
            pktname = "Frame " + str(i+1) + ": "
            layers = list()
            for layer in test[i]:
                pktname += layer.name + " "
                layers.append(layer)
            #print(pktname)
            #print(pktname)
            testpkt = Packet(pktname, layers)

            #print(testpkt.name)
            #print(testpkt.getName())
            self.testpackets.append(testpkt)

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
        return self.testpackets

    def getPacket(self,name):
        for packet in self.testpackets:
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
