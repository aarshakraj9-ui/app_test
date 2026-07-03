import streamlit as st
st.title("take the input")
name= st.text_input("enter the name")
if st.button("submit"):
  st.write(f"print the name: {name}")
  
