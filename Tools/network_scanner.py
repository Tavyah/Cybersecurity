#!/usr/bin/env python

import scapy.all as scapy

def main() -> None:
    scan('192.168.52.137', 'ff:ff:ff:ff:ff:ff')

def scan(ip_address: str, mac_address: str) -> None:
    arp_request = scapy.ARP(pdst = ip_address)
    broadcast = scapy.Ether(dst = mac_address)
    arp_request_broadcast = broadcast/arp_request

if __name__ == "__main__":
    main()