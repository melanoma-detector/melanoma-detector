import streamlit as st
import requests

st.title("My mole classifier app")

#st.write("Please load your image")

param1 = st.slider('Select a number', 1, 10, 3)

param2 = st.slider('Select another number', 1, 10, 3)

#this needs to be changed with the gcp url
url = 'https://melcont-frvnbh56ia-ew.a.run.app/predict'

params = {
    'feature1': param1,  # 0 for Sunday, 1 for Monday, ...
    'feature2': param2
}
response = requests.get(url, params=params).json()
#st.text(response.json())
st.write("The mole ", str(response['prediction']))
