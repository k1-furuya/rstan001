import streamlit as st
from st_pages import _get_pages_from_config
# ページの設定
st.set_page_config(
    page_title="Streamlit勉強会",
    page_icon=":computer:",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        'Get Help': 'https://docs.streamlit.io/develop/api-reference/configuration/st.set_page_config',
        'Report a bug': "https://docs.streamlit.io/develop/api-reference/configuration/st.set_page_config",
        'About': "Streamlitでアプリを作成しよう"
}
)
st.title('はじめてのStreamlit')
st.write('Streamlitでアプリを作成しよう')
_get_pages_from_config()

st.title('session_stateを使う場合')
if "count" not in st.session_state:
        st.session_state["count"] = 0

test = st.button("test")

if test:
    st.session_state["count"] += 1

st.write("session_state使用 → ", st.session_state["count"])

st.title("コールバックの使用")

def test_callback():
    st.write("コールバックが実行されました。入力されたテキストはこちら→" + st.session_state["text_input"])

st.text_input("テキスト入力", key="text_input", on_change=test_callback)