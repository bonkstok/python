import socket
import argparse
import socket_functions

def main():
	args = socket_functions.getCmdArg()
	sock = socket_functions.createSocketUDP()
	port = int(args.port)
	host = args.host
	remote_server = ('127.0.0.1',9000)
	sock.bind((host,port))

	print("Client started on ip {}:{}".format(host,port))
	#sock.listen(1) # doesnt work on udp
	message = input("-->")
	while message != 'q':
		#sock.accept() doesnt work on udp
		sock.sendto(message.encode('ascii'), remote_server)
		data, addr = sock.recvfrom(1024)
		print(data.decode('ascii'))
		message = input("-->")
	sock.close()
if __name__ == '__main__':
	main()