from sys import argv
import datetime
#declare the necessary variables
text = []
script, filename = argv
target = None
lines = 0 

def fillFile2(bestand, line, txt):
	print "Now we are going to add some new text to %s" % bestand
	line = raw_input("Tell me how many lines of new text you would like to add: ")
	if line > 0:
		with open(bestand, 'w+') as f:
			i = 0
			for i in range (0, int(line)):
				txt.append(raw_input("Type lijn nummer %d hier: " % (i+1)))
			for i in range (len(txt)):
				if i < line:
					f.write((txt[i] + "\n"))
				elif (i + 1) == line:
					f.write((txt[i]))
			print "This is the new content of the file: "		
	else:
		print "no new lines were written."
	with open(bestand, 'r') as r:
		tek = r.read()
		print tek

		
def cleanFile(bestand):
	
	print "We are going to truncate the following file: %s " % bestand
	print "If you dont want this to happen, simply press ctrl + c."
	print "If you do want to truncate %s simply press enter." % bestand 
	raw_input("?")
	print "Opening the file %s" % bestand
	print "deleting content......"
	try:
		target = open(bestand, 'w')
		target.truncate()
		print "Completed"
		target.close
	except:
		print "File has not been found."

# def fillFile(bestand, line, txt): 
# 	openFile(bestand)
# 	print "Now we are going to add some new text to %s" % bestand
# 	line = raw_input("Tell me how many lines of new text you would like to add: ")
# 	i = 0
# 	for i in range (0, int(line)):
# 		txt.append(raw_input("Type lijn nummer %d hier: " % (i+1)))
# 	for i in range (len(txt)):
# 		target.write(txt[i])
# 	closeFile()

def main():
	time1 = datetime.datetime.now()
	cleanFile(filename)
	fillFile2(filename, lines, text)
	time2 = datetime.datetime.now()
	time = time2 - time1
	print "Script took %s to finish " % time

if __name__ == '__main__':
	main()

