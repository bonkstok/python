import sys
import socket
import argparse
import socket_functions



def main():
	args = socket_functions.getCmdArg() # getting cmdline arguments from function
	port = int(args.port)
	host = args.host
	#now create a socket
	sock = socket_functions.createSocket()	
	#bind socket
	sock.bind((host,port))
	sock.listen(1)
	print("listening for connections....")
	c, addr = sock.accept()
	print("Got a connection from {}:{}".format(addr[0], addr[1]))
	while True:
		data = c.recv(1024)
		data = data.decode()
		if not data:
			break
		print("{} -> {}".format(addr[0],data))
		data = data.upper()
		c.send(data.encode('ascii'))
		c.send("\nThanks for your message. Bye.".encode('ascii'))
	c.close()	


if __name__ == '__main__':
	main()