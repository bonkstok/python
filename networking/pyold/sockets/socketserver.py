import socket
from random import randint
s = socket.socket() #create socket object.
host = socket.gethostname() #local machine
port = 12341 #randint(2000,3000) #random port
s.bind((host,port)) # bind to port

s.listen(5) # waiting for connection

while True:
	c, addr = s.accept() 
	print 'Connection received from:', addr
	c.send('Thank you for connecting')
	c.close()
s.close()
	