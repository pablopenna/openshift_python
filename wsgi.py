"""
from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Welcome to the main page!"


@application.route("/<nombre>")
def greet(nombre):
	return "Hello there, "+nombre

if __name__ == "__main__":
    application.run()
"""
from flask import Flask, session, redirect, url_for, escape, request

application = Flask(__name__)
application.config['SECRET_KEY'] = 'ITSASECRET'

@application.route('/')
def index():
	if 'username' in session:
		username = session['username']
		return 'Logged in as ' + username + '<br>' + \
		"<b><a href = '/logout'>click here to log out</a></b>"
	else:
		print "test_index"
		return "You are not logged in <br><a href = '/login'></b>" + \
		"click here to log in</b></a>"


@application.route('/login', methods = ['GET', 'POST'])
def login():
	if request.method == 'POST':
		session['username'] = request.form['username']
		return redirect(url_for('index'))
	else:
		print "test_login"
		return '''

		<form action = "/login" method = "POST">
		<p><input type = "text" name = "username"/></p>
		<p><input type = "submit" value = "Login"/></p>
		</form>

		'''

@application.route('/logout')
def logout():
# remove the username from the session if it is there
	session.pop('username', None)
	return redirect(url_for('index'))



if __name__ == '__main__':
	#application.config["SECRET_KEY"] = "ITSASECRET"
	#application.run(port=5000,debug=True)
	#application.run(threaded=True)
	application.run()
	
