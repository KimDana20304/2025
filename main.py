import streamlit as st
import random

st.set_page_config(page_title="MBTI 직업 & 연애 스타일 & 생년월일 분석", layout="centered")

# 샘플 직업 이미지 URL
job_images = {
    "연구원": "https://cdn-icons-png.flaticon.com/512/4341/4341139.png",
    "전략기획": "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
    "소프트웨어 엔지니어": "https://cdn-icons-png.flaticon.com/512/2721/2721299.png",
    "데이터 과학자": "https://cdn-icons-png.flaticon.com/512/865/865672.png",
    "창업가": "https://cdn-icons-png.flaticon.com/512/1055/1055687.png",
    "마케터": "https://cdn-icons-png.flaticon.com/512/1087/1087840.png",
    "기획자": "https://cdn-icons-png.flaticon.com/512/3187/3187880.png",
    "크리에이터": "https://cdn-icons-png.flaticon.com/512/6165/6165547.png",
}

# MBTI 데이터
mbti_data = {
    "INTJ": {
        "emoji": "🧠",
        "연애스타일": "논리적이고 계획적인 연애, 깊은 대화와 목표 공유 선호, 공간 존중\n잘 맞는 MBTI: ENFP\n안 맞는 MBTI: ESFP",
        "추천직업": {
            "설명": "연구원, 전략기획, 소프트웨어 엔지니어, 데이터 과학자\n- 복잡한 문제를 분석하고 전략을 세움\n- 장기적인 비전을 실현함\n- 체계적 접근으로 성과 창출",
            "이미지": job_images["연구원"]
        },
        "스트레스해결": ["문제의 원인 분석하기", "혼자만의 시간 갖기(책/산책)", "목표 재정리 및 계획 세우기"]
    },
    "INTP": {
        "emoji": "🔍",
        "연애스타일": "아이디어 중심의 대화형 연애, 자유로운 관계 선호, 관찰자 모드\n잘 맞는 MBTI: ENTJ\n안 맞는 MBTI: ESFJ",
        "추천직업": {
            "설명": "연구자, 프로그래머, UX 리서처, 학술 분야\n- 지식 탐구를 즐김\n- 논리적 문제 해결 능력 발휘\n- 독립적으로 프로젝트 수행",
            "이미지": job_images["데이터 과학자"]
        },
        "스트레스해결": ["아이디어 정리(노트)", "창작 활동", "혼자 사색하는 시간"]
    },
    "ENTJ": {
        "emoji": "🚀",
        "연애스타일": "주도적이고 목표지향적, 함께 성장하는 관계 선호, 직설적\n잘 맞는 MBTI: INTP\n안 맞는 MBTI: ISFP",
        "추천직업": {
            "설명": "경영자, 프로젝트 매니저, 변호사, 컨설턴트\n- 팀을 이끌고 목표 달성\n- 전략적 판단력 발휘\n- 큰 규모의 의사결정 주도",
            "이미지": job_images["전략기획"]
        },
        "스트레스해결": ["우선순위 재정립", "운동으로 에너지 발산", "실행 계획 세우기"]
    },
    "ENTP": {
        "emoji": "💡",
        "연애스타일": "재미와 자극 중시, 토론과 도전 즐김, 에너지 폭발\n잘 맞는 MBTI: INFJ\n안 맞는 MBTI: ISFJ",
        "추천직업": {
            "설명": "창업가, 마케터, 기획자, 크리에이터\n- 새로운 아이디어 사업화\n- 도전적 프로젝트 주도\n- 창의적이고 유연한 접근",
            "이미지": job_images["창업가"]
        },
        "스트레스해결": ["아이디어 브레인스토밍", "새로운 활동 시도", "유머로 분위기 전환"]
    },
    "INFJ": {
        "emoji": "🌙",
        "연애스타일": "깊고 의미 있는 연결, 감정 이해 중시, 헌신적\n잘 맞는 MBTI: ENFP\n안 맞는 MBTI: ESTP",
        "추천직업": {
            "설명": "상담사, 작가, 교육자, 사회복지사\n- 사람들의 내면 이해\n- 사회에 긍정적 영향\n- 감정적 통찰력 발휘",
            "이미지": "https://cdn-icons-png.flaticon.com/512/3062/3062634.png"
        },
        "스트레스해결": ["감정 일기 쓰기", "신뢰하는 사람과 대화", "자연 속 휴식"]
    },
    # 나머지 11개 MBTI도 동일 구조로 입력 (생략 없이 채우면 됨)
}

# MBTI 선택 UI
st.markdown("<h1 style='text-align:center;'>😜 MBTI 연애·직업·스트레스 퀵 가이드 😜</h1>", unsafe_allow_html=True)
mbti_list = list(mbti_data.keys())
selected = st.selectbox("👉 니 MBTI 뭐긔? 골라봐", mbti_list, format_func=lambda x: f"{mbti_data[x]['emoji']}  {x}")
category = st.radio("📌 카테고리 찍어라", ("연애스타일", "추천직업", "스트레스 해결법"))
data = mbti_data[selected]

# 이모티콘 애니메이션 함수
def random_emojis(emoji, count=10):
    positions = [(random.randint(0, 90), random.randint(0, 90)) for _ in range(count)]
    animation_html = "<div style='position:relative;height:200px;'>"
    for top, left in positions:
        animation_html += f"""
        <div style='position:absolute;top:{top}%;left:{left}%;
        animation: float 3s ease-in-out infinite; font-size:2rem;'>{emoji}</div>
        """
    animation_html += """
    <style>
    @keyframes float {
      0% {transform: translateY(0px);}
      50% {transform: translateY(-10px);}
      100% {transform: translateY(0px);}
    }
    </style>
    </div>
    """
    return animation_html

st.markdown(random_emojis(data['emoji']), unsafe_allow_html=True)

# 결과 출력
st.markdown(f"## {data['emoji']} {selected} 타입 분석 들어간다긔😎")
if category == "연애스타일":
    st.write(data["연애스타일"])
elif category == "추천직업":
    st.write(data["추천직업"]["설명"])
    st.image(data["추천직업"]["이미지"], width=150)
else:
    st.write("😤 스트레스 받을 땐 이렇게 하긔")
    for i, item in enumerate(data["스트레스해결"], 1):
        st.write(f"{i}. {item}")

# 전체 목록
with st.expander("🔍 모든 유형 한눈에 보기"):
    cols = st.columns(2)
    for idx, key in enumerate(mbti_list):
        col = cols[idx % 2]
        col.markdown(f"**{mbti_data[key]['emoji']} {key}**")
        col.write(mbti_data[key]["연애스타일"].split("\n")[0] + "...")

# -------------------------------------------
# 생년월일 분석 파트
st.markdown("---")
st.markdown("## 🎂 생년월일 기반 분석 들어간다긔")

birth_date = st.date_input("너 태어난 날짜 찍어봐라")
if birth_date:
    st.write(f"📅 네 생일은 {birth_date} 긔")

    birth_category = st.radio("카테고리 골라라", ("연애유형", "추천직업", "스트레스 해소법"))

    if birth_category == "연애유형":
        st.write("1. 감정 공감 능력이 뛰어나 연애에 진심임")
        st.write("2. 사랑 표현을 아끼지 않음")
        st.write("3. 파트너를 챙기고 안정감을 줌")
        st.write("4. 다만 기분 기복이 있을 수 있음")
        st.write("5. 장기적인 관계 유지에 강점이 있음")
    elif birth_category == "추천직업":
        st.write("1. 사람을 다루는 직종에 강점이 있음")
        st.write("2. 협력과 조율이 필요한 직업에 적합함")
        st.write("3. 창의성과 실행력을 모두 발휘 가능")
        st.write("4. 팀워크 중심 환경에서 성과를 냄")
        st.write("5. 교육, 상담, 기획 분야 추천")
    else:
        st.write("1. 자연 속에서 휴식하기")
        st.write("2. 신뢰하는 사람과 속마음 나누기")
        st.write("3. 좋아하는 취미에 몰입하기")
        st.write("4. 음악이나 예술 감상")
        st.write("5. 가벼운 운동과 명상")
