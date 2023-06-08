import streamlit as st
if st.button('Clear Uploaded File(s)') and 'key' in st.session_state.keys():
    st.session_state.pop('key')
    st.experimental_rerun()
    

