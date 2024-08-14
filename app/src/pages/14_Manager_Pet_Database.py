import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.write("# Edit Pet Database")
st.write(f"### Hi, {st.session_state['first_name']}. What would you like to do today?")

if st.button('Put up a Pet for Adoption', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/12_Manager_Adoption_Add.py')

if st.button("Delete a Pet from the Database",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/15_Manager_Delete_Pet.py')