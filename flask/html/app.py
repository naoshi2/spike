from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html', message="Home")

@app.route("/hoge")
def hoge():
	lst = [1, 2, 3]
	return render_template('hoge.html', message="Hogeee", lst = lst)

if __name__ == "__main__":
	app.run()
