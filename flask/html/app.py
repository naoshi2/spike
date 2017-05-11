from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html', message="Home")

def getStr():
	return "haaaaaaaa"

@app.route("/hoge")
def hoge():
	lst = [1, 2, 3]
	message = getStr()
	return render_template('hoge.html', message=message, lst = lst)


if __name__ == "__main__":
	app.run()
