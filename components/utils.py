import streamlit as st

SECTIONS = [
    "この教材でできるようになること",
    "Webサービスの登場人物とその役割は何だろう？",
    "登場人物同士はどんなやり取りをしているのだろう？",
    "確認テスト" 
]

def show_progress():
    if "completed" not in st.session_state:
        st.session_state.completed = {s: False for s in SECTIONS}

    done_count = sum(1 for s in SECTIONS if st.session_state.completed.get(s, False))
    percent = int(100 * done_count / len(SECTIONS))

    st.sidebar.markdown(f"### ✅ 進捗: {percent}%")
    st.sidebar.progress(percent / 100)

def section_complete_button(section_name: str):
    if "completed" not in st.session_state:
        st.session_state.completed = {s: False for s in SECTIONS}

    if not st.session_state.completed.get(section_name, False):
        if st.button("✅ このセクションを完了する"):
            st.session_state.completed[section_name] = True
            st.success("このセクションを完了として記録しました！")
            st.rerun() 
    else:
        st.info("このセクションは完了済みです。")

# テスト用：満点で進捗登録（確認テストページで使う）
def mark_section_complete_if_all_correct(section_name: str, score: int, total: int):
    if "completed" not in st.session_state:
        st.session_state.completed = {s: False for s in SECTIONS}
        

    if score == total:
        st.session_state.completed[section_name] = True
        st.rerun() 