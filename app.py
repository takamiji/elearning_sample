# 📁 ファイル: Home.py
import streamlit as st
from components.utils import show_progress

st.title("📘 Webアプリ技術入門 LMS")

show_progress()

st.markdown("""
この教材は、Webサービスの仕組みを初学者向けにわかりやすく解説する入門教材です。
左側のメニューから順番にセクションを選び、学習を進めてください。

- 各ページは短く完結にまとめられています
- コメントを書いたり、最後には確認テストで理解度をチェックできます
""")
