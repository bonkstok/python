#classes
class LotteryPlayer():
	def __init__(self,name): #constructor
		self.name = name
		self.numbers = (5,2,1,2,4,50)

	def total(self):
		return sum(self.numbers)

	def getName(self):
		return self.name

	def setNumbers(self,numbers):
		self.numbers = numbers


def main():
	player = LotteryPlayer('Johnny')
	print("Player name: {}".format(player.getName()))
	print("Total sum of player {} numbers: {}".format(player.getName(),player.total()))
	#print(type(player.name))
	print("Sum of numbers before:",player.total())
	player.setNumbers((2,1,23,4,5,111,11))
	print("Sum of numbers after:",player.total())



if __name__ == '__main__':
	main()