import streamlit as st
from components.utils import show_progress, SECTIONS, mark_section_complete_if_all_correct

def show_quiz():
    st.write("この教材の内容をもとに、以下の質問に答えてください。")

    questions = [
        {
            "question": "Webサービスにおいて、ユーザーの操作を最初に受け取るのは誰ですか？",
            "options": ["データベース", "Webサーバー", "ブラウザ", "アプリケーションサーバー"],
            "answer": "ブラウザ"
        },
        {
            "question": "次のうち、データを保存・検索する役割をもつのはどれですか？",
            "options": ["Webサーバー", "ブラウザ", "アプリケーションサーバー", "データベース"],
            "answer": "データベース"
        },
        {
            "question": "リクエストとは何ですか？",
            "options": [
                "ユーザーが画面を見ること",
                "ユーザーがブラウザを閉じること",
                "ブラウザがサーバーに「こうしてほしい」と伝えること",
                "データベースが情報を返すこと"
            ],
            "answer": "ブラウザがサーバーに「こうしてほしい」と伝えること"
        }
    ]

    section_id = "確認テスト"

    # 初期化
    if "quiz_submitted" not in st.session_state:
        st.session_state.quiz_submitted = False
        st.session_state.quiz_score = 0
        st.session_state.quiz_answers = {}

    # 初回表示または再受験モード
    if not st.session_state.quiz_submitted:
        for i, q in enumerate(questions):
            selected = st.radio(
                f"**Q{i+1}: {q['question']}**",
                q["options"],
                key=f"quiz_q{i}"
            )
            st.session_state.quiz_answers[i] = selected

        if st.button("✅ 回答を提出する"):
            score = 0
            for i, q in enumerate(questions):
                if st.session_state.quiz_answers.get(i) == q["answer"]:
                    score += 1
            st.session_state.quiz_score = score
            st.session_state.quiz_submitted = True
            mark_section_complete_if_all_correct("確認テスト", score, len(questions))

            # ✅ 満点ならこのセクションを完了として記録
            if 'completed' not in st.session_state:
                st.session_state.completed = {}
            st.session_state.completed[section_id] = (score == len(questions))

    # 結果表示
    if st.session_state.quiz_submitted:
        st.markdown("### 結果")
        total = len(questions)
        score = st.session_state.quiz_score
        st.write(f"正解数：{score} / {total}")
        percentage = int(100 * score / total)
        st.progress(percentage / 100)

        if percentage == 100:
            st.success("素晴らしい！全問正解です 🎉 このセクションは完了と記録されました。")
        elif percentage >= 60:
            st.info("よくできました！あと少しで満点です。")
        else:
            st.warning("もう一度内容を見直して、再チャレンジしてみましょう。")

        if st.button("🔄 もう一度テストする"):
            st.session_state.quiz_submitted = False
            st.session_state.quiz_answers = {}
            st.session_state.quiz_score = 0
