import streamlit as st
import numpy as np
import pandas as pd


##タイトル
st.title('Streamlit 超入門')

##テキスト
st.write('Progress')

#プログレスバーの作成
import time
'Start!!'

latest_interation = st.empty()
bar = st.progress(0)

for i in range(100):
    #print(i)
    latest_interation.text(f'Interation {i + 1}')
    bar.progress(i + 1)
    time.sleep(0.1)

#プログレスバーが100になると、下記の記述が表示される
'Done!!'
