# Sprint 02 - Group5
# starter
# streamlit run group5-sprint02.py --server.port 8502

# https://www.geeksforgeeks.org/a-beginners-guide-to-streamlit/


import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
import folium
from streamlit_folium import folium_static 
import warnings
warnings.filterwarnings('ignore')

import streamlit.components.v1 as components

## import
import notebooks.sprint_functions as sf

## spotify
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import time

## Extra configs
st.set_page_config(page_title="Music Streaming Analytics")
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
## End of Extra configs

## Modular pages
#import page_test
#page_test.hello()


# Example how to load Images
# pip install pillow
from PIL import Image
#image = Image.open('./images/sunrise.jpg.jpg')
#st.image(image, caption='Sunrise by the mountains', use_column_width=False, width=350)
# end of Image load example

###### DATA Loading
# Create the 6 data frames per csv file (Upload the CSV files first!)
# df_file = pd.read_csv("./data/file.csv")

######

## Pages as def functions

## Anyone wants a loadable setup? multiple pages?
## Modular pages
#import page_test
#page_test.hello()


## Site Wide Contents
### Main
#Oops Let's Do it Again")


### Side bars
st.sidebar.title("Oops Let's Do it Again")

## Radio
nav = st.sidebar.radio("Navigation ", 
               (
                    'Home', 
                    'Recommender System',
                    'Spotify dev'
               ))

### Dev
def page_dev():

    
    client_id='b50b238e07504b9fa981137104f61b24'
    client_secret='7a6fc994db03435b9728db16c06268db'
    redirect_uri='http://datadev.bullandbearcapital.com:8502/callback/'

    username = 'rob0nismydxooi7jxg95k19mp'
    scope_playlist = 'playlist-modify-public'
    scope_user = 'user-library-modify'

    #Credentials to access the Spotify Music Data
    manager = SpotifyClientCredentials(client_id,client_secret)
    sp = spotipy.Spotify(client_credentials_manager=manager)

    #Credentials to access the library  
    token_user= spotipy.util.prompt_for_user_token(username,scope_user,client_id,client_secret,redirect_uri) 
    sp_user = spotipy.Spotify(auth=token_user)

    #Credentials to access the playlists
    token_playlist= spotipy.util.prompt_for_user_token(username,scope_playlist,client_id,client_secret,redirect_uri) 
    sp_playlist = spotipy.Spotify(auth=token_playlist)
    
    ## Tracklist
    track_id_list = ['4pUCKHjJ4Ijewc37rRrvHn', '5troof8mcGO3AafoDbk1gc',
       '78qd8dvwea0Gosb6Fe6j3k', '0Wv6HtcBNex6lwPugykWCd',
       '7HzvvhTmfzvD1dV4F7MIcm', '5p10VwQ8LRoyTc8LFrvPw6',
       '1raaNykBg1bDnWENUiglUA', '017PF4Q3l4DBUiWoXk4OWT',
       '1ZEm9cJC05rawV2tptNfTS', '6aHCXTCkPiB4zgXKpB7BHS']
    
    ## create new playlist
    new_playlist_name = "Eskwelabs: DEV 1 Recommendations for seed track Kill This Love"    
    new_playlist = sp_playlist.user_playlist_create(username, name=new_playlist_name)
    new_playlist
    
    ## create
    playlist_id=new_playlist['id']
    sp_playlist.user_playlist_add_tracks(username, playlist_id, track_id_list)
    
### Pages
genre = []
def page_home():
    st.title("Home")
    st.markdown("""
## Our Client
""")
    image = Image.open('./images/SDC_2212108_2016-23-12--01-05-18.jpg')
    st.image(image, caption='', use_column_width=False, width=350)
    st.markdown("""
## Objectives
ldfslfs
    """)

def page_recommender():
    image = Image.open('./images/britney-spears-facebook-cover-timeline-banner-for-fb.jpg')
    st.image(image, caption='', use_column_width=False, width=640)
    st.title("Recommender System")
    feature_cols = ['danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 'instrumentalness',\
                'liveness', 'valence', 'tempo']
    
    action1 = st.sidebar.selectbox("Match: ", 
                           ['Track', 'Genre', 'Music'])
    if action1 == 'Track':
        tracks1 = st.sidebar.multiselect("Britney's Tracks:",
                                        [''])
        mult1 = st.sidebar.multiselect("Select Collaborator Genres: ",
                         ['Dancing', 'Reading', 'Sports'])
        st.sidebar.radio("Select Distance Algorithm",
                         ['Euclidian Distance Algorithm', 'Manhattan Distance Algorithm', 'Cosine Distance Algorithm'])
        
    elif action1 == 'Genre':
        tracks1 = st.sidebar.multiselect("Britney's Genres:",
                                        [''])
        mult1 = st.sidebar.multiselect("Select Collaborator Genres: ",
                         ['Dancing', 'Reading', 'Sports'])
        st.sidebar.radio("Select Distance Algorithm",
                         ['Euclidian Distance Algorithm', 'Manhattan Distance Algorithm', 'Cosine Distance Algorithm'])

    elif action1 == 'Music':
        model1 =  st.sidebar.selectbox("Select a Classifier: ",
                         ['k-Nearest Neighbor', 'Random Forest', 'XGBoost'])
        
        danceability = st.sidebar.slider("danceability", 0.0, 1.00, 0.01)
        energy = st.sidebar.slider("energy", 0.0, 1.00, 0.01)
        speechiness = st.sidebar.slider("speechiness", 0.0, 1.00, 0.01)
        acousticness = st.sidebar.slider("acousticness", 0.0, 1.00, 0.01)
        instrumentalness = st.sidebar.slider("instrumentalness", 0.0, 1.00, 0.01)
        liveness = st.sidebar.slider("liveness", 0.0, 1.00, 0.01)
        valence = st.sidebar.slider("valence", 0.0, 1.00, 0.01)
        tempo = st.sidebar.slider("tempo", 0.0, 1.00, 0.01)
        
        
    
### Page switching
if (nav == 'Home'):
    page_home()
elif (nav == 'Recommender System' ):
    page_recommender()
elif (nav == 'Spotify dev'):
    page_dev()


## Credits
st.sidebar.markdown("""
## The Team
- Beverly Lumbera
- Heide Mae Balcera
- Jay Silverio
- Renzo Luis Rodelas
- Rowen Remis R. Iral

*Eskwelabs Data Science Fellows Cohort 7*

*Mentored by Rods*
""")
