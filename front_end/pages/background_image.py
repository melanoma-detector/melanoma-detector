import streamlit as st
import base64


@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Define separate images for the sidebar and the container
sidebar_img = get_img_as_base64("images/sidebar_background.jpg")
container_img = get_img_as_base64("images/container_background.jpg")

# Define CSS styles for the sidebar and the container
sidebar_css = f"""
[data-testid="stSidebar"] {{
    background-image: url("data:image/jpg;base64,{sidebar_img}");
    background-size: cover;
}}

[data-testid="stHeader"] {{
    background-color: rgba(0, 0, 0, 0);
}}
"""

container_css = f"""
[data-testid="stAppViewContainer"] {{
    background-image: url("data:image/jpg;base64,{container_img}");
    background-size: cover;
}}
"""

# Apply the CSS styles
st.markdown(f"<style>{sidebar_css}</style>", unsafe_allow_html=True)
st.markdown(f"<style>{container_css}</style>", unsafe_allow_html=True)





###########Another way
### BACKGROUND IMAGE
######BACKGROUND IMAGE (https://www.youtube.com/watch?v=pyWqw5yCNdo)
import streamlit as st
import base64

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64("images/background.jpg")

# RGBA : https://www.hexcolortool.com/#f74b6a,0.33
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("data:image/jpg;base64,{img}");
    background-size: cover;
}}

[data-testid="stHeader"] {{
    background-color: rgba(0, 0, 0, 0);
}}

[data-testid="stSidebar"] {{
    background-color: rgba(248, 109, 144, 0.38);
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
