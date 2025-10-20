# park_quiz_streamlit.py
import streamlit as st
import random

# ページ設定
st.set_page_config(
    page_title="公園規模クイズゲーム",
    page_icon="🌳",
    layout="centered"
)

# 問題データ
questions = [
    {
        'question': 'ある公園まで「徒歩5分」の距離からほぼ毎日来園する人が多いです。この公園の規模は？',
        'options': ['大規模公園', '小規模公園'],
        'answer': 1,
        'explanation': '✅ 正解！小規模公園（街区公園など）は「近い」が最大の理由で、徒歩圏内からの日常的な利用が中心です。'
    },
    {
        'question': '自動車で来園する人が75%以上を占める公園の規模は？',
        'options': ['大規模公園', '小規模公園'],
        'answer': 0,
        'explanation': '✅ 正解！大規模公園は遠方からの来園が多く、自動車でのアクセスが主流です。広域公園では75.9%が自動車利用。'
    },
    {
        'question': '平均在園時間が2時間以上になることが多い公園の規模は？',
        'options': ['大規模公園', '小規模公園'],
        'answer': 0,
        'explanation': '✅ 正解！大規模公園は目的地としての利用が多く、運動公園で2.32時間、国営公園で2.25時間など、滞在時間が長い傾向があります。'
    },
    {
        'question': '「近い」という理由で選択されることが圧倒的に多い公園の規模は？',
        'options': ['大規模公園', '小規模公園'],
        'answer': 1,
        'explanation': '✅ 正解！小規模公園では「近い」が最大の選択理由です（街区公園で67.9%）。'
    },
    {
        'question': '来園者の約50%が「500m未満」の距離から来園する公園の規模は？',
        'options': ['大規模公園', '小規模公園'],
        'answer': 1,
        'explanation': '✅ 正解！小規模公園では近距離からの利用が多く、街区公園の49.1%が500m未満からの来園です。'
    },
    {
        'question': '「緑が多い」「広い」という理由で選択されることが多い公園の規模は？',
        'options': ['大規模公園', '小規模公園'],
        'answer': 0,
        'explanation': '✅ 正解！大規模公園では「緑が多い」（国営公園40.4%）、「広い」が主要な選択理由となります。'
    }
]

def initialize_session_state():
    """セッション状態を初期化"""
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.answered' = False
        st.session_state.selected_answer' = None
        st.session_state.questions' = questions.copy()
        random.shuffle(st.session_state.questions')
        st.session_state.game_over' = False

def show_question():
    """現在の問題を表示"""
    q = st.session_state.questions'[st.session_state.current_question']
    
    st.subheader(f"Q{st.session_state.current_question + 1}: {q['question']}")
    st.write("---")
    
    # 選択肢ボタン
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button(q['options'][0], use_container_width=True, 
                    disabled=st.session_state.answered'):
            check_answer(0)
    
    with col2:
        if st.button(q['options'][1], use_container_width=True,
                    disabled=st.session_state.answered'):
            check_answer(1)
    
    # 解説表示
    if st.session_state.answered':
        q = st.session_state.questions'[st.session_state.current_question']
        st.info(q['explanation'])
        
        # 次へボタン
        if st.button("次の問題へ →", type="primary"):
            next_question()

def check_answer(selected_index):
    """答えをチェック"""
    st.session_state.answered' = True
    st.session_state.selected_answer' = selected_index
    
    q = st.session_state.questions'[st.session_state.current_question']
    if selected_index == q['answer']:
        st.session_state.score += 1
    st.rerun()

def next_question():
    """次の問題へ進む"""
    st.session_state.current_question += 1
    st.session_state.answered' = False
    st.session_state.selected_answer' = None
    
    if st.session_state.current_question >= len(st.session_state.questions'):
        st.session_state.game_over' = True
    st.rerun()

def show_result():
    """最終結果を表示"""
    total_questions = len(st.session_state.questions')
    percentage = (st.session_state.score / total_questions) * 100
    
    st.balloons()
    st.success("🎯 ゲームクリア！")
    
    # 結果表示
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("正解数", f"{st.session_state.score}/{total_questions}")
    with col2:
        st.metric("正答率", f"{percentage:.1f}%")
    with col3:
        if percentage >= 80:
            st.metric("評価", "🏆 優秀")
        elif percentage >= 60:
            st.metric("評価", "👍 良好")
        else:
            st.metric("評価", "💪 練習中")
    
    # 評価メッセージ
    st.write("---")
    if percentage >= 80:
        st.success("**🏆 優秀！** あなたは公園の達人です！")
    elif percentage >= 60:
        st.info("**👍 良好！** 公園の特性をよく理解しています")
    else:
        st.warning("**💪 もう一度復習してみましょう**")
    
    # 学習のポイント
    st.write("---")
    st.subheader("📊 学習のポイント")
    col1, col2 = st.columns(2)
    with col1:
        st.write("**小規模公園の特徴:**")
        st.write("• 近距離からの利用")
        st.write("• 短時間の利用")
        st.write("• 日常的な利用")
        st.write("• 徒歩・自転車でのアクセス")
    
    with col2:
        st.write("**大規模公園の特徴:**")
        st.write("• 遠方からの利用")
        st.write("• 長時間の滞在")
        st.write("• レジャー的な利用")
        st.write("• 自動車でのアクセス")
    
    # リスタートボタン
    st.write("---")
    if st.button("🔄 もう一度プレイする", type="primary"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

def main():
    # セッション状態の初期化
    initialize_session_state()
    
    # ヘッダー
    st.title("🌳 公園規模クイズゲーム")
    st.markdown("**大規模公園 vs 小規模公園の利用者行動特性を学ぼう！**")
    
    # ゲーム説明
    with st.expander("ℹ️ ゲームの説明", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            st.write("**小規模公園**")
            st.caption("10ha未満（街区公園、近隣公園など）")
        with col2:
            st.write("**大規模公園**")
            st.caption("10ha以上（総合公園、広域公園など）")
    
    st.write("---")
    
    # 進捗表示
    if not st.session_state.game_over':
        progress = st.session_state.current_question / len(st.session_state.questions')
        st.progress(progress)
        st.caption(f"進捗: {st.session_state.current_question + 1}/{len(st.session_state.questions')}問目")
        
        # スコア表示
        st.metric("現在のスコア", f"{st.session_state.score}点")
    
    # ゲーム画面表示
    if st.session_state.game_over':
        show_result()
    else:
        show_question()

if __name__ == "__main__":
    main()