import streamlit as st
#import numpy as np
#import pandas as pd
from PIL import Image
import time


st.title('Streamlit の練習')
st.title( '下のチェックボックスにチェックいれると写真❣が表示されます！！')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)


for i in range(100):
   latest_iteration.text(f'Iteration {i+1}')
   bar.progress(i+1)
   time.sleep(0.01)

'Done!!!!!!!'

left_column, right_column = st.beta_columns(2)
button = left_column.button('ここをタップしてね')
if button:
   right_column.write('なにがでてくるかな？')

expander1 = st.beta_expander('問題の答え（ここをタップ）')
expander1.write('いいものでてくるよ♥♥♥')


# text = st.sidebar.text_input('あなたの行きたいところを教えてください。')
# level = st.sidebar.slider('どれくらい行きたいかな？', 0, 100, 30)
#
# 'あなたの行きたいところ : ', text
# '行きたいレベル : ', level


#option = st.selectbox(
#    'あなたの好きな数字を教えてください。',
#    list(range(1,11))
#)


if st.checkbox('あなたの、みたい写真は：'):
   img = Image.open('sample1.jpg')
   st.image(img, caption='Sample Image', use_column_width=True)


