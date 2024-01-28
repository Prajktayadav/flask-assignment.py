import sqlite3
from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/', methods=['GET'])
def index():
    render_template('index.html')

@app.route('/listen/<data>',methods=['POST'])
def listen(data):
    conn = sqlite3.connect('storage.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE info(num text)''')
    c.execute('''INSERT INTO info(num) VALUES(?)''',(data))
    conn.commit()
    conn.close()


@socketio.on('message')
def handle_message(message):
    send(message)

if __name__ == '__main__':
    socketio.run(app)