import streamlit as st
import streamlit.components.v1 as components
import json, altair, requests
import pandas as pd
from xtwitter import *
from xutils import *
from xpipe import *

configs = getConfig("config.json")
users = getUsers(configs['database'])

cards_info = UserInfoCards(users)
st.set_page_config(page_title=configs['page_title'], page_icon=configs['favicon'], layout="wide")

image_cols = st.columns([1,1])

with image_cols[0]:
    st.image("ceritakan_logo.png")
with image_cols[1]:
    st.markdown("<h2><br />Check on your <font color='red'>loved</font> ones.</h2>", unsafe_allow_html=True)

def createCards(cards_info):
    card_cols = st.columns(len(list(cards_info.keys())))
    for i, label in enumerate(cards_info.keys()):
        with card_cols[i]:
            st.metric(label, cards_info[label])

st.markdown("<h3>Rekapitulasi Pengguna Diawasi</h3>", unsafe_allow_html=True)
metric_placeholder = st.empty()
with metric_placeholder:
    createCards(cards_info)

st.markdown("<h3>Daftar Pengguna Diawasi</h3>", unsafe_allow_html=True)


# form add new twitter accounts
add_col1, add_col2, add_col3 = st.columns([1.5,0.4,2]) 

with add_col1:
    instr = 'Masukkan Akun X (tanpa ''@'')'
    xaccount = st.text_input(instr,placeholder=instr,label_visibility='collapsed')

with add_col2:
    add_button = st.button('', icon=':material/add:')

with add_col3:
    if xaccount and add_button:
        loading_placeholder = st.empty()
        with loading_placeholder:
            st.write("Loading...")
        tweets = CollectTweetsFromUser(xaccount, last_tweets=configs['num_of_extracted_tweets'])     
             
        
        if tweets:
            loading_placeholder.empty()
            with loading_placeholder:
                st.markdown(f"<i><b>@{xaccount}</b> berhasil ditambahkan", unsafe_allow_html=True)
            users = addNewUser(users, xaccount, tweets, configs['num_of_extracted_tweets'], configs['database'])
            cards_info = UserInfoCards(users)
            
            metric_placeholder.empty()
            with metric_placeholder:
                createCards(cards_info)
        else:
            loading_placeholder.empty()
            with loading_placeholder:
                st.markdown("<i>Pengguna X tidak ditemukan", unsafe_allow_html=True)

depressed_users = getUsernames(users, "mengkhawatirkan")
user_accounts = {}
num_users = NumOfRegisteredUsers(users)
default_cols_width = 0.5
user_cols_width = [default_cols_width for user in users.keys()] + [1.2*default_cols_width]
user_cols = st.columns(user_cols_width)
user_tabs = st.tabs([ "😰 "+"@"+user if user in depressed_users else "😊 "+"@"+user for user in list(users.keys())])

for i, user in enumerate(users.keys()):
    with user_tabs[i]:
        user_profil_cols = st.columns(1)
        user_alert_cols = st.columns(1)
        user_tweets = [tweet for tweet in users[user]]
        user_tab_cols = st.columns(len(user_tweets))

        depression_level_styles = {
            "mengkhawatirkan": "<font color='red' weight='bold'>",
            "waspada": "<font color='orange' weight='bold'>",
            "normal": "<font color='green' weight='bold'>",
        }    

        with user_profil_cols[0]:
            depression_level = user_tweets[0]['class']
            depression_contact_alert = f'''{depression_level_styles[depression_level]}Kontak Darurat! Hubungi <b>Hotline ID 119 Kemenkes</b> melalui:<br /> <a aria-label="Chat on WhatsApp" href="https://wa.me/6281380073120?text=Tolong%20saya.%20Kenalan%20saya%20menunjukkan%20gejala%20depresi%20yang%20mengkhawatirkan"> <img alt="Chat on WhatsApp" src="https://scontent.whatsapp.net/v/t39.8562-34/420077459_703742575180618_3955965302853713788_n.png?ccb=1-7&_nc_sid=73b08c&_nc_ohc=dTeAianoqhoQ7kNvgH7pwnN&_nc_zt=3&_nc_ht=scontent.whatsapp.net&_nc_gid=AyPs47dyfEKqkDR7U_spwSw&oh=01_Q5AaIDHpu5rpDOGcC18ZUEpP0bLSz0SmXlCAxIJi6exgk6y4&oe=673E08E8" width='100' /><a />''' if depression_level=='mengkhawatirkan' else ''''''
            st.markdown(f"{depression_contact_alert}",unsafe_allow_html=True)
            st.markdown(f"<h3>Distribusi Tingkat Depresi pada {configs['num_of_extracted_tweets']} Cuitan Terakhir</h3>", unsafe_allow_html=True)

        for i in range(len(user_tab_cols)):
            depression_level = user_tweets[i]['class']
            tweet = user_tweets[i]['tweet']
            tweet_date = ExtractCleanDate(user_tweets[i]['date'])

            with user_tab_cols[i]:
                st.markdown(f'''
                        <h3><small><font color='blue'>Tingkat Depresi: <br /> {depression_level_styles[depression_level]} {(depression_level).upper()} </small></h3><br />
                        ''',unsafe_allow_html=True)
                st.markdown(f"<h6><small><i>{tweet}</i></small></h6>",unsafe_allow_html=True)            
                st.markdown(f"<i><small>{tweet_date}</small></i>",unsafe_allow_html=True)

        


