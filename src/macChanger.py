import subprocess
import os

class MacHandler():
    def __init__(self, iface:str) -> None:
        self.myMac = self.findMyMac()
        self.iface = iface

    def findMyMac(self):
        return os.popen("ifconfig | grep ether").read().split(" ")[9]
    
    def restoreMac(self):
        self.changeMac(self.myMac)

    def changeMac(self, new_mac_address):
        subprocess.check_output(f"ifconfig {self.iface} down", shell=True)
        subprocess.check_output(f"ifconfig {self.iface} hw ether {new_mac_address}", shell=True)
        subprocess.check_output(f"ifconfig {self.iface} up", shell=True)
