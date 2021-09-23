import scapy.all as scapy
def scan(ip):
    scapy.arping(ip) # Sends out ARP requests to discover clients connected on the same network
scan("10.0.2.2/24")

