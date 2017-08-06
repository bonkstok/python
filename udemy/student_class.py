class Student:
	def __init__(self, name,school):
		self.name = name
		self.school = school
		self.marks = []

	def appendMark(self,mark):
		self.marks.append(mark)

	def getMarks(self):
		return self.marks

	def getName(self):
		return self.name

	def averageGrades(self):
		return sum(self.marks) / len(self.marks)

	def numberOfMarks(self):
		return len(self.marks)	

#class method
	@classmethod
	def classMeth(cls): #no need for self, as we don't return anything specific, but you need to add the cls argument
		print("Just chillin'")
#static method
	@staticmethod
	def staticMeth():
		print("Just staticin'")


def main():
	student1 = Student("Johnny", "KPN")
	student1.appendMark(55)
	student1.appendMark(10)
	print(student1.getMarks())
	print("Number of grades of {name}: {grades} \nWith an average of {average}".format(name=student1.getName(),grades=student1.numberOfMarks(),average=student1.averageGrades()))
	student1.classMeth()
	student1.staticMeth()




if __name__ == '__main__':
	main()
