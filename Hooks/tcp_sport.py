from scapy.all import *
import sys


class TCPsport:

    def __init__(self):
        self.name = "tcp_sport"

    def change_sport(self, packet):
        sPort = 55555
        if(packet.haslayer(TCP)):
            packet.sport = sPort
        return packet


if __name__ == "__main__":
    change_sport(sys.argv[1])
    return
