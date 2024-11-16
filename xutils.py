from datetime import datetime as dt
import json
import streamlit as st
from xpipe import *


def getUsers(jsonpath="saved_users.json", username=None):
    with open(jsonpath) as f:
        users = json.load(f)

    if not username:
        return users
    return users[username][0]

def addNewUser(users, username, tweets, config_max_tweets, jsonpath="saved_users.json"):
    new_tweets = []
    for i in range(config_max_tweets):
        new_tweets.append({
            'date': tweets[i]['user_tweet_created_at'],
            'tweet': tweets[i]['user_tweet'],
            "class": predict(tweets[i]['user_tweet'])
        })
    users.update({username:new_tweets})
    with open(jsonpath, "w") as nf:
        json.dump(users, nf)

    return getUsers(jsonpath)

def getUsernames(users, depression_class=None):
    if not depression_class:
        return list(users.keys())
    return [user for user in users.keys() if users[user][0]['class'] == depression_class]

def getConfig(jsonpath="config.json"):
    with open(jsonpath) as f:
        configs = json.load(f)
    return configs

def ExtractCleanDate(datestr):
    return dt.strftime(dt.strptime(datestr, "%a %b %d %H:%M:%S +%f %Y"), "%d %b %Y %H:%M:%S")

def NumOfRegisteredUsers(users):
    return len(list(users.keys()))

def UserLastSeverityStatus(users, depression_class):
    return len([users[user][0]['class'] for user in users.keys() if users[user][0]['class'] == depression_class])

def UserInfoCards(users):
    return  {"Total": NumOfRegisteredUsers(users),
                "Mengkhawatirkan": UserLastSeverityStatus(users, 'mengkhawatirkan'),
                "Waspada": UserLastSeverityStatus(users, 'waspada'),
                "Normal": UserLastSeverityStatus(users, 'normal')
    }

if __name__ == "__main__":
    datestr = "Wed Nov 13 07:50:39 +0000 2024"
    print(ExtractCleanDate(datestr))