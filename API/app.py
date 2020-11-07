import flask
from flask import request

app = flask.Flask(__name__)

@app.route('/')
def home():
    return 'well, you own it'

@app.route('/reddit')
def reddit():
    username = request.args.get('username')
    

if __name__=='__main__':
    app.run('localhost', port=1244, debug=True)
