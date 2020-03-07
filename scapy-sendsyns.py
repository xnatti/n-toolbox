#!/usr/bin/python3

'''Purpose:
Just being able to send a SYN packet with scapy, to test random stuff.
Currently has issues as it requires root permission

'''

import scapy.all as scapy
import random




def sendsyns(ip, port, count):
    counter = 0
    while counter < count:
        counter += 1
        sourceport = random.randint(3000,8000)
        scapy.send(scapy.IP(dst=ip)/scapy.TCP(dport=port, sport=sourceport))


