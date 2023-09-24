#!/usr/bin/env python

import socket
import sys
import os

UDP_IP = "255.255.255.255"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

stdin = os.fdopen(sys.stdin.fileno(), "rb", closefd=False)

while header := stdin.read(2):
    num_bytes = int.from_bytes(header, 'little')
    print(f'sending {num_bytes} bytes over the net', file=sys.stderr)
    sock.sendto(stdin.read(num_bytes), (UDP_IP, UDP_PORT))
    print('sent the bytes', file=sys.stderr)

