"""
Cook class will provide its information to the classes that need it.
"""
import os
import fnmatch
import subprocess
from pyutils import check_file_exists, extract_hook_name
from Hooks import dns_sport, tcp_3handshake, tcp_sport


class Hook:

    def __init__(self, name, description, status, hookOrder, path):
        self.path = path
        self.name = name
        self.description = description
        self.status = status  # Boolean
        self.hookOrder = hookOrder
        self.real_name = extract_hook_name(self.path)

    def run_hook(self, a_hook, packet):
        print("Will try to run hook_real name: {}".format(a_hook.real_name))
        if a_hook.real_name == "dns_sport":
            print("Running DNSsport")
            r_hook = dns_sport.DNSsport()
            return r_hook.change_sport(packet)
        if a_hook.real_name == "tcp_3handshake":
            print("Running TCP3Handshake")
            r_hook = tcp_3handshake.TCP3Handshake()
            return r_hook.handshake(packet)
        if a_hook.real_name == "tcp_sport":
            print("Running TCPsport")
            r_hook = tcp_sport.TCPsport()
            return r_hook.change_sport(packet)
        return None
