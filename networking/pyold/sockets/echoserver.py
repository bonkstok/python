import socket
import sys

#create tcp socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#now bind is used to bind the port and server address (localhost)
server_address = ('localhost', 10000)
sock.bind(server_address)
#using listen() puts the socket in server mode and accept waits for an incoming connection
sock.listen(1)
while True:
	#wait for connection
	print >>sys.stderr, 'waiting for a connection'
	connection, client_address = sock.accept()


try:
    print >>sys.stderr, 'connection from', client_address

        # Receive the data in small chunks and retransmit it
    while True:
        data = connection.recv(8)
        print >>sys.stderr, 'received "%s"' % data
        if data:
            print >>sys.stderr, 'sending data back to the client'
            connection.sendall(data)
        else:
            print >>sys.stderr, 'no more data from', client_address
            break
            
finally:
        # Clean up the connection
    connection.close()