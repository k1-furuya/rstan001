import streamlit as st
import pandas as pd

#st.write("Hello World")

st.write("Hello :blue[World]")

st.title("Hello World")

st.title("Hello World :sunglasses:")

st.write(
    pd.DataFrame(
        {
            "first columns": [1,2,3,4],
            "second columns": [10,20,30,40]
        }
    )    
)

st.link_button("Clisk here", "https://docs.streamlit.io/develop/api-reference")

st.header("Hello World", divider="rainbow")

code = """print("hello")"""
st.code(code, language="python")

agree = st.checkbox("I agree")
if agree:
    st.write("Okay!")

options = st.multiselect(
    "好きな色はなんですか？",
    ["赤", "緑", "青", "黄"]
)

st.write("あなたが選んだ色は:", options)

options = st.radio(
    "好きな色はなんですか？",
    ["赤", "緑", "青", "黄"]
)

st.write("あなたが選んだ色は:", options)

# 修正できるデータフレーム
df = pd.DataFrame(
    [
        {"colors": "赤", "rating": 4},
        {"colors": "緑", "rating": 5},
        {"colors": "青", "rating": 3},
    ]
)
edited_df = st.data_editor(df)
st.write(edited_df.loc[edited_df["rating"].idxmax()]["colors"])

# 修正できるデータフレーム2
df = pd.DataFrame(
    [
        {"colors": "赤", "rating": 4, "mark": True},
        {"colors": "緑", "rating": 5, "mark": True},
        {"colors": "青", "rating": 3, "mark": True},
    ]
)
edited_df = st.data_editor(df)
edited_df = edited_df[edited_df["mark"] == True]
st.write(edited_df.loc[edited_df["rating"].idxmax()]["colors"])

csv = edited_df.to_csv().encode("utf-8")

st.download_button(
    label="csvをダウンロード",
    data=csv,
    file_name="sample_df.csv",
    mime="text/csv"
)

df = pd.DataFrame(
    {
        "sales": [20,55,100,80],
        "progress_sales": [20,55,100,80]
    }
)

st.data_editor(
    df,
    column_config={
        "progress_sales": st.column_config.ProgressColumn(
            min_value=0,
            max_value=100,
        )
    }
)

# 時系列バー表示
df = pd.DataFrame(
    {
        "sales":[
            [0, 4, 26, 30, 60, 80, 100],
            [3, 50, 0, 80, 40, 30, 100]
        ]
    }
)

st.data_editor(
    df,
    column_config={
        "sales": st.column_config.BarChartColumn(
            y_min=0,
            y_max=100,
        )
    }
)

st.data_editor(
    df,
    column_config={
        "sales": st.column_config.LineChartColumn(
            y_min=0,
            y_max=100,
        )
    }
)

# スライダー
age = st.slider("あなたは何歳ですか？", 0, 130, 40)
st.write("私は", age, "歳です")

# 日付選択
import datetime 
date = st.date_input("あなたが生まれたのはいつですか？", datetime.date(2000, 1, 1))
st.write("私は", date, "に生まれました")

# ユーザーの自由記述
text = st.text_input("入力してください", "XXXXX")
st.write(text)

# カラムを分ける
col1, col2 = st.columns(2)
with col1:
    st.title("Column1")
    st.write("これはカラムです")
with col2:
    st.title("Column2")
    st.write("これはカラム2です")

# タブを分ける
tab1, tab2 = st.tabs(["tab1","tab2"])
with tab1:
    st.title("tab1")
    st.write("これはタブ1です")
with tab2:
    st.title("tab2")
    st.write("これはタブ2です")

# アコーディオン表示
with st.expander("もっと詳しく見る"):
    st.write("XXXXXX")

# ポップアップ表示
with st.popover("もっと詳しく見る"):
    st.write("XXXXXX")

# サイドバー
with st.sidebar:
    st.title("XXXXXX")
    st.write("XXXXXX")

# 複数ページ実装
st.page_link("app.py", label="Home", icon="🏠")
st.page_link("pages/page1.py", label="page1")
st.page_link("pages/page2.py", label="page2")