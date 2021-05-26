# Sprint 02 - Group5
# starter
# streamlit run group5-sprint02.py --server.port 8502

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

## Extra configs
st.set_page_config(page_title="Resource Allocation of SPED Schools in the Philippines")
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
import page_test
page_test.hello()


## Site Wide Contents
### Main
st.header("Spotify")


### Side bars
st.sidebar.title("Spotify")

### Page switching


## Credits
st.sidebar.markdown("""
## The Team
- Beverly Lumbera
- Heide Mae Balcera
- Jay Silverio
- Mark Mendoza
- Renzo Luis Rodelas
- Rowen Remis R. Iral

*Eskwelabs Data Science Fellows Cohort 7*

*Mentored by Rods*
""")