import socket
import sys

ip = "localhost"
port = 9999

sock = socket.socket()
sock.connect((ip, port))
f_name = "messagetoserver.txt"
sock.send((bytes(f_name, encoding = 'UTF-8')))
f = open ("/root/send/" + f_name, "rb")
l = f.read(1024)
while (l):
	sock.send(l)
	l = f.read(1024)
f.close()
sock.close()
