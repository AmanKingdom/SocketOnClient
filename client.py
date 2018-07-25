# coding=utf-8

import socket

s = socket.socket()

host = socket.gethostname()
port = 8001
s.bind((host, port))

s.listen(5)
while True:
    c, addr = s.accept()
    print('get')
    c.send('I got your message.'.encode('utf-8'))
    c.close()