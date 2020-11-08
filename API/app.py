import flask
from flask import request

app = flask.Flask(__name__)

# Please restructure these into different files
class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)


@app.route('/')
def home():
    return 'well, you own it'

@app.route('/reddit')
def reddit():
    username = request.args.get('username')
    

if __name__=='__main__':
    app.run('localhost', port=1244, debug=True)
