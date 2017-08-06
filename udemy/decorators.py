# is a function that gets called before another function 
import functools #function tools


#create your own decorator(func)
def my_dec(func): # when calling the decoratir, the function that calls is will be the argument
	@functools.wraps(func) #wrap something around the calling function
	def function_that_runs_func(): #what to do..
		print("I'm the decorator!")
		func() # run the function
		print("After the function...")
	return function_that_runs_func


@my_dec
def testing():
	print("Im the function")

testing()


print("############################")
#advanced decorators.

def my_dec_wargs(number):
	def my_dec(func):
		@functools.wraps(func)
		def function_that_runs_func():
			print("Im the decorator")
			func()
			print(number)
			print("Leaving the decorator...")
		return function_that_runs_func
	return my_dec

@my_dec_wargs(55)
def testArgs():
	print("Im the function")

testArgs()
