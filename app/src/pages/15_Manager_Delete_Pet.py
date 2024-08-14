import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks
import pandas as pd
SideBarLinks()

st.write("# Delete a Pet from the Database")

# Using HTML in st.markdown to style the text
st.markdown("<div style='color: indianred; font-size: 20px;'> \
<strong>WARNING: Once you delete a pet, you cannot recover the data.<strong></div>", unsafe_allow_html=True)

# Fetch the list of petIDs from the API
response = requests.get('http://api:4000/p/pets')
pets = response.json()

# Create a DataFrame from the pets data
df = pd.DataFrame(pets)

# Rearrange the columns
df = df[['petID', 'name', 'adoption_status', 'species', 'breed', 'birthday', 'age', 'is_alive']]

# Display the DataFrame
st.dataframe(df)

# Extract the petIDs from the response
pet_ids = [pet['petID'] for pet in pets]

# Create a select box for petID
selected_pet_id = st.selectbox('Select Pet ID to delete:', pet_ids)

# This is a workaround to get a session state
if 'delete' not in st.session_state:
    st.session_state.delete = False

if 'confirm' not in st.session_state:
    st.session_state.confirm = False

if st.button('Delete Pet'):
    st.session_state.delete = True

if st.session_state.delete:
    st.write('Are you sure you want to delete this pet?')

    if st.button('Yes'):
        st.session_state.confirm = True

    if st.button('No'):
        st.session_state.delete = False
        st.write('Pet not deleted.')

if st.session_state.confirm:
    # Send a DELETE request to the API
    response = requests.delete(f'http://api:4000/p/pets/{selected_pet_id}')

    if response.status_code == 200:
        st.success('Pet deleted!')
        st.session_state.delete = False
        st.session_state.confirm = False
    else:
        st.error('Failed to delete pet.')