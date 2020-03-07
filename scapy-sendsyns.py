#!/usr/bin/python3

'''Purpose:
Just being able to send a SYN packet with scapy, to test random stuff.
Currently has issues as it requires root permission

'''

import scapy.all as scapy
import random

print('\nSyntax is as....')
print('sendsyns(<ip address>, <dst port>, <count>\n')


# short reference https://packetlife.net/media/library/36/scapy.pdf


# a while loop that takes IP, port and a count as an argument
# will send TCP SYN packets to IP:port four count number of tims.
# will not wait for a return packet.


def sendsyns(ip, port, count):
    counter = 0
    while counter < count:
        counter += 1
        sourceport = random.randint(3000,8000)
        scapy.send(scapy.IP(dst=ip)/scapy.TCP(dport=port, sport=sourceport))


# using sendp may be faster...

def sendpsyns(ip, port, count):
    counter = 0
    while counter < count:
        counter += 1
        sourceport = random.randint(3000,8000)
        scapy.sendp(scapy.Ether()/scapy.IP(dst=ip)/scapy.TCP(dport=port, sport=sourceport), iface="eth0")


