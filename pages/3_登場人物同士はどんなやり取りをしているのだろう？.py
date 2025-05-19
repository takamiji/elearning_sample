import streamlit as st
from pathlib import Path
from PIL import Image
from components.utils import show_progress, SECTIONS, section_complete_button

show_progress()

image1 = Image.open("images/HTTPリクエスト.png")
image2 = Image.open("images/HTTPレスポンス.png") 

st.title("登場人物同士はどんなやり取りをしているのだろう？")

with Path("content/section2.md").open(encoding="utf-8") as f:
    st.markdown(f.read(), unsafe_allow_html=True)

# コンテンツ
st.image(image1, caption="HTTPリクエスト",  width=600)  
st.image(image2, caption="HTTPレスポンス",  width=600)

# セクションを完了
section_complete_button("登場人物同士はどんなやり取りをしているのだろう？")

# コメント欄（任意）
try:
    from components.comments import comment_block
    comment_block("section2")
except ImportError:
    st.info("コメント機能が未定義です。components/comments.py を確認してください。")