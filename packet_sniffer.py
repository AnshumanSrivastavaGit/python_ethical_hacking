"""
Packet Sniffer

"""


import scapy.all as scapy
from scapy.layers import http


def sniff(interface):
    # store = where packets are stored
    # prn = callback func
    # easy way
    scapy.sniff(
            iface=interface,
            store=False,
            prn=process_sniffed_packet
            )


def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        print(packet)


sniff("eth0")
