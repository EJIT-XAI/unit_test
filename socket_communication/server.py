# !/bin/python

from socket import *

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('',8080))
serverSock.listen(1)

connectionSock, addr=serverSock.accept()

print(str(addr),"is connected to server")

data = connectionSock.recv(1024)
print('received data :', data.decode('utf-8'))

connectionSock.send('I am a server.'.encode('utf-8'))
print('send a message to client')
