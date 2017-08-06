import sys
import socket
import urllib2
import os
import platform
from struct import *
import datetime
today = datetime.datetime.now()
tday= str(today.year) + '-' + str(today.month) + '-' + str(today.day) + '-' + str(today.hour) +'-' +  str(today.minute)
dict1 = {}
dict2 = {}
target = open(str(tday+'.txt'), 'w+')
try:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
	print 'err code: ' + str(msg[0]) + 'err message: ' + msg[1]
 	sys.exit();

def printMenu():
	file:///home/jj/Desktop/sqlitestudio
	print "3. If you would like to run a portscan.\n"
	print "4. If you would like to use our Packet Sniffer.\n"
	print "5. If you feel lonelcy, you can use our useless chat function\n"
	print "6. Press Q if you would like to quit.\n"
	try:
		keuze = int(raw_input(">>> "))
		return keuze
	except ValueError:
		"Please use numbers![1:6] and no letters!"
	#keus = printMenu()
	#selection = 0
def main():
	while True:
		keus = int(printMenu())
		

		
		if keus > 0 and keus < 7:

			if keus == 1: 
				hostname  = socket.gethostname()
				ip = socket.gethostbyname(hostname)
				public_ip = urllib2.urlopen('http://ip.42.pl/raw').read()
				print "You're currently using a " + platform.system() + " operating system."
				print "Your current local IP is :	" + ip
				print "Your current public IP is:	" + public_ip
				print os.name
			elif keus == 2:
				print "Which host would you like to contact?"
				host = raw_input("Please use the format www.name.tld\n-> ")
				port = 80
				try:
					remote_ip = socket.gethostbyname(host)
					print "The ip address of %s is: %s " % (host, remote_ip)
				except socket. gaierror:
						#could not resolve
					print 'hostname could not be resolved, exiting'
				
					
				try:#connect to remote server
					sock.connect((remote_ip, port))
				except ValueError:
					"You entered a wrong address. Please use www.name.domain. EQ. www.google"#send some stuff to remote
				message = "GET / HTTP/1.1\r\n\r\n"
				try:
						#send the message
					sock.sendall(message)
				except socket.error:
					print "send failed"
					break
				print "Message is sent."
					#fetch data
				reply = sock.recv(4096)
				print reply
					#when done with socket, close it.
				sock.close()
			elif keus == 4:
				try:
					s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
    				
				except socket.error , msg:
					print 'Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    				#sys.exit()
    				
 
				# receive a packet
				while True:
				    packet = s.recvfrom(65565)
				     
				    #packet string from tuple
				    packet = packet[0]
				     
				    #take first 20 characters for the ip header
				    ip_header = packet[0:20]
				     
				    #now unpack them :)
				    iph = unpack('!BBHHHBBH4s4s' , ip_header)
				     
				    version_ihl = iph[0]
				    version = version_ihl >> 4
				    ihl = version_ihl & 0xF
				     
				    iph_length = ihl * 4
				     
				    ttl = iph[5]
				    protocol = iph[6]
				    s_addr = socket.inet_ntoa(iph[8]);
				    d_addr = socket.inet_ntoa(iph[9]);
				     
				    print 'Version : ' + str(version) + ' IP Header Length : ' + str(ihl) + ' TTL : ' + str(ttl) + ' Protocol : ' + str(protocol) + ' Source Address : ' + str(s_addr) + ' Destination Address : ' + str(d_addr)
				    dict1.update({'Version' : str(version), 'IP Header Length' : str(ihl), 'TTL' : str(ttl), 'protocol' : str(protocol), 'Source Address' : str(s_addr), 'Destination Address' : str(d_addr)})
				    cont = 0 
				    for k, v in dict1.iteritems():
				        if cont == 5:
				            target.write(k + ' > ' + v + '\n')
				            cont = cont + 1
				        else:
				            target.write(k + ' > ' + v + ' ')
				            cont = cont + 1
				     
				    tcp_header = packet[iph_length:iph_length+20]
				     
				    #now unpack them :)
				    tcph = unpack('!HHLLBBHHH' , tcp_header)
				     
				    source_port = tcph[0]
				    dest_port = tcph[1]
				    sequence = tcph[2]
				    acknowledgement = tcph[3]
				    doff_reserved = tcph[4]
				    tcph_length = doff_reserved >> 4
				     
				    print 'Source Port : ' + str(source_port) + ' Dest Port : ' + str(dest_port) + ' Sequence Number : ' + str(sequence) + ' Acknowledgement : ' + str(acknowledgement) + ' TCP header length : ' + str(tcph_length)
				     
				    h_size = iph_length + tcph_length * 4
				    data_size = len(packet) - h_size
				     
				    #get data from the packet
				    data = packet[h_size:]
				     
				    print 'Data : ' + data
				    print

			elif keus == 6:
					sys.exit()
		else:
			print "Please enter a number between 1-6"
		
if __name__ == '__main__':
	main()
