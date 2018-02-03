#!/usr/bin/env python

import subprocess

from scapy.all import *

# torch smartplug
# 192.168.1.223
# 50:C7:BF:5A:2E:6A

def kitchen_counter_lights_toggle():
    subprocess.call(r"C:\Users\James\dev\PyCharmProjects\ScapyToy\run.bat")

def torch_toggle():
    subprocess.call(r"C:\Users\James\dev\PyCharmProjects\ScapyToy\runtorch.bat")

def kitten_desk_lamp_toggle():
    subprocess.call(r"C:\Users\James\dev\PyCharmProjects\ScapyToy\runki10desk.bat")

MAC = {
    '78:e1:03:df:f2:09':kitchen_counter_lights_toggle,  # arm & hammer cat litter
    '00:fc:8b:ee:d2:56':torch_toggle,                   # tide
    '78:e1:03:59:9e:21':kitten_desk_lamp_toggle,        # red bull
}

def detect_button(pkt):
    if pkt.haslayer(DHCP):
        mac_address = pkt[Ether].src
        print "Button Press Detected " + mac_address
        if mac_address.lower() in MAC.keys():
            MAC[mac_address]()
        else:
            print "Unknown button pressed " + mac_address

sniff(prn=detect_button, filter="(udp and (port 67 or 68))", store=0)