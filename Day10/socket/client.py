# Auther: ZhengZhong,Jiang

import socket

ck = socket.socket()

ck.connect(('127.0.0.1', 9999))

recv_bytes = ck.recv(1024)
print(recv_bytes.decode())

while True:
    send_data = input('>>> ').strip()
    ck.sendall(bytes(send_data, encoding='utf8'))
    print(ck.recv(1024))
ck.close()
