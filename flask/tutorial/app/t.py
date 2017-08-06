from test import x, app

print(x)
@app.route('/route')
def route():
	return "test"

app.run()