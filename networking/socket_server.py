import socket

try:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
	print("FAILED TO CREATE SOCKET")
