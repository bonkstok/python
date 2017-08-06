import socket
import sys

host = '' # all int
port = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'socket created'

try:
	s.bind((host,port))
except socket.error, msg:
	print str(msg[0]) + ' ' + msg[1]
	sys.exit("Programma zal sluiten")

print 'socket binding completed'

s.listen(10)
print 'listening mode [x]'
#accept connection
conn, addr = s.accept()

# client info
print addr

data = conn.recv(1024)
conn.sendall(data)
 
conn.close()
s.close()