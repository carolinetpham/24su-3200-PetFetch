import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks
import requests
import pandas as pd 
from datetime import datetime


st.set_page_config(layout = 'wide')

SideBarLinks()
st.title('Pet Stay Time')

st.write('\n\n')
st.write("### Hi Alex, here are pets that haven't been adopted")

# Fetching the data from the api
data = {} 
date = st.date_input(
    "Show Pets After This Date:",
     value=datetime(2020,1,1),
     max_value = datetime(2024,1,1),
)
if date:
    data = requests.get(f'http://api:4000/p/pets/date/{date}').json()
    st.dataframe(data)
    




