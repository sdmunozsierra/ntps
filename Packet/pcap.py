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
        self.remove(packet)

    def save(self):
        ### TO DO: save to file
        if(not os.path.exists("./PCAPs"):
               os.makedirs("./PCAPs")

        filepath = "/PCAPs/" + name + ".txt"

        file = open(filepath, 'w')
        file.write("Hello")
        file.close()

    def load(self):
        ### TO DO: Transform info to packets

pcap = PCAP("test",0)
pcap.save()
               
