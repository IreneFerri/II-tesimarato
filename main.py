import streamlit as st
import os
import numpy as np
import uuid
from glob import glob



if st.button('Clear Uploaded File(s)'): #and 'key' in st.session_state.keys():
    
    files_number_loaded = glob("*.dat")
    for my_file in files_number_loaded:
        st.write(my_file)
        os.remove(my_file)
        
if st.button('Compute mean/2'):
    mean = 0.0
    counter = 0
    files_number_loaded = glob("*.dat")
    for my_file in files_number_loaded:
        counter = counter + 1
        with open(my_file, 'r') as current_file:
            var = current_file.read()          
#            st.write(type(var))
            var = float(var)
#            st.write(type(var))
            mean = mean + var
    half_mean = mean/(2*counter)
    st.write('result is: ', half_mean)
    


