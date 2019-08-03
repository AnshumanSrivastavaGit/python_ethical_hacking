"""
Network Scanner
- Discover all devices on the network
- Display their IP address
- Display their MAC address

# discover
netdiscover -r <ip_range>

# display routing table
route -n

ARP (address resolution protocol)
- link IP addresses with MAC addresses
"""

import scapy.all as scapy
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
            "-t", "--target", dest="target", help="Target IP / IP range."
            )
    return parser.parse_args()


def scan(ip):
    # easy way
    # scapy.arping(ip)

    arp_request = scapy.ARP(pdst=ip)
    # scapy.ls(scapy.ARP())
    # print(arp_request.summary())

    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # scapy.ls(scapy.Ether())
    # print(broadcast.summary())

    arp_request_broadcast = broadcast/arp_request
    # print(arp_request_broadcast.summary())
    # arp_request_broadcast.show()

    # send, recieve packets
    answered_list = scapy.srp(
            arp_request_broadcast, timeout=1, verbose=False
            )[0]
    clients_list = []
    for element in answered_list:
        _dict = {'ip': element[1].psrc, 'mac': element[1].hwsrc}
        clients_list.append(_dict)
    return clients_list


def print_result(results_list):
    print("IP\t\t\tMAC Address\n--------------------------------------")
    for client in results_list:
        print(client['ip'] + '\t\t' + client['mac'])
    print("--------------------------------------")


options = get_args()
scan_result = scan(options.target)
print_result(scan_result)
