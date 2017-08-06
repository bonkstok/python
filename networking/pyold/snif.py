import sys
import socket
import urllib2
import os
import platform

hostname  = socket.gethostname()
ip = socket.gethostbyname(hostname)
public_ip = urllib2.urlopen('http://ip.42.pl/raw').read()

print "You're currently using a " + platform.system() + " operating system."
print "Your current local IP is :	" + ip
print "Your current public IP is:	" + public_ip
print os.name


