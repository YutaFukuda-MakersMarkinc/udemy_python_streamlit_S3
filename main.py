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

##テキスト
st.write('DataFrame')

##表組み
#表組みの中身
df = pd.DataFrame({
    '一列目': [1, 2, 3, 4],
    '二列目': [10, 20, 30, 40]
})

#表組みの生成 -- ソート機能付き、whiteでは引数を指定できない
st.write(df)

#表組みの生成 -- ソート機能付き、引数による大きさの指定が可能
st.dataframe(df, width=200, height=200)
#https://docs.streamlit.io/library/api-reference/data/st.dataframe

#表組みの生成 -- ハイライトの表示 -- axis＝0は縦列を比較、axis＝1は横列を比較
st.dataframe(df.style.highlight_max(axis=0))
st.dataframe(df.style.highlight_max(axis=1))

#表組みの生成 -- スタティックな表組みの生成。ソート機能なし
st.table(df.style.highlight_max(axis=0))
#https://docs.streamlit.io/library/api-reference/data/st.table

#外部のjsonデータを取得することも可能
#https://docs.streamlit.io/library/api-reference/data/st.json

##マジックコマンド
#マークダウンを「"""〜"""」に記述
#https://docs.streamlit.io/library/api-reference/text
"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

##グラフの生成
#https://docs.streamlit.io/library/api-reference/charts
#折れ線グラフの中身
graph = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)

#折れ線グラフの生成
st.line_chart(graph)
#塗り付き折れ線グラフの生成
st.area_chart(graph)
#棒グラフの生成
st.bar_chart(graph)

##マップの生成
#https://docs.streamlit.io/library/api-reference/charts/st.map
#マップの中身
map = pd.DataFrame(
    np.random.rand(100, 2) / [50, 50] + [35.69, 139.70],#新宿付近を生成
    columns=['lat', 'lon']
)
#マップの生成
st.map(map)


##画像の表示
#https://docs.streamlit.io/library/api-reference/media
#画像を扱うため、PILをインポートする
from PIL import Image

#タイトルの生成
st.write('Display Image')

#チェックボックスのon/offで画像の表示を切り替える
#if行の下に、インデントで落とすと、trueの内容になる
if st.checkbox('Show Image'):
    #変数imgに「画像パス img.jpg※相対パス」を定義
    img = Image.open('img.jpg')
    #変数imgをst.imageで生成 -- use_column_width=Trueでカラムの幅100%で表示
    st.image(img, caption='explosion', use_column_width=True)


#タイトルの生成
st.write('Interactive Widgets')

#セレクトボックスの値を表示する
option = st.selectbox(
    'あなたが好きな数字を教えてください',
    #1〜10の数字を生成
    list(range(1,11))
)
'あなたの好きな数字は、', option, 'です。'

#st.sidebarを記述すると、サイドバーに掲載される
#テキストエリアの値を表示する
value = st.sidebar.text_input(
    'あなたの好きは花は？'
)
st.sidebar.write(
    'あなたの好きは花は、', value, 'です。'
)

slide = st.sidebar.slider(
    'あなたのテンションは？',
    0,#最低値
    100,#最高値
    50#デフォルト値
)
st.sidebar.write(
    'あなたのテンションは、', slide, 'です。'
)


left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('右カラム')

expander1 = st.expander('質問01')
expander1.write('回答01')
expander2 = st.expander('質問02')
expander2.write('回答02')
expander3 = st.expander('質問03')
expander3.write('回答03')