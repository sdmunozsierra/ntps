from netfilterqueue import NetfilterQueue
from scapy.all import *
import os
class IPTable:
    nfq= NetfilterQueue()

    def __init__(self):
        self.status = False

    def toggleIPTableState(self):

        if (self.status == False):
            # set the IPtable rules -A is to append a new rule to the exisiting rules  -j to jump if it matches rule to NFQUEUE is
            rule = "iptables -A OUTPUT -j NFQUEUE --queue-num 1" 
            os.system(rule)
            self.nfq.bind(1, "new packet function")
            self.nfq.run(block=True)
            self.status = True
        if (self.status == True):
            # Turn the IPtable off -D is to delete the current rules
            self.nfq.unbind()
            delete_rule= "iptables -D OUTPUT -j NFQueue --queue-num 1"
            os.system(delete_rule)
            self.status = False

    def getStatus(self):
        return self.status
