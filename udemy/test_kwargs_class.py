class Student():
	def __init__(self,**kwargs):
		self.name = kwargs.pop('name')




student1 = Student(name="Johnny", school="HvA")
print(student1.name)