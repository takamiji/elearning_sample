import streamlit as st
from pathlib import Path
from components.utils import show_progress, SECTIONS, section_complete_button

show_progress()
st.title("この教材でできるようになること")

with Path("content/section0.md").open(encoding="utf-8") as f:
    st.markdown(f.read(), unsafe_allow_html=True)

section_complete_button("この教材でできるようになること")

# コメント欄（任意）
try:
    from components.comments import comment_block
    comment_block("section0")
except ImportError:
    st.info("コメント機能が未定義です。components/comments.py を確認してください。")