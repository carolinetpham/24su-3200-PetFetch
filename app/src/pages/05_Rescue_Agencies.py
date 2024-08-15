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
import altair as alt

SideBarLinks()

# add the logo
add_logo("assets/logo.png", height=400)

# set up the page
st.markdown("# Find Pet Agencies Near You")

# You can access the session state to make a more customized/personalized app experience
st.write(f"### Hi, {st.session_state['first_name']}!")
st.write('This is a list of pet agencies that have pets available for adoption.')
agencies = requests.get('http://api:4000/a/agencies').json()
agencies_df = st.dataframe(agencies)

geocoder = Nominatim(user_agent="your_app_name")

zip_from = st.text_input(label = "Zip: ")

def get_location(zip_code):
    location = geocoder.geocode(zip_code)
    return (location.latitude, location.longitude)

def find_distance_between(zip1, zip2):
    distance = geodesic(get_location(zip1), get_location(zip2)).miles
    return distance

def handleClick():
    try: 
        df = pd.DataFrame(agencies)
        distances = []
        for index, row in df.iterrows():
            distances.append(find_distance_between(zip_from, row['zip']))
        df['distance'] = distances
        last_column = df.columns[-1]
        df = df[[last_column] + list(df.columns[:-1])]        
        st.session_state['agencies_df'] = df
    except:
        pass

btn = st.button('search', key='search', on_click=handleClick)

st.write(f"Agencies by distance from {zip_from}: ")

try: 
    st.dataframe(st.session_state['agencies_df'])
except:
    pass