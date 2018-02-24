from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Welcome to the main page!"


#@application.route("/<nombre>")
#def greet(nombre):
#	return "Hello there, "+nombre

if __name__ == "__main__":
    application.run()
