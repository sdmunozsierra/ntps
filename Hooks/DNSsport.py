from scapy.all import *


class DNSsport:

    def changeSport(self, packet):
        """Changes the port number.
        :param packet: String packet sent from hook class.
        """
        packet = Packet(packet)
        sPort = 44444
        if packet.haslayer(DNS):
            packet.sport = sPort
        print(str(packet.payload))
        # return packet
        #     return True
        # return False


if __name__ == "__main__":
    DNSsport().changeSport(sys.argv[1])
