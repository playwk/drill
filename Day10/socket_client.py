#Author ZhengZhong,Jiang

import socket

ck = socket.socket()

ck.connect(('127.0.0.1', 9999, ))

r_data = ck.recv(1024)
print(r_data.decode())

while True:
    inp = input('>>> ').strip()
    ck.sendall(bytes(inp, encoding='utf8'))
    r_data = ck.recv(1024)
    print(r_data.decode())
