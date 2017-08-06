import sys
import socket
import argparse


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

def createSocketUDP():
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
	except socket.error:
		print("FAILED TO CREATE SOCKET")
	return sock