import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:
	message = 'This is the message. It will be repeatedThis is the message. It will be repeatedThis is the message. It will be repeated'

	print 'sending "%s"' % message
	sock.sendall(message)

	#look for response
	amount_received = 0
	amount_expected = len(message)

	while amount_received < amount_expected:
		data = sock.recv(8)
		amount_received += len(data)
		print 'received "%s"' % data

finally:
	print 'closing socket'
	sock.close()