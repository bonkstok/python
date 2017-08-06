import sys
import socket
import argparse
from threading import Timer
from time import sleep

def getCmdArg():
	parser = argparse.ArgumentParser()
	parser.add_argument("-p", "--port", help="Give a port to bind.", action="store", default=9000) 
	#port = 9000 if not args.port else args.port # if --port not supplied default is 9000.. <- alternative for default value. 
	parser.add_argument("-i", "--interface", help="Address to open a port on. Default = 127.0.0.1", dest="host", action="store", default="127.0.0.1")
	args = parser.parse_args()
	return args

def createSocket():
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
	except socket.error:
		print("FAILED TO CREATE SOCKET")
	return sock

def main():
	args = getCmdArg() # getting cmdline arguments from function
	port = int(args.port)
	host = args.host
	#now create a socket
	sock = createSocket()
	print(type(sock))
	#bind socket
	sock.bind((host,port))
	sock.listen(5)

	while True:
		conn , addr = sock.accept()
		print("Connected with {}:{}".format(addr[0],addr[1]))
		data = conn.recv(1024)
		print("Host sent data with size of {}".format(sys.getsizeof(data)))
		reply = "OK --> " + data.decode('ascii')
		if not data:
			break # if data is emplty.. no use of sending smth back
		conn.send(reply.encode('ascii'))
	sock.close()


if __name__ == '__main__':
	main()