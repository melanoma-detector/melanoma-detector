import streamlit as st
from PIL import Image
import requests


# Title
highlighted_text_title = (
    "<span style='font-size: 35px; color: gray; text-decoration: underline overline;font-family: Calibri; '>"
    "**MELANOMA DETECTER**"
    "</span>"
)
st.markdown(highlighted_text_title, unsafe_allow_html=True)

two_mode = st.selectbox('Choose How', ['Upload Image File', 'Live Capture'])

if two_mode == "Upload Image File":
    # File uploader
    st.markdown('<h4 style="color:gray;">Upload the Image 📂</h2>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    # Check the uploaded Image
    if uploaded_file is not None:
        # Read Image file
        image = Image.open(uploaded_file)

        # Display the uploaded image
        st.image(image, caption="Uploaded Image", use_column_width=True)

        #Predict Button
        predict_button = st.button('Prediction')

        # When the Button "Prediction" is pushed >> Link it to Model
        if predict_button:
           # response = requests.post(predict_uri, files={'img':img_bytes}, timeout=30)
            st.write("O/X")


elif two_mode =='Live Capture':
    st.markdown('<h4 style="color:gray;">Live Capture 🎥</h4>', unsafe_allow_html=True)

    captured_picture = st.camera_input("Take a picture")

    if captured_picture:
        st.image(captured_picture, caption="Captured Image", use_column_width=True)

        #Predict Button
        predict_button = st.button('Prediction')

        # When the Button "Prediction" is pushed >> Link it to Model
        if predict_button:
            st.write("O/X")



#### 링크 참고: https://docs.streamlit.io/library/api-reference/widgets/st.camera_input
