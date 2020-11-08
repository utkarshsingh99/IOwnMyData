# from mongoengine import *
# connect('users', host='mongodb+srv://admin:u7wWXx7KTONHiY5w@users.v9vdh.mongodb.net/users?retryWrites=true&w=majority')

conn_string = 'mongodb+srv://admin:u7wWXx7KTONHiY5w@users.v9vdh.mongodb.net/users?retryWrites=true&w=majority'

import pymongo

client = pymongo.MongoClient(conn_string)
user_db = client['users'].posts

class User:
    def __init__(self, name, email, reddit, twitter):
        self.name = name
        self.email = email
        self.username = email
        self.reddit = reddit
        self.twitter = twitter
    def to_dict(self):
        return {
            'name': self.name,
            'email': self.email,
            'username': self.username,
            'reddit': self.reddit,
            'twitter': self.twitter
        }
    def from_dict(self, dic):
        return User(
            dic['name'], dic['email'], dic['reddit'], dic['twitter']
        )

class Social:
    def __init__(self, title, text, media, url,
            timestamp, social, socialid, favorites=None,
            retweets=None, ups=None
            ):
            self.title = title
            self.text = text
            self.media = media
            self.url = url
            self.timestamp = timestamp
            self.social = social
            self.socialid = socialid
            self.favorites = favorites
            self.retweets = retweets
            self.ups = ups

    def dic_to_obj(self, dic):
        return Social(dic['title'], dic['text'], dic['media'], dic['url'], 
        dic['timestamp'], dic['social'], dic['socialid'], 
        dic.get('favorites'), dic.get('retweets'), dic.get('ups'))

    def to_dict(self):
        return {'title': self.title,
            'text': self.text,
            'media': self.media,
            'url': self.url,
            'timestamp': self.timestamp,
            'social': self.social,
            'favorites': self.favorites,
            'retweets': self.retweets,
            'socialid': self.socialid,
            'ups': self.ups
        }

# # Please restructure these into different files
# class User(Document):
#     email = StringField(required=True)
#     username = StringField(required=False)
#     first_name = StringField(max_length=50)
#     last_name = StringField(max_length=50)

def find_last_id(username, social):
    all_data = get_data(username, social)
    last_id = all_data0]['socialid']
    return last_id

def get_data(username, social):
    data = user_db.find_one({'user_id':user_id, 'social':social})


def push_data(username, data, social='reddit')