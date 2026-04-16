import streamlit as st

st.title("My First Python Web App")
st.write("This app is connected with GitHub Actions and security scan.")

name = st.text_input("Enter your name")

if name:
    st.success(f"Hello {name}!")