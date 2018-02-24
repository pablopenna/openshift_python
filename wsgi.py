from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to the main page!"

"""
@app.route("/<nombre>")
def greet(nombre):
	return "Hello there, "+nombre
"""
if __name__ == "__main__":
    app.run()
