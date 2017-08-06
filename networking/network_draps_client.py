import socket
import argparse
import socket_functions

def main():
	args = socket_functions.getCmdArg()
	sock = socket_functions.createSocket()
	port = int(args.port)
	host = args.host

	#connect to server.
	sock.connect((host,port))

	message = input("-->")
	while message != 'q':
		sock.send(message.encode('ascii'))
		data = sock.recv(1024) # for wait return data
		print("message from server -> {}".format(data.decode('ascii')))
		message = input("-->")
	sock.close()
if __name__ == '__main__':
	main()