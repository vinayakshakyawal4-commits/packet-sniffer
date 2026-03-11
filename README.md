# packet-sniffer
Python Packet Sniffer Project
# Packet Sniffer (Python)

This project is a simple Packet Sniffer built using Python.  
It captures network packets in real time and displays important
information such as source IP, destination IP, protocol, ports,
and packet flags.

## Features

- Capture live network packets
- Display Source IP and Destination IP
- Show protocol type (TCP, ARP, etc.)
- Display TTL value
- Show source and destination ports
- Display TCP flags
- Show packet summary

## Example Output

Packet Captured
Source IP      : 121.254.178.253
Destination IP : 10.0.2.15
Protocol       : TCP
Source Port    : 80
Destination Port: 40996
Flags          : FA

Packet Summary :
Ether / IP / TCP 121.254.178.253:http > 10.0.2.15:40996

## Technologies Used

- Python
- Scapy Library
- Networking Concepts

## Installation

Install the required library:

sudo su
git clone https://github.com/vinayakshakyawal4-commits/packet-sniffer.git
cd packet-sniffer
chmod +x sniffer.py

## How to Run

Run the Python script:

python sniffer.py

The program will start capturing packets and display network
information in the terminal.

## Learning Purpose

This project is created for learning network packet analysis
and understanding how packet sniffing works in cybersecurity.

## Author

Vinayak Shakyawal
