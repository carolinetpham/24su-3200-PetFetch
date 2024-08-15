import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

# Display the appropriate sidebar links for the role of the logged in user
SideBarLinks()

st.title('Add New Pet Medical History')

# Fetch the list of petIDs from the API
response = requests.get('http://api:4000/p/pets')
pets = response.json()

# Extract the petIDs from the response
pet_ids = [pet['petID'] for pet in pets]

# Create a select box for petID
selected_pet_id = st.selectbox('Select Pet ID:', pet_ids)

# Create a form
entry_error = True
with st.form(key='add_medical_history'):
  entry = st.text_input(label='Entry: Describe the medical issue (2000 characters or less)')
  if len(entry) > 2000:
      st.write('**Sorry, your medical issue entry is too long.**')
      entry_error = False
  date = st.date_input(label='Date')

  # Submit button
  submitted = st.form_submit_button('Submit')

# If the form is submitted, send a POST request to the API with the form data
if submitted and entry_error:
    data = {}
    data['entry'] = entry
    data['date'] = date.isoformat()

    response = requests.post(f'http://api:4000/m/med/{selected_pet_id}', json=data)

    if response.status_code == 200:
        st.success('Medical entry added successfully!')
    else:
        st.error('Failed to add medical entry.')
if entry_error == False:
    st.write('Error: Form filled out incorrectly')
  