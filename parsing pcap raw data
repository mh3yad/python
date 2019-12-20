#!/usr/bin/env python
from scapy.all import *
flag =[]
pcap =rdpcap('capture.pcap')
for i in pcap[UDP]:
        try:
               print(i[Raw].load)
        except IndexError:
             continue

