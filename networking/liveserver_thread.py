import sys
import socket
import argparse
from threading import Timer
from time import sleep
import threading

q = "q"
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

def clientThread(conn,addr):
	conn.send("Welcome to {}. Try chatting with me.\n".encode('utf-8'))
	while True:
		data = conn.recv(1024) # receiving the reply from the client
		data = data.decode('utf-8')
		print(type(q))
		if data == q:
			print("Closing connection")
			conn.close()
		else:
			print("continue//")
			#print(addr[0],"->" , data.decode('utf-8')) # printing the reply from the client
			print(addr[0],"->" , data) # printing the reply from the client
			msg = input()
			msg = msg[:0] + "192.168.242.156 -> " + msg + "\n"
			conn.send(msg.encode('utf-8'))
		# reply = "OK -> " + data.decode('ascii') # send data back to the client, echo echo.
		# if not data:
		# 	break
		# conn.send(reply.encode('ascii'))
	conn.close()


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
	print("start")
	while True:
		conn, addr = sock.accept()
		#sock.send("Welcome to my server. ")
		print("Received a connection from {}:{}".format(addr[0],addr[1]))
		t = threading.Thread(target=clientThread, args=(conn, addr)) # create a thread, target a function  and supply the agruments! remember it takes a tuple as an argument!
		t.start() # start the threading baby
	sock.close()	










	# while True:
	# 	conn , addr = sock.accept()
	# 	print("Connected with {}:{}".format(addr[0],addr[1]))
	# 	data = conn.recv(1024)
	# 	print("Host sent data with size of {}".format(sys.getsizeof(data)))
	# 	reply = "OK --> " + data.decode('ascii')
	# 	if not data:
	# 		break # if data is emplty.. no use of sending smth back
	# 	conn.send(reply.encode('ascii'))
	# sock.close()


if __name__ == '__main__':
	main()