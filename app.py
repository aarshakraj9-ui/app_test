import streamlit as st
name= st.text_input("enter the name")
st.title("take the input")
if st.button("submit"):
  st.write(f"print the name: {name}")
  
