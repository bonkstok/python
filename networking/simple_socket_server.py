import socket
import time

#create a new socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# ^ create a new socket given address family, and type of protocol udp / tcp
#get local machine name
host = socket.gethostname()

#set port, if you use a port below 1024 you need to have root rights to execute.
port = 9999
print(host)
#bind socket to port
server_socket.bind((host, port))
#bin
#queue up to 5 requests
server_socket.listen(5)
# ^ starts to listen, and speicify how many connections can be queued.
while True:
	client_socket, addr = server_socket.accept()
	# ^ create a new socket usable to receive and send data on the connection. the address is the address bound to the socket on the other end of the connection
	# ^ at accept() a new socket is created that is distinct from the named socket. This new socket is used solely for communication with this client. 
	# ^ For tpc serves the socket object used to receive connections is not the same socket used to perform subsequent communication with the client
	# ^ In particular the accept() system call returns a new socket object that's actually used for the connection. This allows a server to manage connections from large number of clients at the same time.

	print("Got a connection from {}".format(addr))

	current_time = time.ctime(time.time()) + "\r\n"
	client_socket.send(current_time.encode('ascii'))
	client_socket.send("Hey test".encode('ascii')) #always encode your data.
	# ^ send data to the socket. the socket must be connected to a remote socket. Returns the number of bytes sent. Applications are responsible for checking that all data has been sent,
	# ^ if only some of the data has been sent, the application needs to attempt delivery of the remaining data. 
	client_socket.close()
	# ^ Close the socket and all further activity will fail.
