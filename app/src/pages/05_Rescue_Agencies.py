import logging
logger = logging.getLogger(__name__)
import streamlit as st
from streamlit_extras.app_logo import add_logo
import pandas as pd
import pydeck as pdk
from urllib.error import URLError
from modules.nav import SideBarLinks
import requests
import numpy
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

SideBarLinks()

# add the logo
add_logo("assets/logo.png", height=400)

# set up the page
st.markdown("# Pet Agencies Near 02284")

# You can access the session state to make a more customized/personalized app experience
st.write(f"### Hi, {st.session_state['first_name']}!")
st.write('This is a list of pets that are alive and available for adoption.')
agencies = requests.get('http://api:4000/a/agencies').json()
agencies_df = st.dataframe(agencies)

geocoder = Nominatim(user_agent="your_app_name")

zip_from = st.text_input(label = "zip: ")

def get_location(zip_code):
    location = geocoder.geocode(zip_code)
    return (location.latitude, location.longitude)

def find_distance_between(zip1, zip2):
    distance = geodesic(get_location(zip1), get_location(zip2)).miles
    return distance

def handleClick():
    df = pd.DataFrame(agencies)
    distances = []
    for index, row in df.iterrows():
        distances.append(find_distance_between(zip_from, row['zip']))
    df['distance'] = distances
    df.sort_values('distance')
    agencies_df = st.dataframe(df)

btn = st.button('next', key='next', on_click=handleClick)