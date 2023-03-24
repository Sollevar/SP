import socket
import  uuid
print('Say your name please')
a=input()
print('Hello , '+ a + '!')
hostname = socket.gethostname()
ip=socket.gethostbyname(hostname)
print('your ip address : ' + ip)
print('your mac address : ', end="")
print(':' .join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
for ele in range(0,8*6,8)][::-1]))
