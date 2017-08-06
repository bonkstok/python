import socket
import argparse
import socket_functions

def main():
	args = socket_functions.getCmdArg()
	sock = socket_functions.createSocketUDP()
	port = int(args.port)
	host = args.host
	sock.bind((host,port))
	print("Server started on ip {}:{}".format(host,port))
	#sock.listen(1) # doesnt work on udp
	while True:
		#sock.accept() doesnt work on udp
		data, addr = sock.recvfrom(1024) # first result is the data, second is the remote info
		#recvfrom recive data from socket. the return value is a pair (string,address)
		print(addr)
		print(data.decode('ascii'))
		data = "Thanks for connecting to my server."
		sock.sendto(data.encode('ascii'),addr) # send back to server. 
		#sendto (data to send, addr) # addr so it knows where ti send it to!
		# you can accept, listen or close a client socket.. Since you dont maintain a connection.
	sock.close()

if __name__ == '__main__':
	main()