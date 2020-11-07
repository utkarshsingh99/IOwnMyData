import praw
import os
CLIENT_ID = os.environ.get('client')
CLIENT_SECRET = os.environ.get('secret')

print(CLIENT_SECRET)

reddit = praw.Reddit(client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent="testscript by u/fakebot3123123"
)

def get_posts(username, last_id=None):
    data = []
    user = reddit.redditor(username)

    for post in yoptgyo.submissions.new(limit=5):
        data.append(
            {
                'title':post.title.encode('utf-8'),
                'text': post.selftext.encode('utf-8'),
                'media': post.url.encode('utf-8'),
                'url': f'https://reddit.com{post.permalink}',
                'timestamp': post.created_utc,
                'social':'reddit',
                'ups':post.ups
             }
            )
    return data
