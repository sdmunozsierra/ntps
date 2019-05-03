import fnfqueue
from scapy.all import *
import os
class IPTable:

    def __init__(self):
        self.status = False

    def toggleIPTableState(self):
        if (self.status == False):
            # set the IPtable rules -I is to insert the rule -d is the destination -j to jump if it matches rule to NFQUEUE is
            rule = "iptables -I INPUT -d 192.168.0.0/24 -j NFQUEUE --queue-num 1"
            os.system(rule)
            self.status = True
        if (self.status == True):
            # Turn the IPtable off -F is to delete all the current rules -X is to delete all the user defined rules
            os.system('iptables -F')
            os.system('iptables -X')
            self.status = False

    def getStatus(self):
        return self.status
