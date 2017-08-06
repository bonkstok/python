#fruitful functions
def area(radius):
	b = 3.14159 * radius**2
	return b

def find_first_2_letter_word(*args):
	for wd in args:
		if len(wd) == 2:
			return wd
		return ""


print (find_first_2_letter_word(["is",  "is", "a", "dead", "parrot"]))
print (area(5))