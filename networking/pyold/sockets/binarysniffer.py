import socket
import sys

host = 'sss' # all interfaces
port = 8888
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'socket created'

try:
	s.bind((host,port))
except socket.error as msg:
	print 'bind failed. Error code: ' + str(msg[0]) + ' Message ' + msg[1]
	sys.exit("Failed binding socket!")
print 'socket bind completed'
#start to listen on socket
s.listen(10)
print 'now listening to something'
while 1:
	conn, addr = s.accept()
	print 'connected with ' + addr[0] + ':' + str(addr[1])

s.close()
