import streamlit as st
import json
import os

COMMENTS_DIR = "data/comments"
os.makedirs(COMMENTS_DIR, exist_ok=True)

def _get_comment_path(section_id):
    return os.path.join(COMMENTS_DIR, f"{section_id}.json")

def load_comments(section_id):
    path = _get_comment_path(section_id)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_comments(section_id, comments):
    path = _get_comment_path(section_id)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(comments, f, ensure_ascii=False, indent=2)

def comment_block(section_id: str):
    st.markdown("## 💬 このセクションへのコメント")

    comments = load_comments(section_id)

    with st.form(key=f"{section_id}_form"):
        name = st.text_input("名前（任意）", key=f"{section_id}_name")
        comment = st.text_area("コメントを書く", key=f"{section_id}_comment")
        submitted = st.form_submit_button("コメントを投稿する")

        if submitted and comment.strip():
            new_comment = {
                "name": name.strip() or "匿名",
                "comment": comment.strip()
            }
            comments.append(new_comment)
            save_comments(section_id, comments)
            st.success("コメントを投稿しました")

    st.markdown("### 📝 投稿されたコメント")
    if comments:
        for item in reversed(comments):
            st.markdown(f"**{item['name']}**")
            st.write(item['comment'])
            st.markdown("---")
    else:
        st.info("まだコメントはありません。")
