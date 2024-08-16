import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome Rescue Agency Manager, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('Add A Pet\'s Medical History', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/11_Manager_Med_His_View.py')

if st.button('Edit Pet Data', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/14_Manager_Pet_Database.py')

if st.button("View Status Of Pending Adoptions",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/13_Manager_Adoption_View.py')