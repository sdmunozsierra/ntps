from scapy.all import *


class DNSsport:

    def __init__(self):
        self.name = "dns_sport"

    def change_sport(self, packet):
        """Changes the port number.
        :param packet: String packet sent from hook class.
        """
        print("Inside DNSport")
        sPort = 44444
        if packet.haslayer(DNS):
            packet.sport = sPort
        return packet


if __name__ == "__main__":
    DNSsport().change_sport(sys.argv[1])
