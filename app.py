import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
import streamlit_authenticator as stauth
from xtwitter import *
from xutils import *

last_tweets = 5
loading_gif = "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcGp6bGl0NHBqZjZ6dm1lZTg1a2JhZDlzaGptdHphdTBkNngwOHQ5ayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/gibvnAbdWQEiGtPlk3/giphy.webp"

with open('saved_users.json') as f:
    users = json.load(f)

st.set_page_config(page_title="Ceritakan", page_icon="ceritakan_favicon.png", layout="wide")
instr = 'Enter a Twitter Account (without @)'

with st.form('add_new_twitter_account'):
    # Create two columns; adjust the ratio to your liking
    col1, col2, col3 = st.columns([1,0.2,2]) 

    # Use the first column for text input
    with col1:
        xaccount = st.text_input(
            instr,
            placeholder=instr,
            label_visibility='collapsed'
        )
    # Use the second column for the submit button
    with col2:
        submitted = st.form_submit_button('Add')
    
    with col3:
        if xaccount and submitted:
            loading_placeholder = st.empty()
            with loading_placeholder:
                st.write("Loading...")
            tweets = CollectTweetsFromUser(xaccount, last_tweets=last_tweets)     
            
            
            
            if tweets:
                loading_placeholder.empty()
                with loading_placeholder:
                    st.markdown(f"<i>You have successfully added <b>@{xaccount}</b> to your watchlist", unsafe_allow_html=True)
                
                new_tweets = []
                for i in range(5):
                    new_tweets.append({
                        'date': tweets[i]['user_tweet_created_at'],
                        'tweet': tweets[i]['user_tweet']
                    })
                
                users.update({xaccount:new_tweets})
                with open("saved_users.json", "w") as nf:
                    json.dump(users, nf)
            else:
                loading_placeholder.empty()
                with loading_placeholder:
                    st.write("User not found")
 



col_acc_list, col_tweets = st.columns([1,4])
acc_buttons = []
tweets_placeholder = st.empty()

with col_acc_list:
    for user in users.keys():
        acc_buttons.append(st.button(f'@{user}'))

with col_tweets:
    for i in range(len(acc_buttons)):
        if acc_buttons[i]:
            username = list(users.keys())[i]
            user = users[username]
            st.write(f"Tweets of @{username}")
            tcols = st.columns(last_tweets)
            for j in range(len(tcols)):
                if j == len(user):
                    break
                with tcols[j]:
                    st.markdown("<b>"+ExtractCleanDate(user[j]['date']), unsafe_allow_html=True)
                    st.markdown("<i>"+user[j]['tweet'], unsafe_allow_html=True)
