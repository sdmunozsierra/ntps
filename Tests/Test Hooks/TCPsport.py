from scapy.all import *
import sys

def changeSport(packet):
    sPort=55555
    if(packet.haslayer(TCP)):
        packet.sport=sPort
        return packet
if __name__ == "__main__":
    return changeSport(sys.argv[1])
    
