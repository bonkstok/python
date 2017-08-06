import socket

s = socket.socket() #create socket object
host = socket.gethostname()
port = 12341

s.connect((host,port))
print s.recv(1024)
s.close()