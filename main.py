import streamlit as st
import os
import numpy as np
import uuid
from glob import glob



if st.button('Clear Uploaded File(s)') and 'key' in st.session_state.keys():
    st.session_state.pop('key')
    st.experimental_rerun()
    st.experimental_rerun()

