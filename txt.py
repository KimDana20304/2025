import streamlit as st
import random
import urllib.parse

# 페이지 설정
st.set_page_config(page_title="꿈 분석 & 심리 테스트", layout="centered")

# CSS 스타일 적용
st.markdown(
    """
    <style>
    body {
        background: radial-gradient(circle at 20% 0%, rgba(122,162,255,0.15), transparent 50%),
                    radial-gradient(circle at 80% 100%, rgba(255,182,193,0.15), transparent 50%);
        font-family: 'Arial', sans-serif;
    }
    .result-box {
        padding: 15px;
        border-radius: 12px;
        background-color: #f8f9fa;
        margin-top: 20px;
        font-size: 18px;
    }
    .share-box {
        background-color: #eef2ff;
        padding: 10px;
        border-radius: 10px;
        margin-top: 15px;
        font-size: 14px;
        word-wrap: break-word;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🌙 꿈 분석 & 심리 테스트")

# 입력창
mbti = st.text_input("당신의 MBTI를 입력하세요 (예: INFP)")
dream = st.text_area("원하는 꿈을 입력하세요")

# 심리 테스트 문항
questions = [
    "이 꿈은 당신에게 희망을 줍니까?",
    "이 꿈을 위해 노력할 준비가 되어 있습니까?",
    "이 꿈을 이루면 자신감이 생길 것 같습니까?",
    "이 꿈이 현재 당신의 삶에 중요한가요?",
    "이 꿈을 생각하면 기분이 좋아지나요?"
]
answers = []

if mbti and dream:
    st.subheader("✅ 당신의 꿈 분석")
    analysis = f"'{dream}'은(는) {mbti} 성향을 가진 사람에게 매우 의미 있는 목표입니다. 이 꿈은 당신의 창의성과 성격적 강점을 반영하고 있습니다."
    st.markdown(f"<div class='result-box'>{analysis}</div>", unsafe_allow_html=True)

    st.subheader("🧠 간단 심리 테스트")
    for idx, q in enumerate(questions):
        ans = st.radio(q, ["예", "아니오"], key=f"q{idx}")
        answers.append(ans)

    if st.button("결과 보기"):
        score = answers.count("예")
        if score >= 4:
            mood = "당신은 꿈에 대한 확신과 열정이 매우 강합니다."
        elif score == 3:
            mood = "당신은 꿈에 대해 긍정적이지만 약간의 불안감이 있습니다."
        else:
            mood = "당신은 꿈에 대해 아직 확신이 부족합니다."

        st.subheader("📌 심리 결과")
        st.markdown(f"<div class='result-box'>{mood}</div>", unsafe_allow_html=True)

        # ✅ 결과 공유 URL 생성
        base_url = "https://dream-mbti-app.com/share"
        params = urllib.parse.urlencode({"mbti": mbti, "dream": dream, "result": mood})
        share_url = f"{base_url}?{params}"

        st.write("🔗 결과 공유하기:")
        st.markdown(f"<div class='share-box'>{share_url}</div>", unsafe_allow_html=True)

        # ✅ 클립보드 복사 버튼 (Streamlit + JS)
        st.markdown(
            f"""
            <button onclick="navigator.clipboard.writeText('{share_url}')" style="padding:10px 15px; background:#4F46E5; color:white; border:none; border-radius:8px; cursor:pointer;">
                📋 URL 복사
            </button>
            """,
            unsafe_allow_html=True
        )
