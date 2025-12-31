import streamlit as st

option = st.selectbox(
    "Choose a role",
    ["Manual QA", "Automation QA", "Developer"]
)
st.write("Selected:", option)