from scapy.all import *
import os
class IPTable:

    def __init__(self):
        self.status = False

    def toggleIPTableState(self):

        if (self.status == False):
            # Set the IPtable rules -A is to append a new rule to the exisiting rules  -j to jump if it matches rule to NFQUEUE is
            rule = "iptables -A INPUT -j NFQUEUE --queue-num 1" 
            os.system(rule)
            self.status = True
        else:
            # Turn the IPtable off -D is to delete the current rules
            delete_rule = "iptables -D INPUT -j NFQueue --queue-num 1"
            os.system(delete_rule)
            self.status = False

    def getStatus(self):
        return self.status
