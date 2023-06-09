import streamlit as st
import os
import time
import datetime
import numpy as np
import uuid
from glob import glob


print("The app is starting...")


# If the user is new --> Generate a username with uuid
if 'username' not in st.session_state:
    st.write("USUARI NOU!")
#    username = f"user_{np.random.randint(100000000000)}"
    username = uuid.uuid4()
    print(username)
    st.session_state['username'] = username
else:
    print("Ja has enviat un nombre!")
    username = st.session_state['username']

filename = f"{username}.dat"



# check if the number is already submitted by looking
# at the files in the directory
if os.path.exists(filename):
    winner_filename =  "winner_file.dat"
    if os.path.exists( winner_filename):
        print("We have a winner")
        with open(winner_filename, "r") as f:
            winner_file_dat = f.readlines()[0]
            if winner_file_dat == filename:
                st.write("TU ETS EL GUANYADOR!")
            else:
                st.write("El guanyador és", winner_file_dat)

    else:
        with open(filename, "r" ) as f:
            user_number = int(f.readlines()[0])
            print(user_number)
        st.write(f"HAS ENVIAT EL NOMBRE {user_number}, usuari {username}")

        # wait 10 seconds

        time.sleep(10)
        # reload the page after 10 seconds
        st.experimental_rerun()

#    files_number_loaded = glob("*.dat")
#    st.write(f"Files loaded = {files_number_loaded}")
#    st.write(f{glob("f*.dat")})  # so you can see how many sumbissions are there, just to check htat you can see all the files
else:
    user_number = st.slider('Selecciona un nombre', 1, 100)
    st.write('El nombre seleccionat és ', user_number)
    st.write("El teu nom d'usuari és  ", username)
    #filename = f"{username}.dat"

    if st.button('Envia!'):
        st.write('Nombre enviat')
        with open(filename, "w" ) as f:
            print("El nombre enviat és ", user_number, "usuari", username)
            f.write(str(user_number))
        st.experimental_rerun()
