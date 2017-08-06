import socket
import sys

# try:
# 	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# except  socket.error, msg:
# 	print 'failed to create socket. Errorcode: ' + str(msg[0]) +', Errormessage: ' + msg[1]
# 	sys.exit()

# print 'socket created

try:
	# create socket tcp
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
	print 'failed to create socket. Code: ' + str(msg[0]) + 'Errormessage: ' + msg[1]
	sys.exit()

print 'socket created'

host = 'www.google.nl'
port = 80
try:
	remote_ip = socket.gethostbyname(host)

except socket.gaierror:
	#could now resolve
	print 'host name could not be resolved. Exiting'
	sys.exit()

print 'The ip address of ' + host + ' is ' + remote_ip

#connect to remote server
s.connect((remote_ip , port))

print 'socket connected to:' + host + '\non ip:' + remote_ip + ' on port:' + str(port)

#send data to server
message = "GET / HTTP/1.1\r\n\r\n"

try:
	#send whole string
	s.sendall(message)
except socket.error:
	print 'send failed'
	sys.exit()

print 'message sent succesfully'

#receive 
reply = s.recv(4096)
print reply

#close the socket.
s.close()