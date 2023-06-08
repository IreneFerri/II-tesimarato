import streamlit as st
import os
import numpy as np
import uuid
from glob import glob



if st.button('Clear Uploaded File(s)') #and 'key' in st.session_state.keys():
    
    files_number_loaded = glob("*.dat")
    for my_file in files_number_loaded:
        os.remove(my_file)


