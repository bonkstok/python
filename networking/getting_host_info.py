import socket
from sys import argv
import argparse

parser = argparse.ArgumentParser(description='get-host')
parser.add_argument("-t", "--test", dest="host",help="Give a host to query.", action="store", default="www.google.nl")
parser.add_argument("-p", "--port", dest="port", help="Give port", action="store", default=80, type=int)
args = parser.parse_args()
#dest the value of dest will be how the value will be stored. without dest the variable name will be --test or -- port.
print(args)
host = args.host
port = args.port
try:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
	print("FAILED TO CREATE SOCKET")

#host = argv[1]
#port = 80
print(host)
print(args.port ,args.host)
try:
	remote_ip = socket.gethostbyname(host)
except:
	print("Could not resolve hostname")

print("IP address of {} is {}".format(host,remote_ip))

sock.connect((remote_ip, port)) #if the port is closed, the script will freeze for a bit. 

message = "GET / HTTP/1.1\r\n\r\n"
try: # sending data
	sock.send(message.encode('ascii'))
except socket.error:
	print("failed to send message.")
print("Message sent successfully.")

#receiving data..
reply_from_remote = sock.recv(4096)
print("Host {} replied with message:\n{}".format(host,reply_from_remote.decode('ascii')))



sock.close()