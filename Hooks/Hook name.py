from scapy.all import *
import os

class dropTCP:

    def drop(self):
        rule = "iptables -A INPUT -j DROP -p tcp" 
        os.system(rule)