import streamlit as st
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

    if "quiz_submitted" not in st.session_state:
        st.session_state.quiz_submitted = False
        st.session_state.quiz_score = 0
        st.session_state.quiz_answers = {}

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
            st.success("回答を提出しました。")
    else:
        st.markdown("### 🧾 結果")
        st.write(f"正解数：{st.session_state.quiz_score} / {len(questions)}")
        percentage = int(100 * st.session_state.quiz_score / len(questions))
        st.progress(percentage / 100)

        if percentage == 100:
            st.success("素晴らしい！全問正解です 🎉")
        elif percentage >= 60:
            st.info("よくできました！もう一度見直すとさらに理解が深まります。")
        else:
            st.warning("もう一度内容を読み直してみましょう。")

        if st.button("🔄 もう一度テストする"):
            st.session_state.quiz_submitted = False
            st.session_state.quiz_answers = {}
            st.session_state.quiz_score = 0
