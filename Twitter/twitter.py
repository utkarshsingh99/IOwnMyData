import tweepy #https://github.com/tweepy/tweepy
import os
#Twitter API credentials
# consumer_key = os.environ.get('consumer_key')
# consumer_secret = os.environ.get('consumer_secret')
# access_key = os.environ.get('access_key')
# access_secret = os.environ.get('access_secret')
consumer_key="LntJTC2OiMoQXO4Xn7lNVirUX"
consumer_secret="5yWB8ElG0C5KUoVX07N4BJgi9ShbqXjESJJiiS2RAHltIxCHEe"
access_key="1279593164-lwNko43Ln038BWAfaoBCYsRRKtm1o89K5tXN5Iy"
access_secret="0as8tHNkbHXCpaEo7kjdZAbmaF4JzGtDn8LlSk0yh80oj"
# bearer: AAAAAAAAAAAAAAAAAAAAAPsXJgEAAAAAw6dAjnqFG6egiPzT%2BAfC%2BVR5lhg%3D7gKXlqbkS2EKJ33ZqpY5bOv9uy7RFR8RuwgdpnRr7T35Xd9IG4

def get_all_tweets(screen_name):
    #Twitter only allows access to a users most recent 3240 tweets with this method
    
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    #initialize a list to hold all the tweepy Tweets
    alltweets = []  
    
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=200, tweet_mode='extended')
    #save most recent tweets
    alltweets.extend(new_tweets)
    
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    
    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print(f"getting tweets before {oldest}")
        
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
        
        #save most recent tweets
        alltweets.extend(new_tweets)
        
        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        
        print(f"...{len(alltweets)} tweets downloaded so far")
    
    data = []
    for tweet in alltweets:
        data.append({
            'title': '',
            'text': tweet.full_text,
            # 'media': tweet.entities['media'][0]['media_url'],
            'media': '',
            'url': tweet.source_url,
            'timestamp': tweet.id,
            'social': 'twitter',
            'favorites': tweet.favorite_count,
            'retweets': tweet.retweet_count,
            'socialid': tweet.id
        })
    print(alltweets[0].entities['media'][0]['media_url'])
    return data
    pass


if __name__ == '__main__':
	#pass in the username of the account you want to download
	get_all_tweets("ListenMrUtkarsh")