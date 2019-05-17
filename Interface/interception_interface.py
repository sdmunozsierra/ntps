from scapy.all import *
from netfilterqueue import NetfilterQueue
from Packet.packet_manager import PacketManager

class InterceptionInterface:
    def __init__(self):
        self.intercepting = False
        return
    
    def toggleIntercept(self):
        if (self.intercepting == False):
            self.nfqueue = NetfilterQueue()
            self.nfqueue.bind(1,self.display)
            self.intercepting = True
            print("Interception has been turned on.")
        else:
            self.nfqueue.unbind()
            print("Inteception has been turned off.")
            self.intercepting = False

    def display(self, packet):
        print(packet)
        packet = IP(packet.get_payload())
        print(type(packet))
        self.packet_manager.addToQueue(packet)