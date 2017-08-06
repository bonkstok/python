class Student:
	def __init__(self,name,school):
		self.name = name
		self.school = school
		self.marks = []

	def average(self):
		return sum(self.marks) / len(self.marks)

	def friend(self, friend_name):
		friend = Student(friend_name,self.school)
		return friend.name
	def appendMark(self,mark):
		self.marks.append(mark)

	@staticmethod
	def printClass():
		print("I'm the parent.")


class WorkingStudent(Student):
	def __init__(self,name,school,salary):
		super().__init__(name,school)
		self.salary = salary

	@property #getter
	def salary(self):
		print("hey getter")
		return self.__salary

	@salary.setter
	def salary(self, salary):
		print("hey setter")
		self.__salary = salary


#	@salary.deleter
#	def delSalary(self):
	#	print("Deleting the salary of:" + self.name)
	#	del self.__salary




stud = Student("Johnny", "KPN")
wstudent = WorkingStudent("Test", "KFC", 2500)
print(stud.friend("Jasper"))
wstudent.appendMark(10)
#wstudent.setSalary(1500)
#WorkingStudent.salary(500)
print(wstudent.salary)
wstudent.salary=500
print(wstudent.salary)
wstudent.printClass()
