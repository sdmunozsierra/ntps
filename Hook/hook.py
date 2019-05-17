"""
Cook class will provide its information to the classes that need it.
"""
import os
import fnmatch
import subprocess
from pyutils import check_file_exists, extract_hook_name
from Hooks import dns_sport, tcp_3handshake, tcp_sport


class Hook:

    def __init__(self, name, description, status, hook_order, path):
        self.path = path
        self.name = name
        self.description = description
        self.status = status  # Boolean
        self.hook_order = hook_order
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

    def get_hook_info(self, hook_name):
        if self.name == hook_name:
            info = f"Hook name: {self.name}\nHook description: {self.description}"
            info = f"{info} Hook status: {self.status}\nHook order: {self.hook_order}"
            info = f"{info} Hook real name: {self.real_name}"
            print(info)
        print(f"Hook {hook_name} not found")
