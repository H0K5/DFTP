#! /usr/bin/env python
'''
DFTP client
'''



import socket
import time
import sys
import binascii
import struct
import string


UDP_IP = "127.0.0.1"
UDP_PORT = 53
BUFSIZE = 1024
PDF = "foo.pdf"
#PDF = "/Users/antigen/dev/DFTP/DNS_Exfiltration.pdf"
END = "EOF"

fh = open(PDF)

file_buffer = fh.read(BUFSIZE)
while file_buffer:
    print "UDP target IP:", UDP_IP
    print "UDP target port:", UDP_PORT
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(file_buffer, (UDP_IP, UDP_PORT))
    file_buffer = fh.read(BUFSIZE)
sock.sendto(END, (UDP_IP, UDP_PORT))
