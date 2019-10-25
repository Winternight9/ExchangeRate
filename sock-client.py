import socket
import time
s = socket.socket(socket.AF_INET,
socket.SOCK_STREAM)
s.connect(('10.2.46.148',10001))
amount = input("Please specify amount of money and currency: ")

s.send(bytes(str.encode(f'{amount}')))
time.sleep(0.5)
msg=s.recv(1024)
print(msg.decode())
