#from Interface.interception_interface import InterceptionInterface
from Interface.ip_table import IPTable
import os, sys

class InterfaceManager:
    
    def __init__(self):
<<<<<<< HEAD
       # self.nfqueue = InterceptionInterface()
=======
        #self.nfqueue = InterceptionInterface()
>>>>>>> 0841c1b419d5282fd46ccb2496f979c423eab453
        self.ip_table = IPTable()
        
    def toggleIPtableState(self):
        self.ip_table.toggleIPTableState()
        
    def toggleIntercepting(self):
        self.nfqueue.toggleIntercept()