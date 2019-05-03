"""
PCAP class will provide its information to the classes that need it.
"""
import os


class PCAP:
    def __init__(self, name, timestamp):
        self.packets = list()
        self.name = name
        self.timestamp = timestamp
        self.load()

    def addPacket(self, packet):
        self.packets.append(packet)

    def removePacket(self, packet):
        self.packets.remove(packet)

    def save(self):
        # TODO: save to file
        if(not os.path.exists("./PCAPs")):
            os.makedirs("./PCAPs")

        filepath = "{}{}{}".format("/PCAPs/", self.name, ".txt")

        file = open(filepath, 'w')
        file.write("Hello")
        file.close()

    def load(self):
        # TODO: Transform info to packets
        pass


pcap = PCAP("test", 0)
pcap.save()
