from scapy.all import *

class DNSsport:

    def changeSport(self,packet):
        sPort=44444
        if(packet.haslayer(DNS)):
            packet.sport=sPort