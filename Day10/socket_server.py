#Author ZhengZhong,Jiang

import socket
import select

sk = socket.socket()

sk.bind(('127.0.0.1', 9999, ))

sk.listen(5)

inputs = [sk, ]
outputs = []
message = {}

while True:
    r_list, w_list, elist = select.select(inputs, outputs, [sk, ], 1)
    print(len(inputs), len(r_list), len(w_list), len(outputs))
    for r in r_list:
        if r == sk:
            conn, address = r.accept()
            inputs.append(conn)
            message[conn] = []
            conn.sendall(bytes('hello', encoding='utf8'))
        else:
            try:
                r_data = r.recv(1024)
                if not r_data:
                    raise Exception('disconnect ...')
                else:
                    outputs.append(r)
                    message[r].append(r_data)
            except Exception as e:
                inputs.remove(r)
                del message[r]

    for w in w_list:
        msg = message[w].pop()
        w.sendall(bytes('%s %s' % (msg.decode(), 'OK'), encoding='utf8'))
        outputs.remove(w)

