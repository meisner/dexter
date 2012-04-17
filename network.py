#!/usr/bin/python

import socket

def connect(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((ip, port))
    except:
        sock.close()
        sock = None
    return sock
