import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.write("# Edit Pet Database")
st.write(f"### Hi, {st.session_state['first_name']}. What would you like to do today?")

if st.button('Put a pet up for adoption', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/12_Manager_Adoption_Add.py')  

if st.button('Edit pet information', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/16_Manager_Edit_Pet.py') 

if st.button("Delete a pet from the database",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/15_Manager_Delete_Pet.py')