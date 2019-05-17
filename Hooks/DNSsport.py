from scapy.all import *


class DNSsport:

    def changeSport(self, packet):
        print("changeSport")
        sPort = 44444
        if packet.haslayer(DNS):
            packet.sport = sPort
        #     return True
        # return False


if __name__ == "__main__":
    pkt = 'E\x00\x00\x14\x00\x01\x00\x00@\x00|\xe7\x7f\x00\x00\x01\x7f\x00\x00\x01'
    DNSsport().changeSport(pkt)
    # DNSsport().changeSport(sys.argv[1])
