
import streamlit as st
import pandas as pd

st.set_page_config(page_title="MBTI 직업 추천 앱", page_icon="💼", layout="centered")

st.title("MBTI 기반 직업 추천 앱")
st.caption("간단한 MBTI 검사 또는 직접 유형 선택으로 맞춤 직업을 추천해요")

# MBTI 검사
st.subheader("1) MBTI 검사하기 또는 직접 선택하기")
col1, col2 = st.columns([2, 1])
with col1:
    q1 = st.radio("1. 사람들과 만나서 에너지를 얻나? (E) / 혼자서 충전하나? (I)", ("E", "I"))
    q2 = st.radio("2. 사실과 현실을 중시하나? (S) / 가능성과 아이디어를 중시하나? (N)", ("S", "N"))
    q3 = st.radio("3. 결정을 할 때 논리와 원칙을 따르나? (T) / 사람과 가치에 더 신경쓰나? (F)", ("T", "F"))
    q4 = st.radio("4. 계획적이고 정리된 편인가? (J) / 유연하고 즉흥적인 편인가? (P)", ("J", "P"))
with col2:
    mbti_manual = st.selectbox("직접 MBTI 선택하기", ("", "INTJ", "INTP", "ENTJ", "ENTP", "INFJ", "INFP", "ENFJ", "ENFP",
                                                   "ISTJ", "ISFJ", "ESTJ", "ESFJ", "ISTP", "ISFP", "ESTP", "ESFP"))

if mbti_manual:
    mbti = mbti_manual
else:
    mbti = q1 + q2 + q3 + q4

st.markdown(f"### 선택된 MBTI: **{mbti}**")

# MBTI별 추천 직업
MBTI_JOB_MAP = {
    'INTJ': ["전략기획자", "데이터과학자", "연구원"],
    'INTP': ["연구원", "소프트웨어 엔지니어", "데이터 분석가"],
    'ENTJ': ["경영진/리더", "프로젝트 매니저", "컨설턴트"],
    'ENTP': ["스타트업 창업가", "제품기획자", "광고 기획자"],
    'INFJ': ["상담사", "작가", "교육 기획자"],
    'INFP': ["문학/콘텐츠 창작", "디자이너", "상담 관련 직업"],
    'ENFJ': ["인사/조직 개발", "교사/강사", "커뮤니케이션 전문가"],
    'ENFP': ["마케팅/브랜딩", "창의적]()
