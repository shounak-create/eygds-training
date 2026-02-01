import streamlit as st

st.title("some basic command in streamlit like slider, checkbox, radio button etc")

age = st.slider("select your age", 1, 100) 
city = st.selectbox("select your city", ["shrigonda", "Mumbai", "pune", "yz_pakistan", "Phoenix"])


if st.checkbox("show details"):
    st.write(f"your age is {age} and you live in {city}")
