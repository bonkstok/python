def my_method(arg1, arg2):
	return arg1+arg2

my_method(5,2)


def my_args(*args):
	return args


print(my_args(3,4,5,1,))

def my_args_sum(*args):
	return sum(args)

def my_kwargs(**kwargs):
	print(kwargs)
	for k,v in kwargs:
		print("Hello {}".format(v))

print(my_args_sum(10,10,10))

my_kwargs(name="Jose", location="Purmerend", naame="Henk", locaation="Boel")
