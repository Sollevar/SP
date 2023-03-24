import socket
import sys

sock = socket.socket()
ip = "localhost"
port = 9999
sock.bind((ip,port))
sock.listen(10)
print ('Server is running, please, press ctrl+c to stop')
while True:
	conn, addr = sock.accept()
	print ('connected: ', addr)
	name_f = (conn.recv(1024)).decode ('UTF-8')
	f = open ('/root/recieve/' + name_f,'wb')
	while True:
		l = conn.recv(1024)
		f.write(l)
		if not l:
			break
	f.close()
	conn.close()
	print ('file received')
sock.close()
