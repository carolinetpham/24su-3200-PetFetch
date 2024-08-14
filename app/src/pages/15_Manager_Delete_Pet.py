import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.write("# Delete a Pet from the Database")

# Using HTML in st.markdown to style the text
st.markdown("<div style='color: indianred; font-size: 20px;'> \
<strong>WARNING: Once you delete a pet, you cannot recover the data.<strong></div>", unsafe_allow_html=True)