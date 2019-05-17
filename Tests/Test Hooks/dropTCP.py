from scapy.all import *
import os, fnfqueue

class dropTCP:

    def drop(self):
        if(packet.haslayer(tcp))
            payload.set_verdict(nfqueue.NF_DROP)
        