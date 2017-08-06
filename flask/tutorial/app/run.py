from flask import Flask, render_template, redirect, url_for,request
from sys import argv
from forms import EmailPasswordForm



import functions

def main():
	test = "hoi"
	app = Flask(__name__)
	app.config.from_object('config')
	print(len(argv))
	@app.route('/template')
	def templatePrint():
		user = {'nickname' : 'bonkstok'}
		return render_template('index.html',title='template',user=user,message=functions.spam())

	@app.route('/login', methods=["GET","POST"])
	def login():
		form = EmailPasswordForm()
		if form:
			if request.form['email'] == "johnnyvanveen@hotmail.com":
				return redirect(url_for('template'))
			else:
				redirect("https://google.com", code=302)
			
		return render_template('login.html', form=form)

	@app.route('/test')
	def test():
		return "test..."
	app.run()
'''	if len(argv) != 1 and len(argv) < 3:
		if argv[1] == "debug":
			functions.createRoute(app)
			app.run(debug=True)
			print("Running")
	else:
		functions.createRoute(app)
		app.run(debug=False)
		print("Running")'''






	

if __name__ == '__main__':
	main()

