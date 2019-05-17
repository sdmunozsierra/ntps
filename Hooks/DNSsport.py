from scapy.all import *


class DNSsport:

    def __init__(self):
        self.name = DNSsport

    def changeSport(self, packet):
        """Changes the port number.
        :param packet: String packet sent from hook class.
        """
        sPort = 44444
        if packet.haslayer(DNS):
            packet.sport = sPort
        return packet


if __name__ == "__main__":
    DNSsport().changeSport(sys.argv[1])
