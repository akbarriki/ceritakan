from xtwitter import *
from xutils import *
import json
from datetime import datetime as dt
import urllib.parse as uparse

# username = "gakbolehspill"
# tweets = CollectTweetsFromUser(username)
# print(tweets)

# new_tweets = []
# for i in range(5):
#     new_tweets.append({
#         'date': tweets[i]['user_tweet_created_at'],
#         'tweet': tweets[i]['user_tweet']
#     })

# print(new_tweets)
# new_dct = {username:new_tweets}



# with open("saved_users_test.json", "w") as nf:
#     json.dump(new_dct, nf)
# with open('saved_users.json') as f:
#     x = json.load(f)

# print(len([x[user][0]['class'] for user in x.keys() if x[user][0]['class'] == 'severe']))

string = "Tolong saya. Kenalan saya menunjukkan gejala depresi yang mengkhawatirkan."
print(uparse.quote(string))

# print(len(x))
# print(x['user1'][0]['date'])
# print(ExtractCleanDate(x['user1'][0]['date']))
# print(list(x.keys()))
