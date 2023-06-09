import streamlit as st
import os
import numpy as np
import uuid
from glob import glob


# If the user is new --> Generate a username with uuid
if 'username' not in st.session_state:
    st.write("USUARI NOU!")
#    username = f"user_{np.random.randint(100000000000)}"
    username = uuid.uuid4()
    print(username)
    st.session_state['username'] = username
    filename = f"{username}.dat"
else:
    print("Ja has enviat un nombre!")
    username = st.session_state['username']





if os.path.exists(f"{username}.dat"):
    filename = f"{username}.dat"
    with open(filename, "r" ) as f:
        user_number = int(f.readlines()[0])
        print(user_number)
    st.write(f"HAS ENVIAT EL NOMBRE {user_number}, usuari {username}")
#    files_number_loaded = glob("*.dat")
#    st.write(f"Files loaded = {files_number_loaded}")
#    st.write(f{glob("f*.dat")})  # so you can see how many sumbissions are there, just to check htat you can see all the files
else:

    user_number = st.slider('Pick a number', 1, 100)
    st.write('El nombre seleccionat es ', user_number)
    st.write("El teu nom d'usuari es  ", username)
    filename = f"{username}.dat"

    if st.button('submit'):
        st.write('Number submitted')
        with open(filename, "w" ) as f:
            print("the user number is ", user_number, "user", username)
            f.write(str(user_number))
        st.experimental_rerun()
