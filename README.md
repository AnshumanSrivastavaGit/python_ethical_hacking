# Python Ethical Hacking

## Description

* This repository contains a collection of ethical hacking programs such as backdoors, keyloggers, credential harvesters, and network/website monitoring tools written in Python.

## Learning Objectives

* Basics of network hacking / penetration testing
* Network mapping
* ARP Spoofing - redirect the flow of packets in a network
* DNS Spoofing - Redirect requests from one website to another
* Detecting ARP spoofing attacks
* Changing MAC address & bypassing filtering
* Spying on any client connected to the network - see usernames, passwords, visited urls ....etc
* Injecting code in pages loaded by any computer connected to the same network
* Replacing files on the fly as they get downloaded by any computer on the same network
* Bypassing HTTPS
* Creating malware for Windows, OS X and Linux
* Creating trojans for Windows, OS X and Linux
* Hacking Windows, OS X and Linux using custom backdoor
* Bypassing Anti-Virus programs
* Using fake login prompt to steal credentials
* Displaying fake updates
* Using own keylogger to spy on everything typed on a Windows or OS X computer
* Learning the basics of website hacking / penetration testing
* Discovering subdomains
* Discovering hidden files and directories in a website
* Running wordlist attacks to guess login information
* Discovering and exploit XSS vulnerabilities
* Discovering weaknesses in websites using own vulnerability scanner

## Tasks

| Program           | Description                                                                                               |
|-------------------|-----------------------------------------------------------------------------------------------------------|
| [MAC Changer](./mac_changer.py) | Changes MAC Address to user input |
| [Network Scanner](./network_scanner.py) | Scans network and discovers the IP and MAC address of all connected clients |
| [Arp Spoofer](./arp_spoofer.py) | Runs an arp spoofing attack to redirect the flow of packets in the network, allowing user to intercept data |
| [Packet Sniffer](./packet_sniffer.py) | Filters intercepted data and shows usernames, passwords, visited links ....etc |
| [DNS Spoofer](./dns_spoofer.py) | Redirects DNS requests, eg: redirects requests to from one domain to another. |
| file_interceptor  | replaces intercepted files with any file we want.                                                         |
| code_injector     | injects code in intercepted HTML pages.                                                                   |
| arpspoof_detector | detects ARP spoofing attacks.                                                                             |
| execute_command payload | executes a system command on the computer it gets executed on. |
| execute_and_report payload | executes a system command and reports result via email. |
| download_and_execute payload | downloads a file and executes it on target system. |
| download_execute_and_report payload | downloads a file, executes it, and reports result by email. |
| reverse_backdoor | gives remote control over the system it gets executed on, allows us to |
| keylogger | records key-strikes and sends them to us by email. |
| crawler | discovers hidden paths on a target website. |
| discover_subdomains | discovers subdomains on target website. |
| spider | maps the whole target website and discovers all files, directories and links. |
| guess_login | runs a wordlist attack to guess login information. |
| vulnerability_scanner | scans a target website for weaknesses and produces a report with all findings. |

## Usage

* All files were created and compiled on Mac OS X 10.11 and Linux Kali with Python3 (version 3.7)

## Awknowledgements

* Zaid Sabih's course "Learn Python & Ethical Hacking From Scratch" on Udemy.com

---

## Author

* __Tu Vo__
