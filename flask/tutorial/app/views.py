from init import app
#from flask import Flask
#test = Flask(__name__)

@app.route('/index')
def index():
	return "test"



#app.run(debug=True)