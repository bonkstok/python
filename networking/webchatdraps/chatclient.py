import socket
import threading
import time

tLock = threading.Lock()
shutdown = False

def receiving(name, sock):
	while not shutdown:
		try:
			tLock.acquire()
			while True:
				data,addr = sock.recvfrom(1024)
				print(data.decode('ascii'))
		except:
			pass
		finally:
			tLock.release()

host = '127.0.0.1'
port = 0 # any free port on the computer

remote_server = ('127.0.0.1', 5000)# bind to remote server
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host,port))
sock.setblocking(0)

rT = threading.Thread(target=receiving, args=("RecvThread",sock))
rT.start()

alias = input("Name: ")
message = input(alias+ ">>")
while message != 'q':
	if message != '':
		message = alias + "::" + message
		sock.sendto(message.encode('ascii'), remote_server)
		tLock.acquire()
		message = input(alias+ ">>")
		tLock.release()
		time.sleep(0.2)

shutdown = True
rT.join()
sock.close()