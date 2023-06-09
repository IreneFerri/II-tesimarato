import streamlit as st
import os
import numpy as np
import uuid
from glob import glob



if st.button('Esborrar arxius'): #and 'key' in st.session_state.keys():
    
    files_number_loaded = glob("*.dat")
    for my_file in files_number_loaded:
        st.write(my_file)
        os.remove(my_file)
        
if st.button('Meitat de la mitjana'):
    mean = 0.0
    files_number_loaded = glob("*.dat")
    total_inputs = len(files_number_loaded)
    for my_file in files_number_loaded:
        with open(my_file, 'r') as current_file:
            var = current_file.read()          
            var = float(var)
            mean = mean + var
            st.write("L'USUARI    " , my_file, '    ha enviat el nombre ', var)
    half_mean = mean/(2*total_inputs)
    st.write('LA MEITAT DE LA MITJANA ES: ', half_mean)

if st.button('Comprovar arxius'):
    files_number_loaded = glob("*.dat")
    for my_file in files_number_loaded:
        st.write(my_file)

    

    


