import streamlit as st
import os
import numpy as np
import uuid
from glob import glob

# Fuction to find the nearest value
def find_nearest(array, value, users):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return users[idx]


        
if st.button('Comprovar arxius'):
    files_number_loaded = glob("*.dat")
    for my_file in files_number_loaded:
        with open(my_file, 'r') as current_file:
            var = current_file.read()
            var = float(var)
            st.write("L'USUARI    " , my_file, '    ha enviat el nombre ', var)
        
if st.button('Meitat de la mitjana'):
    mean = 0.0
    files_number_loaded = glob("*.dat")
    total_inputs = len(files_number_loaded)
    var_array = np.zeros(total_inputs)
    counter = 0
    for my_file in files_number_loaded:
        with open(my_file, 'r') as current_file:
            var = current_file.read()          
            var = float(var)
            mean = mean + var
            var_array[counter] = var            
            counter = counter + 1
            st.write("L'USUARI    " , my_file, '    ha enviat el nombre ', var)
    half_mean = mean/(2*total_inputs)
    winner = find_nearest(var_array, half_mean, files_number_loaded)
    st.write('LA MEITAT DE LA MITJANA ES: ', half_mean)
    st.write('EL GUANYADOR ES: ', winner)

    with open("winner_file.dat", "w") as f:
        f.write(winner)



if st.button('Esborrar arxius'): #and 'key' in st.session_state.keys():
    
    files_number_loaded = glob("*.dat")
    for my_file in files_number_loaded:
        st.write(my_file)
        os.remove(my_file)
    

    


