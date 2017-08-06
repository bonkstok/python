from sys import argv


script, filename = argv
text = []
print "we are going to truncate: %s " % filename
print "If you dont want to do that, press ctrl + c"
print "If you do want to delete this file, press enter "
raw_input("?")

	

print "Opening the file.."
target = open(filename, 'w')

print "Say goodbye to your files..."
target.truncate()
print "Now we need to type some lines into %s ," % filename
lines = int(raw_input("Tell me how many lines you would like to add to the file: "))
i = 0
for i in range (0, lines):
	text.append(raw_input("type lijn nummer %d hier: " % (i+1)))

for i in range (0, len(text)):
	target.write(text[i])
	target.write("\n")

target.close()
print text


