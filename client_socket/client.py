from socket import *

print("started")
clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('192.168.56.112',8080))

print('connection is confirmed')
clientSock.send('I am a client'.encode('utf-8'))

print('msg sended')

data = clientSock.recv(1024)
print('recieved data : ', data.decode('utf-8'))
