"""Module containing global variables to be used across the system."""
from Hook.hook_manager import hookManager
from Interface.interface_manager import InterfaceManager
from Packet.packet_manager import PacketManager

h_manager = hookManager()
i_manager = InterfaceManager()
p_manager = PacketManager()
