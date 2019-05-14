class PacketManager:

    def __init__(self):
        self.queue = Queue(100)
        self.pcap = None
        
    def setQueueSize(self, size):
        self.queue.setSize(size)

    def loadPcap(self, name):
        self.pcap = Pcap(name)
        
    def removeFromPcap(self, packet):
        pcap.removePacket(packet)
        
    def addToQueue(self, packet):
        self.queue.addPacket(packet)

    def getPacket(self, packetName):
        self.queue.getPacket(packetName)

    def getPackets(self):
        return queue.getPackets)
