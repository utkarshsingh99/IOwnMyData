import flask
from flask import request, Response
from db import db
from . import utils
app = flask.Flask(__name__)



@app.route('/')
def home():
    return 'well, you own it'

@app.route('/reddit')
def reddit():
    username = request.args.get('username')

@app.route('register')
def register():
    name = request.args.get('name')
    email = request.args.get('email')
    reddit = request.args.get('reddit')
    twitter = request.args.get('twitter')

    user = db.User(name, email, reddit, twitter)
    db.create_user(user)
    return Response(200)

@app.route('fetch')
def fetch():
    email = request.args.get('email')
    utils.initial_scrape(email)
    return Response(200)

if __name__=='__main__':
    app.run('localhost', port=1244, debug=True)
