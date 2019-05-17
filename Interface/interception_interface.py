from scapy.all import *
from netfilterqueue import NetfilterQueue
from packet_manager import PacketManager

class InterceptionInterface:
    def __init__(self):
        return
    
    def initialize(self):
        self.nfqueue = NetfilterQueue()
        self.nfqueue.bind(1)
        
    def end():
        nfqueue.unbind()
        
    
        
        
        
