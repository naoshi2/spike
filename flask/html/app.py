from flask import Flask, render_template
from flask_sockets import Sockets

app = Flask(__name__)
sockets = Sockets(app)

@app.route("/")
def index():
	return render_template('index.html', message="Home")

def getStr():
	return "haaaaaaaa"

@app.route("/hoge")
def hoge():
	message = getStr()
	return render_template('hoge.html', message=message)

@sockets.route('/echo')
def echo_socket(ws):
    while True:
        message = ws.receive()
        ws.send(message)

if __name__ == "__main__":
	#app.run()
	from gevent import pywsgi
	from geventwebsocket.handler import WebSocketHandler
	server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
	server.serve_forever()
