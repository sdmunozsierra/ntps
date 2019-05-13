from scapy.all import *

class TCPsport:

    def changeSport(self,packet):
        sPort=55555
        if(packet.haslayer(TCP)):
            packet.sport=sPort