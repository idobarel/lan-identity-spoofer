import scapy.all as scapy
from src.client import Client
import os

class Scanner():
    def __init__(self) -> None:
        self.ip = self.findNetworkIp()
        self.clients = []
    
    def findNetworkIp(self):
        ip = os.popen("ifconfig | grep inet").read().split(" ")[9]
        ip += "/24"
        return ip

    def scan(self):
        packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") / scapy.ARP(pdst=self.ip)
        ans = scapy.srp(packet, timeout=3, verbose=False)[0]
        for e in ans:
            self.clients.append(Client(e[1].psrc, e[1].hwsrc))
    
    def getClients(self):
        return self.clients
    