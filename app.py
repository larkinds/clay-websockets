from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

# initial request handler
@app.route("/")
def home():
    return render_template("index.html")

@socketio.on('chat message')
def handle_message(data):
     socketio.emit("chat message", data)
# to learn: how to send a message to a particular group

# find out when this if statement is needed
if __name__ == '__main__':
    socketio.run(app)

