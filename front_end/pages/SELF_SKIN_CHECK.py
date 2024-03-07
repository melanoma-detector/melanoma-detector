import streamlit as st
import numpy as np
import pandas as pd
import base64

## Image Classification:
### https://medium.com/geekculture/image-classifier-with-streamlit-887fc186f60
#####이미지 업로드_Streamlit 에서 제공하는 파일 업로드 함수를 사용해서 파일을 올릴 버튼을 생성
# https://velog.io/@wonjun12/Streamlit-%ED%8C%8C%EC%9D%BC-%EC%97%85%EB%A1%9C%EB%93%9C



#####실험중
highlighted_text_title = (
    "<span style='font-size: 35px; color: gray; text-decoration: underline overline;font-family: Calibri; '>"
    "**SELF SKIN CHECK**"
    "</span>"
)
st.markdown(highlighted_text_title, unsafe_allow_html=True)

st.markdown('<h4 style="color:gray;">Using Webcam 📸</h2>', unsafe_allow_html=True)
st.markdown('<h4 style="color:gray;">Uploading File 📂</h2>', unsafe_allow_html=True)

####################
####################
upload= st.file_uploader('Insert image for classification', type=['png','jpg'])
c1, c2= st.columns(2)
if upload is not None:
  im= Image.open(upload)
  img= np.asarray(im)
  image= cv2.resize(img,(224, 224))
  img= preprocess_input(image)
  img= np.expand_dims(img, 0)
  c1.header('Input Image')
  c1.image(im)
  c1.write(img.shape)


####################
# First, we need to upload the image to our image classifier.
# That uploaded image is pre-processed before feeding to a classifier.

#load weights of the trained model.
  input_shape = (224, 224, 3)
  optim_1 = Adam(learning_rate=0.0001)
  n_classes=6
  vgg_model = model(input_shape, n_classes, optim_1, fine_tune=2)
  vgg_model.load_weights('/content/drive/MyDrive/vgg/tune_model19.weights.best.hdf5')
# 위의 model 경로 바꿔!


  # prediction on model
  vgg_preds = vgg_model.predict(img)
  vgg_pred_classes = np.argmax(vgg_preds, axis=1)
  c2.header('Output')
  c2.subheader('Predicted class :')
  c2.write(classes[vgg_pred_classes[0]] )




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
