import streamlit as st
from PIL import Image
from components.comments import comment_block

def load_markdown(section_index):
    paths = ["content/section1.md", "content/section2.md"]
    with open(paths[section_index], "r", encoding="utf-8") as f:
        return f.read()

st.set_page_config(layout="wide")

# セクション一覧
sections = [
    "Webサービスの登場人物とその役割は何だろう？",
    "登場人物同士はどんなやり取りをしているのだろう？"
]

# 初期状態の保持
if 'current_section' not in st.session_state:
    st.session_state.current_section = sections[0]

if 'completed' not in st.session_state:
    st.session_state.completed = {section: False for section in sections}

# サイドバーのカスタムボタンUI
st.sidebar.title("Webアプリ技術入門")
for section in sections:
    if st.sidebar.button(section, key=section):
        st.session_state.current_section = section

# 現在のセクション表示
selected_section = st.session_state.current_section
st.title(selected_section)

# コンテンツ
image = Image.open("images/Webサービスの登場人物.png")
if selected_section == sections[0]:
    st.markdown(load_markdown(0), unsafe_allow_html=True)
    
    st.image(image, caption="Webサービスの登場人物",  width=600)    
    
    st.markdown("""
---
### まとめ

Webサービスは「1つの大きな仕組み」ではなく、複数の登場人物が分業して支えているのです。  
それぞれの役割を理解することで、後の学習（DOM・HTTP・DBなど）もスムーズになります。
""")
    st.markdown("""---""") 
    comment_block("section0")
    st.markdown("""---""") 

elif selected_section == sections[1]:
    st.markdown(load_markdown(1), unsafe_allow_html=True)
    st.markdown("""
---

### まとめ

- Webサービスは、役割の違う登場人物たちが順番に処理を行い、1つの結果を作り上げている。
- ブラウザ、サーバー、アプリ、データベースがそれぞれ会話しながら連携している。
- 普段は見えないけれど、検索ボタン1つでたくさんのやり取りが同時に動いているのです。

""")
    st.markdown("""---""") 
    comment_block("section1")
    st.markdown("""---""")       

# 完了ボタン
if not st.session_state.completed[selected_section]:
    if st.button("✅ このセクションを完了する"):
        st.session_state.completed[selected_section] = True
        st.success("完了として記録しました！")
else:
    st.info("このセクションは完了済みです。")

# 進捗表示
completed_count = sum(st.session_state.completed.values())
total = len(sections)
progress = int((completed_count / total) * 100)

st.sidebar.markdown("---")
st.sidebar.markdown(f"進捗：{progress}% 完了")
st.sidebar.progress(progress / 100)
