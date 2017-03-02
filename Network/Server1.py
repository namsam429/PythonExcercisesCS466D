#!/usr/bin/python3           # This is server.py file
import socket                                         

# create a socket object
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = "localhost"                           

port = 9999                                           

serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# bind to the port
serversocket.bind((host, port))                                  

# queue up to 5 requests
serversocket.listen(5)                                           

while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()      

    print("Got a connection from %s" % str(addr))
    
    msg='Connected To Server'+ "\r\n"
    clientsocket.send(msg.encode('ascii'))
    while True:
    	msg = clientsocket.recv(1024)
    	if msg.decode('ascii') == "E":
    		break
    	print(msg.decode('ascii'))
    clientsocket.close()