import socket

#create a new socket object
socket_object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine hostname..
host = socket.gethostname()

port = input("please enter the port number:")

#connect to server
socket_object.connect(("127.0.0.1",port))
# can also use an ip addres isntead of host..

#recieve no more than 1024 bytes of data
#tm = socket_object.recv(1024) # receives whatever the server sends..
#socket_object.send("hey daar".encode('ascii'))
socket_object.close()

#print(tm.decode)
#print(type(tm.decode('ascii')))
#print("Data received: {}".format(tm.decode('ascii'))) # always decode your data
