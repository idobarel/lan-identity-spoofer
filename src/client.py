import socket

class Client():
    def __init__(self, ip, mac) -> None:
        self.ip = ip
        self.mac = mac
        self.name = self.findName()
    
    def findName(self):
        try:
            return socket.gethostbyaddr(self.ip)[0]
        except:
            return "Unknown."

