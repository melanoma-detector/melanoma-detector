import streamlit as st
from PIL import Image
import numpy as np
import cv2
from streamlit_webrtc import VideoTransformer, webrtc_streamer

# from your_module import preprocess_input


## Image Classification:
### https://medium.com/geekculture/image-classifier-with-streamlit-887fc186f60
#####이미지 업로드_Streamlit 에서 제공하는 파일 업로드 함수를 사용해서 파일을 올릴 버튼을 생성
# https://velog.io/@wonjun12/Streamlit-%ED%8C%8C%EC%9D%BC-%EC%97%85%EB%A1%9C%EB%93%9C

#### TEXT
highlighted_text_title = (
    "<span style='font-size: 35px; color: gray; text-decoration: underline overline;font-family: Calibri; '>"
    "**SCAN YOUR SKIN**"
    "</span>"
)
st.markdown(highlighted_text_title, unsafe_allow_html=True)

st.markdown('<h4 style="color:gray;">Uploading File 📂</h2>', unsafe_allow_html=True)

####################
####################
# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Display the uploaded image
if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)


###################
####Using Webcam##########
st.markdown('<h4 style="color:gray;">Using Webcam 📸</h2>', unsafe_allow_html=True)

class VideoTransformerBase(VideoTransformer):
    frame_rate: float

    def __init__(self) -> None:
        self.frame_rate = 0

    def transform(self, frame):
        self.frame_rate = self.frame_rate * 0.9 + 1.0 / (frame.timestamp - getattr(self, 'timestamp', frame.timestamp))
        self.timestamp = frame.timestamp

        return frame

def main():
    st.title("Webcam Image Capture")

    webrtc_ctx = webrtc_streamer(
        key="example",
        video_transformer_factory=VideoTransformerBase,
        async_transform=True,
        sendback_audio=False,
        height=480,
        )

    if webrtc_ctx.video_transformer:
        st.write(f"Frame rate: {webrtc_ctx.video_transformer.frame_rate:.2f}")

        if st.button("Capture Image"):
            captured_image = webrtc_ctx.video_transformer.last_frame
            if captured_image is not None:
                st.image(captured_image.to_ndarray(format="bgr24"), channels="BGR")

if __name__ == "__main__":
    main()







from datetime import datetime

#def main(img_file):
    #if img_file is not None: # 파일을 넣을 경우에만 실행 함
        #current_time = datetime.now() # 현재 시간 가져옴.
    # 2023-05-25 17:54:48.360 형태로 가져온다.
        #filename = current_time.isoformat().replace(":", "_")
        # isoformat() : String으로 포멧 (변환)하겠다.
        # replace() : 파일을 저장하는데 일부 특수문자를 사용하지 못하는데 ':'를 '_'로 변환해준다.
        #img_file.name = filename
    ##### Simha + call api
        #response = requests.get(api_url)  # Simha: ins[ector -- error status (Method: GET / 8000)]
        #st.title(response)
        #response.json()
        #st.write(f"Do I have cancer?:"+response.prediction)
        # 이미지 파일의 이름을 변환한 이름으로 변경한다.



def save_uploaded_file():
    response = requests.get(api_url)  # Simha: ins[ector -- error status (Method: GET / 8000)]
    st.title(response)

img_file = st.file_uploader('이미지를 업로드 하세요.', type=['png', 'jpg', 'jpeg'], on_change=save_uploaded_file)
#save_uploaded_file() ##Figure out how to make this method wait till image is selected
# 위의 함수를 아래의 img_file 안에 저장해서, on_change 가 불려지면, 뭔가 변화가 생기면 그것을 불러냄.
