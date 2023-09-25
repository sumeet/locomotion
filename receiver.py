#!/usr/bin/env python
# reads UDP multicast messages from all ifaces on port 5555
# sends them to stdout packed in the following format:
# - 4 bytes packed ipv4 address
# - 2 bytes (16 bit) payload length
# - payload

# it's just that repeated

import os
import sys
import socket
from ipaddress import ip_address

UDP_IP = "0.0.0.0"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

stdout = os.fdopen(sys.stdout.fileno(), "wb", closefd=False)

while True:
    data, addr = sock.recvfrom(1 << 16)
    print(f'got {len(data)} bytes from {addr[0]}', file=sys.stderr)
    stdout.write(ip_address(addr[0]).packed)
    stdout.write(len(data).to_bytes(2, 'little'))
    stdout.write(data)
    stdout.flush()
