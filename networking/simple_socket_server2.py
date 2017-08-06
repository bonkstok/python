import socket
from sys import argv


port = argv
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ("127.0.0.1", port)
print("Starting server on ip {}:{}".format(server_address[0], server_address[-1]))
sock.bind(server_address)

#listen for incoming connections
sock.listen(1)
while True:
	client_socket, addr = sock.accept()
	#print(type(client_socket))
	print("Got a connection from {}".format(addr))
	msg = sock.recv(1024)
	print(msg.decode('ascii'))







#result of client_socket
#(<socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketType.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 5000), raddr=('127.0.0.1', 60612)>, ('127.0.0.1', 60612))
