import socket
import time

def main():
	host = '127.0.0.1'
	port = 5000
	clients = []
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # create a udp socket
	#bind to server
	sock.bind((host,port))
	sock.setblocking(0) # doesnt wait for data, so you cna have multiple connections. 
	quitting = False
	print("Server started")

	while not quitting:
		try:
			data, addr = sock.recvfrom(1024) # recv para is byte size
			if "Quit" in str(data.decode('ascii')):
				quitting = True
			if addr not in clients:
				clients.append(addr)
			print(time.ctime(time.time()) + str(addr) + "::" + str(data))
			for client in clients:
				sock.sendto(data,client)

		except:
			pass # if there is nothing to catch, pass and try again

	sock.close()

if __name__ == '__main__':
	main()