import streamlit as st
st.title("take the input")
name= st.text_input("enter the name")
st.title("take the input")
if st.button("submit"):
  st.write(f"print the name: {name}")
  
