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
                    'Recommender System'
               ))
  
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
