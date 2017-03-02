#!/usr/bin/python3           # This is server.py file
import socket         
import math                                

def gptb2(a,b,c):
	if a == 0:
		if b == 0:
			if c== 0:
				return "Pt vo so nghiem"
			else:
				return "Pt vo nghiem"
		else:
			return "Pt co 1 nghiem: " + str(-c/b)
	else:
		delta = b*b - 4*a*c
		if delta < 0:
			return "Pt vo nghiem"
		elif delta == 0:
			return "Pt co nghiem kep: " + str(-b/2/a)
		else:
			x1 = (-b + math.sqrt(delta)) / 2 /a
			x2 = (-b - math.sqrt(delta)) / 2 /a
			return "Pt co 2 nghiem: " + str(x1) + " " + str(x2)


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
	file = open("db", "a+")
	clientsocket,addr = serversocket.accept()      

	print("Got a connection from %s" % str(addr))
    
	msg='Connected To Server'+ "\r\n"
	clientsocket.send(msg.encode('ascii'))

	msg = clientsocket.recv(1024)
	data = msg.decode('ascii')

	msg = ""
	file.seek(0)
	while True:
		text = file.readline()
		if text == "":
			break
		if text.split("|")[0].strip() == data.strip() :
			print("Log in db")
			msg = text.split("|")[1].strip()
			break

	if msg == "":
		msg = gptb2(float(data.split(" ")[0]),float(data.split(" ")[1]),float(data.split(" ")[2]))
		file.write(data.strip() + "\t|\t" + msg + "\n")
	
	file.close()
	
	clientsocket.send(msg.encode('ascii'))
	clientsocket.close() 