from Reddit import scrape
from Twitter import twitter
from db import db

def initial_scrape(username):
    handles = db.get_social_handles(username)

    reddit_list = scrape.get_posts(handles['reddit'])
    twitter_list = twitter.get_all_tweets(handles['twitter'])

    # create a single list of all posts
    reddit_list.extend(twitter_list)

    # list of Social objects
    reddit_objs = [db.Social().dic_to_obj(post) for post in reddit_list]
    # convert to dict for posting
    posts = [post.to_dict() for post in reddit_objs]
    db.push_data(username, posts)