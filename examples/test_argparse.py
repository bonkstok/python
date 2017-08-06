import argparse

def main():
	parser = argparse.ArgumentParser()
	

	#required!
	#parser.add_argument("num", help="Testing bro")
	#parser.add_argument("second", help="Testing bro")
	
	#print(args)
	#print(args.num)
	parser.add_argument("-t", "--test", help="Add a argument ok", action="store") 
	# store_false/true   or store -> this will store the value given to --test or -test

	args = parser.parse_args()
	if args.test:
		print("test is set.")
		print(args.test)
	else:
		print("Test is not set.")
	print(args)
if __name__ == '__main__':
	main()