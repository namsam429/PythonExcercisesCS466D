#!/usr/bin/python3           # This is client.py file

import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = "localhost"                           

port = 9999

# connection to hostname on the port.
s.connect((host, port))                               

# Receive no more than 1024 bytes
msg = s.recv(1024)      

msg2 = "Request From Client 1\n"
s.send(msg2.encode('ascii'))

print (msg.decode('ascii'))

while True:
	
	msg3 = input("Enter a msg: ")

	if msg3 == "E":
		break
	s.send(msg3.encode('ascii'))

s.close()
