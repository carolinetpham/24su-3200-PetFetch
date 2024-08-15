import logging
logger = logging.getLogger(__name__)
import pandas as pd
import streamlit as st
from streamlit_extras.app_logo import add_logo
import numpy as np
import plotly.express as px
from modules.nav import SideBarLinks
import requests

# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()

# set the header of the page
st.header("Adoptable Pet Data Test!")

# You can access the session state to make a more customized/personalized app experience
st.write(f"### Hi, {st.session_state['first_name']}!")
st.write('Select your pet criteria:')
pets = requests.get('http://api:4000/p/pets/available').json()

# Add a multiselect widget to select species
selected_species = st.multiselect('Preferred species:', list(set(item['species'] for item in pets)))

# Add a multiselect widget to select breeds
selected_breeds = st.multiselect('Preferred breeds:', list(set(item['breed'] for item in pets)))

# Add a range slider for age
selected_age = st.slider("Preferred age:", 0, 25, (0, 25))

# filters pets data
filtered_pets = pets
if selected_species:
    filtered_pets = [item for item in filtered_pets if item.get('species') in selected_species]
if selected_breeds:
    filtered_pets = [item for item in filtered_pets if item.get('breed') in selected_breeds]
if selected_age:
    filtered_pets = [item for item in filtered_pets if selected_age[0] <= int(item.get('age')) <= selected_age[1]]

# Report the unfiltered/filtered dataframe
if filtered_pets:
    st.write('Here are all the pets that fufill your criteria!')
    st.dataframe(filtered_pets)

    # get the contact data
    contact_info = requests.get('http://api:4000/p/pets/contact').json()

    # Select a pet you would like to express interest in!
    desired_pet = st.selectbox('Select you a pet you are interested in adopting!', filtered_pets)

    # filter contacts for those hosting a desired pet
    filtered_contacts = [item for item in contact_info if item.get('petID') == desired_pet['petID']]

    # save important attributes
    name = [item.get('agencyName') for item in filtered_contacts]
    phone = [item.get('phone') for item in filtered_contacts]
    email = [item.get('email') for item in filtered_contacts]
    street = [item.get('street') for item in filtered_contacts]
    city = [item.get('city') for item in filtered_contacts]
    state = [item.get('state') for item in filtered_contacts]
    zip = [item.get('zip') for item in filtered_contacts]
    entryDate = [item.get('entryDate') for item in filtered_contacts]

    # If the pet is held at an agency, report that agencies contacts
    try:
        st.write(f'''
            Here is their current agencies' contact information:
            - **Agency Name**: {name[0]}
            - **Phone Number**: {phone[0]}
            - **Email Address**: {email[0]}
            - **Address**: {street[0]}, {city[0]} {state[0]} {zip[0]}
            - **Date of Entry**: {entryDate[0]}
            '''
        )
    except:
        st.write('Uh oh! That pet does not seem to currently be held at any agency :(')

    # report contact information for each previous agency the pet was held at
    if len(name) > 0:
        st.write('Here is the contact information of any angecies they were previously held at:')
    for i in range(len(name)):
        if i > 0:
            st.write(f''' 
                {i}.
                - **Agency Name**: {name[i]}
                - **Phone Number**: {phone[i]}
                - **Email Address**: {email[i]}
                - **Address**: {street[i]}, {city[i]} {state[i]} {zip[i]}
                - **Date of Entry**: {entryDate[i]}
                '''
            )
else:
    st.write('Unfortunately, no pets fit your criteria :(.')