import socket

s = socket.socket()
for port in range(20050, 20151):
    try:
        s.connect(("127.0.0.1", port))
        data = s.recv(1024)
        print(data)
    except:
        continue
