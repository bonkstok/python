from flask import Flask 

app = Flask(__name__) #special python variable, give each file a unique name. 

#which requests does this app need to serve / understand 
@app.route("/first")
@app.route("/also") #localhost/first, in programming this is called a 'route'
def first(): # name does not matter, only the route


def test():
	return "Hello."



app.run(port=8080,debug=True) #run on port 8080, if using ports > 1024 you need root priviliges!
#now go to http://localhost:8080/first

#old returns
	#return """<html><head><title>My first page</title></head>
	#		  <body> <h1>Hello, welcome to my first Flask page!</h1>
	#		  </body>
	#		  </html>
	#"""