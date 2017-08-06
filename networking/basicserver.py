import sys
import socket
import argparse
from threading import Timer
from time import sleep


#create socket
try:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
	print("FAILED TO CREATE SOCKET")

sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # figure this out later ok.. ? This makes it reuse the port etc else oyu need to wait 
host = '192.168.242.156'
#host = socket.gethostname() #set hostname to current 
port = 8080
print(host)
#bind to server:
try:
	sock.bind((host,port)) # make sure to make a tuple from the input! else it will throw error 
except socket.error as msg:
	print(msg)

print("socket bind complete.")

#now we need to listen for incoming connections..
sock.listen(10)

print("Listening on {}:{}".format(host,port))


conn, addr = sock.accept()
#addr returns a tuple with the remote ip / port.
print("Received a connection from source {}:{}".format(addr[0],addr[1]))
data = conn.recv(1024)
print(data.decode('ascii'))
#msg = input("Wat wil je sturen?")
conn.send(input("Wat wil je naar de andere kant sturen:").encode('ascii')) # when sending data use the socket of the connected host.. not the socket created above!





#sleep(2) #waiting for 2 seconds..

# print("Closing connection.. ")
# sleep(2)
# sock.close()
# print("socket disconnected.")


# print("Closing connection")
# t = Timer(5.0, sock.close) # dont use function() but function   w/o any parentheses.. else you will get an error
