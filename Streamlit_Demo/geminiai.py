import streamlit as st
import google.generativeai as genai

st.title("Welcom to my streamlit App")

user_input = st.text_input("ASK me anything")

genai.configure(api_key='AIzaSyCa5pZ-5spk4tzE96RB4vRnq-LgxNihh-Q')

model = genai.GenerativeModel('models/gemini-2.5-flash')

if user_input:
    response = model.generate_content(user_input)
    st.write(response.text)

for n in genai.list_models():
    print(n.name)