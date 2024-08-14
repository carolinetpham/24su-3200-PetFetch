import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title(f"Welcome Researcher, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('View Adoption Sites With Least Adoptions', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/21_Least_Adoptions.py')

if st.button('View Pets With Least Interest', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/22_Least_Interest.py')

if st.button('View Most Surrendered Pets', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/23_Most_Surrendered.py')