from Interface.interception_interface import InterceptionInterface
from Interface.ip_table import IPTable
# from pyglobals import i_manager
import os, sys


class InterfaceManager:

    def __init__(self):
        self.nfqueue = InterceptionInterface()
        self.ip_table = IPTable()

    def toggleIPtableState(self):
        self.ip_table.toggleIPTableState()

    def toggleIntercepting(self):
        self.nfqueue.toggleIntercept()
