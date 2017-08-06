 from sys import argv

script, filename = argv

txt = open(filename)

print "Hier is je file %s" % filename
print txt.read()
txt.close()

print "Enter in the filename again please"
file2 = raw_input(">>")

txtagain = open(file2)

print txtagain.read()
txtagain.close()

