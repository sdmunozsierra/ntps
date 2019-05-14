from scapy.all import *

class TCPhandshake:

    def handshake(self,packet):
        if(packet.haslayer(TCP)):
            source = packet.src
            destination = packet.dst
            sourcePort = packet.sport
            destinationPort = packet.dport
            sequence = packet.ack
            acknowledge = packet.seq + 1
            ip = IP(src = destination, dst = source)
            packet_ack = TCP(sport = destinationPort, dport = sourcePort, flags = 'A', seq = sequence , ack = acknowledge)
            send(ip/packet_ack)