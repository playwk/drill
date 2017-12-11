# Auther: ZhengZhong,Jiang

import socket
import select

sk = socket.socket()

sk.bind(('127.0.0.1', 9999, ))

sk.listen(5)

inputs = [sk, ]

outputs = []

while True:
    r_li, w_li, e = select.select(inputs, outputs, [], 1)
    print(len(inputs), len(r_li), len(w_li), len(outputs))
    for i in r_li:
        if i == sk:
            conn, add = sk.accept()
            inputs.append(conn)
            conn.sendall(bytes('hello', encoding='utf8'))
        else:
            try:
                ret = i.recv(1024)
                if not len(ret):
                    raise Exception('断开连接')
                else:
                    outputs.append(i)
            except Exception as e:
                inputs.remove(i)

    for w in outputs:
        w.sendall(bytes('reponse', encoding='utf8'))
        outputs.remove(w)
