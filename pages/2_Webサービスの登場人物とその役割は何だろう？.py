import streamlit as st
from pathlib import Path
from PIL import Image
from components.utils import show_progress, SECTIONS, section_complete_button

show_progress()
image = Image.open("images/Webサービスの登場人物.png")

st.title("この教材でできるようになること")

with Path("content/section1.md").open(encoding="utf-8") as f:
    st.markdown(f.read(), unsafe_allow_html=True)

# コンテンツ
st.image(image, caption="Webサービスの登場人物",  width=600) 

# セクションを完了
section_complete_button("Webサービスの登場人物とその役割は何だろう？")

# コメント欄（任意）
try:
    from components.comments import comment_block
    comment_block("section1")
except ImportError:
    st.info("コメント機能が未定義です。components/comments.py を確認してください。")