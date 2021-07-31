from flask import Flask, render_template, url_for 
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET KEY'] = 'NOYOU'
socketio = SocketIO(app)

@app.route('/')
def main():
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
