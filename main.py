from flask_socketio import SocketIO
import flask
from waitress import serve

app = flask.Flask(__name__, static_folder = "static")

socketio = SocketIO(app)

users = {}

@app.route("/")
def root():
    return flask.render_template("index.html")

@socketio.on("connect")
def connect():
    userid = flask.request.sid

    users[userid] = {"x": 0, "y": 0}

    print(f"Client {userid} connected")

@socketio.on("mousemove")
def mousemove(data):
    userid = flask.request.sid

    users[userid]["x"] = data["x"]
    users[userid]["y"] = data["y"]

    socketio.emit("updatecursors", users)

@socketio.on("disconnect")
def disconnect():
    userid = flask.request.sid

    del users[userid]

    print(f"Client {userid} disconnected")

serve(app, host = "0.0.0.0", port = 8080, allow_unsafe_werkzeug = True)