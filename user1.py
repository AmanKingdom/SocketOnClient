# coding=utf-8

import socket

s = socket.socket()

host = socket.gethostname()
port = 8001

s.connect((host, port))
print(s.recv(1024))
