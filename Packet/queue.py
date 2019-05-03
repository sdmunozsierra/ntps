#
# Stuff
#

class Queue:
    packets = list()
    size = 100
    
    def __init__(self, size):
        self.size = size

    def setSize(self, newSize):
        self.size = newSize

    def forwardPacket(self, packet):
        index = packets.index(packet)
        if(index == 0):
            InterceptionInterface.sendPacket(packets.pop([0]))
        else:
            while(index >= 0):
                InterceptionInterface.sendPacket(packets.pop([0]))
                index = index - 1

    def dropPacket(self, packet):
        packets.remove(packet)

    def addPacket(self, packet):
        if(len(packets) >= size):
            return
        else:
            packets.append(packet)

    def getPackets(self):
        return this.packets

    def getSize(self):
        return this.size

    
