import streamlit as st
from content.test import show_quiz
from components.utils import show_progress, SECTIONS, mark_section_complete_if_all_correct

show_progress()

st.title("確認テスト")

show_quiz()