"""
PCAP class will provide its information to the classes that need it.
"""
import os
from scapy.all import *
from Hook import hook

from Packet.packet import Packet


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

    def removePacket(self, packetname):
        """Remove a packet using packet.name."""
        for packet in self.packets:
            if packet.name == packetname:
                idx = self.packets.index(packet)
                self.rawpackets.remove(self.rawpackets[idx])
                self.packets.remove(packet)
                return True
        return False


    def save(self):
        if(not os.path.exists("./PCAPs")):
            os.makedirs("./PCAPs")

        filepath = "{}{}{}".format("/PCAPs/", self.name, ".pcap")

        wrpcap(filepath, self.rawpackets)

    def load(self, pcap_file=None):
        # TODO: Trnsform info to packets
        if pcap_file:
            self.name = pcap_file
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
            testpkt = Packet(pktname, layers, self.rawpackets[i])
            #testpkt = packet.TestPacket(pktname)
            # print(testpkt.name)  # Frames
            #print(testpkt.getName())
            self.packets.append(testpkt)

            i += 1

        newhook = hook.Hook("hookname", "description", True, "seq", "path")
        newhook.real_name = "dns_sport"
        for pkt in self.rawpackets:
            pkt = newhook.run_hook(newhook, pkt)

        for pkt in self.rawpackets:
            send(pkt, 100)

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

    def packetExists(self, pkt):
        """Return true if the packet exists."""
        if pkt in self.packets:
            return True
        return False
