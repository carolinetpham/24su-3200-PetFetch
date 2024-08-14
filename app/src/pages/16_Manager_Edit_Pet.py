import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests
import pandas as pd

st.set_page_config(layout = 'wide')

# Display the appropriate sidebar links for the role of the logged in user
SideBarLinks()

st.title('Update Pet Information')

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
selected_pet_id = st.selectbox('Select Pet ID:', pet_ids)

# Create input fields for pet attributes
name = st.text_input('Name:')
status = st.selectbox('Adoption Status:', ['Yes', 'No'])
species = st.text_input('Species:')
breed = st.text_input('Breed:')
birthday = st.date_input('Birthday:')
age = st.number_input('Age:', min_value=0)
alive = st.checkbox('Is Alive?')
  
if st.button('Update Pet'):
    # Convert 'Yes' to 1 and 'No' to 0
    status = 1 if status == 'Yes' else 0

    # Send a PUT request to the API with the new values
    response = requests.put('http://api:4000/p/pets', json={
        'petID': selected_pet_id,
        'name': name,
        'adoption_status': status,
        'species': species,
        'breed': breed,
        'birthday': birthday.strftime('%Y-%m-%d'),  # Convert the date to a string
        'age': age,
        'is_alive': alive
    })

    if response.status_code == 200:
        st.success('Pet updated successfully!')
    else:
        st.error('Failed to update pet.')  