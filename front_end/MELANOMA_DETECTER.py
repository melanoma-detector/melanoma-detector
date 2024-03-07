import streamlit as st
import numpy as np
import pandas as pd
import streamlit as st
import requests
import base64


########Simha Teaching

api_url = 'http://127.0.0.1:8000/upload'


######################
####Text
## Title
highlighted_text_title = (
    "<span style='font-size: 35px; color: gray; text-decoration: underline overline;font-family: Calibri; '>"
    "**MELANOMA DETECTER**"
    "</span>"
)
st.markdown(highlighted_text_title, unsafe_allow_html=True)

# Define the text with custom HTML and CSS styling
highlighted_text = (
    "<span style='font-size: 30px; color: gray;  font-family: Calibri; '>"
    "What's Melanoma?"
    "</span>"
)

# Display the rest of the text using the st.text_area function
rest_of_text = (
    "Melanoma is a kind of skin cancer that starts in the melanocytes. Melanocytes are cells that make the pigment that gives skin its color. The pigment is called melanin. Melanoma typically starts on skin that's often exposed to the sun. This includes the skin on the arms, back, face and legs. Melanoma also can form in the eyes. Rarely, it can happen inside the body, such as in the nose or throat. The exact cause of all melanomas isn't clear. Most melanomas are caused by exposure to ultraviolet light. Ultraviolet light, also called UV light, comes from sunlight or tanning lamps and beds. Limiting exposure to UV light can help reduce the risk of melanoma. The risk of melanoma seems to be increasing in people under 40, especially women. Knowing the symptoms of skin cancer can help ensure that cancerous changes are detected and treated before the cancer has spread. Melanoma can be treated successfully if it is found early."
)
st.markdown(highlighted_text, unsafe_allow_html=True)
st.text_area("▶", rest_of_text)



#####IMAGE (https://docs.streamlit.io/library/api-reference/media/st.image)
import streamlit as st
st.image('images/melanoma_image.jpg') # caption='Check Out!')

# Page Link
st.page_link("https://www.mayoclinic.org/diseases-conditions/melanoma/symptoms-causes/syc-20374884", label="Click! for more Information", icon="👉")






###########
###Page_Link (https://docs.streamlit.io/library/api-reference/widgets/st.page_link)
#st.page_link("front_end.py", label="Home", icon="🤖")
#st.page_link("pages/page_1.py", label="Page 1", icon="1️⃣")
#st.page_link("pages/page_2.py", label="Page 2", icon="2️⃣")
#st.page_link("https://freyjamedical.com/signs-of-a-melanoma/", label="For More Information", icon="🌎")
