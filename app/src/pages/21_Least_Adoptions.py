import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks
import requests
import pandas as pd
import altair as alt

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('Total Adoptions by Agency')

st.write('\n\n')
st.write('### Hi Alex, here you can see the agencies with the least adoptions.')

# Fetching the data from the api
data = {} 
try:
  data = requests.get('http://api:4000/a/petagencies').json()
except:
  st.write("Could not connect to database to retrieve agencies!")

df = pd.DataFrame(data)

# Sorting the data
st.write(
  alt.Chart(df).mark_bar(color='#89CFF0').encode(
    y=alt.Y('agencyName', axis=alt.Axis(title='Agency Name'), sort=None),
    x=alt.X('totalAdoptions', axis=alt.Axis(title='Number of Adoptions')),
    tooltip=['agencyName', 'totalAdoptions']
  ).properties(
    width=1100,
    height=800
   )
)