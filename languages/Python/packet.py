# -*- coding: utf-8 -*-

import socket

import dpkt

def printPcap(pcap):
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            print '[+] Src: ' + src + ' --> Dst: ' + dst
        except:
            pass


def main():
    f = open('geotest.pcap')
    pcap = dpkt.pcap.Reader()
    printPcap(pcap)
