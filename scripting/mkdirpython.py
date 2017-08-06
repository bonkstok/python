#demo how to copy a file using python
import shutil
import os

# source = os.listdir('/tmp/') # list all the dirs in /tmp/
# dest = "/tmp/testdir/"
# print(source)
# for files in source: # for every file in source..
# 	if files.endswith(".txt"):
# 		print("/tmp/"+files)
# 		print("Moving {} to {}..".format(files,dest))
# 		shutil.copy("/tmp/"+files,dest+files)
# 	else:
# 		print("Not a text file, skipping {}".format(files))


source = os.listdir('/tmp/') # list all the dirs in /tmp/
dest = "/tmp/testdir/"
print(source)
for files in source: # for every file in source..
	if files.endswith(".txt"):
		print("/tmp/"+files)
		print("Moving {} to {}..".format(files,dest))
		shutil.move("/tmp/"+files,dest+files)
	else:
		print("Not a text file, skipping {}".format(files))
