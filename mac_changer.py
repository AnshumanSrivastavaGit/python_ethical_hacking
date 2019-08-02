#!/usr/bin/env python

"""
MAC Address
- Media Access Control
  - Permanent
  - Physical
  - Unique
- Assigned by manufacturer

Why change the MAC address?
- Increase anonmyity
- Impersonate other devices
- Bypass filters

"""

import subprocess
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface",
                      help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help" +
                     "for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify a new mac, use --help for more info.")
    return options


def change_mac(interface, new_mac):
    print("\n[+] Changing MAC address for " + interface +
          " to " + new_mac + "\n")

    # list all interfaces on current computer
    subprocess.call(["ifconfig"])

    # disable interface, need permission
    # subprocess.call(["ifconfig", interface, "down"])

    # change MAC (12 characters)
    # subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])

    # enable interface
    # subprocess.call(["ifconfig", interface, "up"])


options = get_arguments()
change_mac(options.interface, options.new_mac)
