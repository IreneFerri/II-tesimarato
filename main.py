import streamlit as st
import os
import numpy as np
import uuid
from glob import glob



if st.button('Clear Uploaded File(s)') and 'key' in st.session_state.keys():
    st.session_state.pop('key')
    st.experimental_rerun()
    st.files_number_loaded.pop
    
    files_number_loaded = glob("*.dat")
    st.write(f"Files loaded = {files_number_loaded}")
    st.write(f"st.session_state.key")

