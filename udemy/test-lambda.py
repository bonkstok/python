from functools import reduce

def printLine(*args):
	if args:
		print("###{}###".format(args[0]))
	else:
		print("######")



#map
#map applies a function to all items in an input list:
#print("###MAP###")
printLine("MAP")
items = [1,2,3,4,5]
squared = list(map(lambda x: x**2, items))
print(squared)
printLine()
printLine("Filter")
#filter a list based on the result of a function
my_list = [13,56,77,484]
print(list(filter(lambda x: x != 13, my_list)))
degrees = [-1,-2,5,1,201,101,10,-500]
print(list(filter(lambda x: x < 100 and x > 1, degrees)))

printLine("")
printLine("Reduce")
#x,y rolls trhough a list and uses x,y values in a sequence. 
list = [1,2,3,4]
print(reduce((lambda x,y: x * y), [1,2,3,4]))





printLine()