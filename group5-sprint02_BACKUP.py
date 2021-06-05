# Sprint 02 - Group5 (Group 4) (^_^)
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

import random


## Modeling imports
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.metrics import accuracy_score,roc_curve, auc, confusion_matrix, classification_report
from sklearn.metrics.pairwise import euclidean_distances, manhattan_distances, cosine_similarity

from sklearn.preprocessing import MinMaxScaler


## import external
import notebooks.sprint_functions as sf

## Spotify
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import time
from spotipy import oauth2

import requests

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

###### DATA and Modeling Functions
scalerMinmax = MinMaxScaler()
scaler = MinMaxScaler()

###### DATA Loading
# Create the 6 data frames per csv file (Upload the CSV files first!)
# df_file = pd.read_csv("./data/file.csv")

## DATA: britney_df
britney_df = pd.read_csv('notebooks/data/Britney Spears_playlist_tracks_data.csv')
#st.write(sf.explore_data(britney_df))
#st.dataframe(britney_df)
britney_df =britney_df.drop_duplicates(subset='track_id')
#st.write(sf.explore_data(britney_df))
#st.dataframe(britney_df)
britney_df = britney_df.dropna()
#st.dataframe(britney_df)

britney_df['loudness'] = scalerMinmax.fit_transform(britney_df[['loudness']])
britney_df['tempo'] =  scalerMinmax.fit_transform(britney_df[['tempo']])
#st.dataframe(britney_df)


## DATA: chart_tracks_df
chart_tracks_df = pd.read_csv("notebooks/data/spotify_daily_charts_tracks_predicted_genres.csv", encoding='utf-8')
#st.dataframe(chart_tracks_df)
chart_tracks_df['loudness'] = scaler.fit_transform(chart_tracks_df[['loudness']])
chart_tracks_df['tempo'] =  scaler.fit_transform(chart_tracks_df[['tempo']])





###### END OF DATA Laoding

###### Variables
## Spotify Credentials
username = ''
client_id=''
client_secret=''
redirect_uri='https://datadev.bullandbearcapital.com:8502/callback/'
scopes = ['playlist-modify-public','user-library-modify']
            
## Data Processing

#genre_names = ["Jazz", "Pop", "Reggae", "Classical", "Country"]
#genre_names2 = ["Jazz", "Pop", "Reggae", "Country"]
feature_cols = ['danceability', 'energy',\
       'loudness', 'speechiness', 'acousticness', 'instrumentalness',\
       'liveness', 'valence', 'tempo']

###### End of Variables

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

image = Image.open('./images/britney_black.jpg')
st.sidebar.image(image, caption='', use_column_width=False, width=290)

## Radio
nav = st.sidebar.radio("Navigation ", 
               (
                    'Home', 
                    'Presentation',
                    'Recommender System',
                    'Spotify Deploy'
               ))


## Functions
def generate_random_seedtracks(tracks, N):
    ids = list(tracks.keys())
    seed_tracks = (random.sample(ids, N))
    return {k:v*2 for (k,v) in tracks.items() if k in seed_tracks}

def load_data_pred():
    ## DATA: predictions_df
    predictions_df = pd.read_csv('notebooks/data/genre_predictions.csv')
    
    return predictions_df

    

token = None
### Dev
# https://stackoverflow.com/questions/49239516/spotipy-refreshing-a-token-with-authorization-code-flow
# https://stackoverflow.com/questions/25711711/spotipy-authorization-code-flow
def page_deploy(df):
    
    #st.dataframe(predictions_df)
    britney_df = df[df.artist_name == 'Britney Spears']
    #britney_df

    others_df = df[df.artist_name != 'Britney Spears']
    #others_df

    # EDA - Britney's genres
    bs_genres = list(britney_df.predicted_genre.unique())

    # EDA - Other Artists' genres
    other_genres = list(others_df.predicted_genre.unique())

    # Britney's average audio features by genre
    britney_genre_df = britney_df.groupby('predicted_genre').mean()[feature_cols].reset_index()
    #britney_genre_df
    
    reco =st.sidebar.selectbox('Recommendation',['Tracks'])
    
    bs_genre1 = st.sidebar.selectbox("Britney's Genre:",
                                        #["Jazz", "Pop", "Reggae", "Classical", "Country"])
                                         bs_genres #,bs_genres
                                        )
   
    
    if reco == 'Tracks':
        #st.write("Tracks -- path ******")
        st.header("Spotify Deployer")
        image = Image.open('./images/spotify_py.jpg')
        st.image(image, caption='', use_column_width=False, width=200)
        
       
        #btnRecommend = st.button("Recommend")
        
        #if btnRecommend:
            
        
        st.markdown("**Tracks**")
        
        reco_num = st.number_input('Top N',10,50)
        track_list_df = page_reco_genre(data, genre = bs_genre1, dist_algo='Cosine Distance Algorithm', n=reco_num)
        track_id_list = track_list_df['track_id']
        #track_id_list
        
        new_playlist_name = st.text_input('Enter Playlist name','PlaylistName')
        new_playlist_name = "Rod's Records - Eskewelabs DS Fellows: " + new_playlist_name

        btnCreatePlaylist = st.button("Create Playlist")

        st.markdown('''
    **NOTE:** *This recommended playlist will be submitted to Spotify and will be available to other Spotify subscribers.*

    *This can be used to, let say, recommend a Monthly Playlist / Seasonal Playlist of Britney's existing tracks to help her land a hitmaker position or improve her numbers in terms of streams.*
                ''')

        token_info = None
        if btnCreatePlaylist:

            sp_oauth = oauth2.SpotifyOAuth(client_id=client_id,client_secret=client_secret,redirect_uri=redirect_uri,scope=scopes)
            #token_info = sp_oauth.get_cached_token() 
            if not token_info:
                #auth_url = sp_oauth.get_authorize_url(show_dialog=True)
                auth_url = sp_oauth.get_authorize_url()
                #st.write(auth_url)

                req1 = requests.get(auth_url)
                #st.write(req1)
                #st.write(req1.content)

                response = req1.content
                #st.write(response)

                #response = input('Paste the above link into your browser, then paste the redirect url here: ')

                code = sp_oauth.parse_response_code(response)
                token_info = sp_oauth.get_access_token(code)

                token = token_info['access_token']
            else:
                token = token_info['access_token']

            sp = spotipy.Spotify(auth=token)
            #st.text(token)


                    #
                    ## Tracklist
                #track_id_list = ['4pUCKHjJ4Ijewc37rRrvHn', '5troof8mcGO3AafoDbk1gc',
                #       '78qd8dvwea0Gosb6Fe6j3k', '0Wv6HtcBNex6lwPugykWCd',
                #       '7HzvvhTmfzvD1dV4F7MIcm', '5p10VwQ8LRoyTc8LFrvPw6',
                #       '1raaNykBg1bDnWENUiglUA', '017PF4Q3l4DBUiWoXk4OWT',
                #       '1ZEm9cJC05rawV2tptNfTS', '6aHCXTCkPiB4zgXKpB7BHS']

            recommender_tid_list = []
            
            
            ## create new playlist
            #new_playlist_name = "Eskwelabs: DEV 2 Recommendations for seed track Kill This Love"    
            new_playlist = sp.user_playlist_create(username, name=new_playlist_name)
            #new_playlist    
            ## create
            playlist_id=new_playlist['id']
            sp.user_playlist_add_tracks(username, playlist_id, track_id_list)

            playlists = sp.user_playlists(username)
            
            my_playlist = []
            for playlist in playlists['items']:
                my_playlist.append(playlist['name'])
            #new_playlist
            st.success("Success: " + my_playlist[0] + " created.")
            st.info("♫ 🎧 Click now to Open Playlist: " + playlists['items'][0]["external_urls"]["spotify"])
            st.subheader("My Playlists")
            my_playlist
            
    
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

- Find out Britney Genres
- Advise Britney how she can remain as a Hitmaker on this streaming era
- Get list of Collaborators and Competitors
- Produce Recommended Spotify Playlist
    """)

def page_prezi():
    components.html(
        '<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vRKOq8B3eOumWnBnhbi6MtyoRIKb89M3diXI5VAtKu-i79B2909RrHGnhcvOzXu4EIWNUrkPTIKj-W6/embed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>' 
            ,height=920, width=1630)

def page_reco_track(df, genre):
#def page_reco_track(df):
    
    #st.dataframe(predictions_df)
    britney_df = df[df.artist_name == 'Britney Spears']
    #britney_df

    others_df = df[df.artist_name != 'Britney Spears']
    #others_df

    # EDA - Britney's genres
    bs_genres = list(britney_df.predicted_genre.unique())

    # EDA - Other Artists' genres
    other_genres = list(others_df.predicted_genre.unique())
    
    tracks = britney_df[(britney_df['predicted_genre']==genre)][['track_id', 'track_name']].set_index('track_id').to_dict()['track_name']
    #tracks = britney_df[['track_id', 'track_name']].set_index('track_id').to_dict()['track_name']
    st.dataframe(pd.DataFrame(list(tracks.items()), columns=['track_id','track_name']))
    
    seeds = generate_random_seedtracks(tracks, 3)
    seed_track_ids = list(seeds.keys())
    seedtracks = britney_df[britney_df.track_id.isin(seed_track_ids)].mean()
    
    reco_df = others_df.copy()
    
    reco_df['euclidean_dist'] = others_df.apply(lambda x: euclidean_distances(x[feature_cols].values.reshape(-1, 1), seedtracks[feature_cols].values.reshape(-1, 1)).flatten()[0], axis=1)
    reco_df['manhattan_dist'] = others_df.apply(lambda x: manhattan_distances(x[feature_cols].values.reshape(-1, 1), seedtracks[feature_cols].values.reshape(-1, 1)).flatten()[0], axis=1)
    reco_df['cosine_dist'] = others_df.apply(lambda x: 1-cosine_similarity(x[feature_cols].values.reshape(1, -1), seedtracks[feature_cols].values.reshape(1, -1)).flatten()[0], axis=1)

    # Top 10 recommendations by `cosine similarity`
    reco_df = reco_df.sort_values('cosine_dist', ascending=False).head(10).reset_index()
    
    st.text("Recommended Tracks")
    reco_df
    #return recodf

def page_reco_genre(df, genre, dist_algo, n):
    '''
    df: data
    genre: genre
    dist_algo: Distance algo name
    n: number of result
    '''
    # Data load csv
    britney_df = df[df.artist_name == 'Britney Spears']
    others_df = df[df.artist_name != 'Britney Spears']
    
    # EDA - Britney's genres
    bs_genres = list(britney_df.predicted_genre.unique())

    # EDA - Other Artists' genres
    other_genres = list(others_df.predicted_genre.unique())
    
    # Britney's average audio features by genre
    britney_genre_df = britney_df.groupby('predicted_genre').mean()[feature_cols].reset_index()
    #britney_genre_df

    # Compute distance/similarity by `COUNTRY` genre
    seedtrack_genre = britney_genre_df[britney_genre_df.predicted_genre == genre]

    reco_df = others_df.copy()
    retdf = []
    if dist_algo == 'Cosine Distance Algorithm':
        reco_df['cosine_dist'] = others_df.apply(lambda x: 1-cosine_similarity(x[feature_cols].values.reshape(1, -1), seedtrack_genre[feature_cols].values.reshape(1, -1)).flatten()[0], axis=1)
        reco_top_10 = reco_df.sort_values('cosine_dist', ascending=False).head(n).reset_index()
        st.write('Recommended')
        st.dataframe(reco_top_10)
        retdf = reco_top_10
        
    elif dist_algo == 'Euclidian Distance Algorithm':
        reco_df['euclidean_dist'] = others_df.apply(lambda x: euclidean_distances(x[feature_cols].values.reshape(-1, 1), seedtrack_genre[feature_cols].values.reshape(-1, 1)).flatten()[0], axis=1)
        reco_top_10 = reco_df.sort_values('euclidean_dist', ascending=False).head(n).reset_index()
        st.write('Recommended')
        st.dataframe(reco_top_10)
        retdf = reco_top_10
        
    elif dist_algo == 'Manhattan Distance Algorithm':
        reco_df['manhattan_dist'] = others_df.apply(lambda x: manhattan_distances(x[feature_cols].values.reshape(-1, 1), seedtrack_genre[feature_cols].values.reshape(-1, 1)).flatten()[0], axis=1)
        reco_top_10 = reco_df.sort_values('manhattan_dist', ascending=False).head(n).reset_index()
        st.write('Recommended')
        st.dataframe(reco_top_10)
        retdf = reco_top_10
        
    return retdf
    
def page_reco_music(df):
    pass

def page_recommender(df):
    
    #st.dataframe(predictions_df)
    britney_df = df[df.artist_name == 'Britney Spears']
    #britney_df

    others_df = df[df.artist_name != 'Britney Spears']
    #others_df

    # EDA - Britney's genres
    bs_genres = list(britney_df.predicted_genre.unique())

    # EDA - Other Artists' genres
    other_genres = list(others_df.predicted_genre.unique())
    
    # Britney's average audio features by genre
    britney_genre_df = britney_df.groupby('predicted_genre').mean()[feature_cols].reset_index()
    #britney_genre_df
    
    image = Image.open('./images/britney-spears-facebook-cover-timeline-banner-for-fb.jpg')
    st.image(image, caption='', use_column_width=False, width=640)
    st.title("Recommender System")

    
    action1 = st.sidebar.selectbox("Match: ", 
                           [
                               'Track', 
                               'Genre', 
                           #    'Music'
                           ])
    if action1 == 'Track':
        bs_genre1 = st.sidebar.selectbox("Britney's Tracks:",
                                        #["Jazz", "Pop", "Reggae", "Classical", "Country"])
                                         bs_genres #,bs_genres
                                        )
        #st.sidebar.write("For Collaboration")
        #other_genre1 = st.sidebar.multiselect("Select Collaborator Tracks: ",
        #                                    other_genres#,other_genres
        #                                  )
        distance_algo = st.sidebar.radio("Select Distance Algorithm",
                         ['Euclidian Distance Algorithm', 'Manhattan Distance Algorithm', 'Cosine Distance Algorithm'])
        
        #page_reco_genre(data, bs_genre1, distance_algo, 10)
        
        page_reco_track(data, bs_genre1)
        #page_reco_track(data)
        

    elif action1 == 'Genre':
        bs_genre1 = st.sidebar.selectbox("Britney's Genre:",
                                        #["Jazz", "Pop", "Reggae", "Classical", "Country"])
                                         bs_genres #,bs_genres
                                        )
        #st.sidebar.write("For Collaboration")
        #other_genre1 = st.sidebar.multiselect("Select Collaborator Genres: ",
        #                                    other_genres#,other_genres
        #                                  )
        distance_algo = st.sidebar.radio("Select Distance Algorithm",
                         ['Euclidian Distance Algorithm', 'Manhattan Distance Algorithm', 'Cosine Distance Algorithm'])
        
        page_reco_genre(data, bs_genre1, distance_algo, 50)
            
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
data = load_data_pred()

if (nav == 'Home'):
    page_home()
elif (nav == 'Presentation'):
    page_prezi()
elif (nav == 'Recommender System' ):
    page_recommender(data)
elif (nav == 'Spotify Deploy'):
    page_deploy(data)


## Credits
st.sidebar.markdown("""
## The Team
- Beverly Lumbera
- Heide Mae Balcera
- Jay Silverio
- Renzo Luis Rodelas
- Rowen Remis R. Iral

*Eskwelabs Data Science Fellows Cohort 7*

*Mentored by Rodel "Rods" Arenas*
""")
