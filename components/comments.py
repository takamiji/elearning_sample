import streamlit as st

def comment_block(section_id: str):
    """セクション単位のコメント欄（session_stateベース）"""
    st.markdown("##### 💬 このセクションへのコメント")

    comment_input_key = f"{section_id}_comment_input"
    comment_list_key = f"{section_id}_comments"

    # 初期化
    if comment_list_key not in st.session_state:
        st.session_state[comment_list_key] = []

    # 入力フォーム
    with st.form(key=f"{section_id}_form"):
        name = st.text_input("名前（任意）", key=f"{section_id}_name")
        comment = st.text_area("コメントを書く", key=comment_input_key)
        submitted = st.form_submit_button("コメントを投稿する")

        if submitted and comment.strip():
            st.session_state[comment_list_key].append({
                "name": name if name.strip() else "匿名",
                "comment": comment.strip()
            })
            st.success("コメントを投稿しました")

    # コメント表示
    st.markdown("##### 📝 投稿されたコメント")
    if st.session_state[comment_list_key]:
        for item in reversed(st.session_state[comment_list_key]):
            st.markdown(f"**{item['name']}**")
            st.write(item['comment'])
            st.markdown("---")
    else:
        st.info("まだコメントはありません。")
 
