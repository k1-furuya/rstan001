import streamlit as st
import pandas as pd
import numpy as np

# サンプルデータを作成
np.random.seed(0)
data = pd.DataFrame({
    "x": np.arange(10),
    "y1": np.random.randn(10),
    "y2": np.random.randn(10),
    "y3": np.random.randn(10)
})

# サイドバーを作成
with st.sidebar:
    chart_selection = st.radio("表示するグラフの選択",["棒グラフ", "面グラフ", "散布図"])

# メインコンテンツを作成
st.title("グラフの可視化")

# レイアウト用の列を作成
col1, col2, col3 = st.columns(3)

# チャート1を表示
with col1:
    st.header("グラフ1")
    if chart_selection == "棒グラフ":
        st.line_chart(data[["x","y1"]])
    elif chart_selection == "面グラフ":
        st.area_chart(data[["x","y1"]])
    elif chart_selection == "散布図":
        st.scatter_chart(data[["x","y1"]])

# チャート2を作成
with col2:
    st.header("グラフ2")
    if chart_selection == "棒グラフ":
        st.line_chart(data[["x","y2"]])
    elif chart_selection == "面グラフ":
        st.area_chart(data[["x","y2"]])
    elif chart_selection == "散布図":
        st.scatter_chart(data[["x","y2"]])

with col3:
    st.header("グラフ3")
    if chart_selection == "棒グラフ":
        st.line_chart(data[["x","y3"]])
    elif chart_selection == "面グラフ":
        st.area_chart(data[["x","y3"]])
    elif chart_selection == "散布図":
        st.scatter_chart(data[["x","y3"]])

# チャートに関する詳細情報を表示するためのエクスパンダーを作成
with st.expander("グラフの詳細情報を表示"):
    if chart_selection == "棒グラフ":
        st.write("これは棒グラフです。時間の経過に伴うデータの傾向を可視化しています。")
    elif chart_selection == "面グラフ":
        st.write("これは面グラフです。時間の経過に伴うデータの分布を可視化しています。")
    elif chart_selection == "散布図":
        st.write("これは散布図です。2つの変数間の関係性を可視化しています。")

st.title("テキスト入力アプリ")
user_input = st.text_input("テキストを入力してください", "")
st.write("入力したテキスト:", user_input)

# アプリのタイトル
st.title("スライダーアプリ")

# スライダー
selected_value = st.slider("値を選択してください", min_value=0, max_value=100, value=50)

# 選択された値を表示
st.write("選択された値:", selected_value)

st.title("シンプルなセレクトボックスアプリ")
options = ["選択肢1", "選択肢2", "選択肢3"]
selected_option = st.selectbox("選択してください", options)
st.write("選択された値:", selected_option)