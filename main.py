import streamlit as st
with st.form("my-form", clear_on_submit=True):
        file = st.file_uploader("upload file")
        submitted = st.form_submit_button("submit")
