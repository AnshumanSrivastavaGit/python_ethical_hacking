# Python Ethical Hacking

## Description

* This repository contains a collection of ethical hacking programs such as backdoors, keyloggers, credential harvesters, network hacking tooks and website hacking tools written in Python.

## Learning Objectives

* Basics of network hacking / penetration testing.
* Changing MAC address & bypassing filtering.
* Network mapping.
* ARP Spoofing - redirect the flow of packets in a network.
* DNS Spoofing - Redirect requests from one website to another.
* Spying on any client connected to the network - see usernames, passwords, visited urls ....etc.
* Inject code in pages loaded by any computer connected to the same network.
* Replace files on the fly as they get downloaded by any computer on the same network.
* Detect ARP spoofing attacks.
* Bypass HTTPS.
* Create malware for Windows, OS X and Linux.
* Create trojans for Windows, OS X and Linux.
* Hack Windows, OS X and Linux using custom backdoor.
* Bypass Anti-Virus programs.
* Use fake login prompt to steal credentials.
* Display fake updates.
* Use own keylogger to spy on everything typed on a Windows or OS X computer.
* Learn the basics of website hacking / penetration testing.
* Discover subdomains.
* Discover hidden files and directories in a website.
* Run wordlist attacks to guess login information.
* Discover and exploit XSS vulnerabilities.
* Discover weaknesses in websites using own vulnerability scanner.

## Tasks

| Program           | Description                                                                                               |
|-------------------|-----------------------------------------------------------------------------------------------------------|
| mac_changer       | changes MAC Address to anything we want.                                                                  |
| network_scanner   | scans network and discovers the IP and MAC address of all connected clients.                              |
| arp_spoofer       | runs an arp spoofing attack to redirect the flow of packets in the network allowing us to intercept data. |
| packet_sniffer    | filters intercepted data and shows usernames, passwords, visited links ....etc                            |
| dns_spoofer       | redirects DNS requests, eg: redirects requests to from one domain to another.                             |
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

* All files were created and compiled on Mac OS X 10.11 with Python3 (version 3.7)

## Awknowledgements

* Zaid Sabih's course "Learn Python & Ethical Hacking From Scratch" on Udemy.com

---

## Author

* __Tu Vo__
