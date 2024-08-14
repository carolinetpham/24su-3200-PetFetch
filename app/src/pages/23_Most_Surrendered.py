import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks
import requests
import pandas as pd
import altair as alt

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('Most commonly surrendered pets')

st.write('\n\n')
st.write('### Hi Alex, here you can see the animal breeds that are surrendered to resuces the most.')
st.write('\n\n')
st.write('#### View breeds by species')

# Fetching the data from the api
data = {} 
try:
  data = requests.get('http://api:4000/a/mostsurrendered').json()
except:
  st.write("Could not connect to database to retrieve agencies!")

df = pd.DataFrame(data)

st.bar_chart(df, x="species", y="amount_surrendered", x_label="Species", y_label="Amount Surrendered", color="breed", width=1000, stack=False, use_container_width=False)

st.write('\n\n')
st.write('#### View breeds')

# Create the chart with explicitly specified data types
chart = alt.Chart(df).mark_bar().encode(
    x=alt.X('amount_surrendered', axis=alt.Axis(title='Amount Surrendered')),
    y=alt.Y('breed', axis=alt.Axis(title='Breed')),
    tooltip=[
        alt.Tooltip('breed', title='Breed'),
        alt.Tooltip('amount_surrendered', title='Amount Surrendered')
    ]
).properties(
    width=1100,
    height=800
)

st.write(chart)