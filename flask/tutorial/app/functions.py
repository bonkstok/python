def createRoute(app):
	route = input("Which route would you like to take: ")
	route = "/{}".format(route)
	print("Route",route)
	@app.route(route)
	def printText():
		return "Welcome to route {}".format(route)

def spam():
	return "This is just a fake spam"