import streamlit as st
import random
from datetime import date
import streamlit.components.v1 as components

st.set_page_config(page_title="MBTI 연애·직업·스트레스 퀵가이드 긔", layout="centered")

# ---------- MBTI 데이터 (16가지) ----------
mbti_data = {
    "INTJ": {
        "emoji": "🧠",
        "연애스타일": "논리적이고 계획적인 연애를 선호함.  \n잘 맞는 MBTI: ENFP  \n안 맞는 MBTI: ESFP",
        "추천직업": {
            "title": "연구원",
            "desc": "복잡한 문제를 체계적으로 분석함.  \n장기적 비전 수립과 실행을 즐김.  \n데이터와 이론으로 해결책을 도출함.",
            "image": "https://cdn-icons-png.flaticon.com/512/4341/4341139.png"
        },
        "스트레스해결": ["원인 분석으로 문제 해결", "혼자만의 시간 갖기(산책/독서)", "목표 재정리 및 계획 세우기"]
    },
    "INTP": {
        "emoji": "🔍",
        "연애스타일": "아이디어와 대화를 즐기는 관계.  \n잘 맞는 MBTI: ENTJ  \n안 맞는 MBTI: ESFJ",
        "추천직업": {
            "title": "리서처",
            "desc": "지적 호기심으로 깊이 파고듦.  \n논리적 문제 해결에 강함.  \n독립적 프로젝트에서 성과를 냄.",
            "image": "https://cdn-icons-png.flaticon.com/512/201/201623.png"
        },
        "스트레스해결": ["아이디어 정리(노트)", "창작이나 코딩으로 몰입", "조용히 사색하는 시간"]
    },
    "ENTJ": {
        "emoji": "🚀",
        "연애스타일": "주도적이고 목표지향적 관계를 원함.  \n잘 맞는 MBTI: INTP  \n안 맞는 MBTI: ISFP",
        "추천직업": {
            "title": "경영자",
            "desc": "팀을 이끌어 목표 달성 주도.  \n전략적 판단으로 조직 성과 창출.  \n결단력 있는 의사결정 선호.",
            "image": "https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
        },
        "스트레스해결": ["우선순위 재정립", "강도 있는 운동으로 해소", "실행 가능한 계획 세우기"]
    },
    "ENTP": {
        "emoji": "💡",
        "연애스타일": "재미와 자극을 추구하는 관계.  \n잘 맞는 MBTI: INFJ  \n안 맞는 MBTI: ISFJ",
        "추천직업": {
            "title": "창업가",
            "desc": "새로운 아이디어를 빠르게 시도함.  \n불확실성을 즐기며 기회 포착.  \n유연한 사고로 문제 해결.",
            "image": "https://cdn-icons-png.flaticon.com/512/1055/1055687.png"
        },
        "스트레스해결": ["브레인스토밍으로 에너지 전환", "새로운 액티비티 시도", "유머로 분위기 전환"]
    },
    "INFJ": {
        "emoji": "🌙",
        "연애스타일": "깊고 의미 있는 연결을 추구함.  \n잘 맞는 MBTI: ENFP  \n안 맞는 MBTI: ESTP",
        "추천직업": {
            "title": "상담사",
            "desc": "타인의 감정에 공감하고 통찰 제공.  \n신뢰형 관계를 통해 영향력 발휘.  \n사회적 문제 해결에 관심 많음.",
            "image": "https://cdn-icons-png.flaticon.com/512/3062/3062634.png"
        },
        "스트레스해결": ["감정 일기와 정리", "신뢰하는 사람과의 깊은 대화", "자연 속 휴식"]
    },
    "INFP": {
        "emoji": "🎨",
        "연애스타일": "이상적이고 로맨틱한 관계를 꿈꿈.  \n잘 맞는 MBTI: ENFJ  \n안 맞는 MBTI: ESTJ",
        "추천직업": {
            "title": "작가/디자이너",
            "desc": "감성 표현으로 가치 전달함.  \n창작 활동에서 동기 부여를 얻음.  \n개인적 철학을 작품으로 녹여냄.",
            "image": "https://cdn-icons-png.flaticon.com/512/4140/4140043.png"
        },
        "스트레스해결": ["창작으로 감정 표출", "음악/독서로 위안 얻기", "조용한 휴식 취하기"]
    },
    "ENFJ": {
        "emoji": "🤝",
        "연애스타일": "사람 중심의 헌신적인 파트너임.  \n잘 맞는 MBTI: INFP  \n안 맞는 MBTI: ISTP",
        "추천직업": {
            "title": "교사/HR",
            "desc": "타인을 이끄는 능력과 공감력 보유.  \n조직 내에서 조율과 성장 도모.  \n커뮤니케이션 역량이 핵심.",
            "image": "https://cdn-icons-png.flaticon.com/512/2965/2965567.png"
        },
        "스트레스해결": ["신뢰하는 사람과 솔직히 대화", "타인 도우며 만족감 얻기", "충분한 휴식으로 재충전"]
    },
    "ENFP": {
        "emoji": "🌈",
        "연애스타일": "열정적이고 개방적인 연애를 즐김.  \n잘 맞는 MBTI: INTJ  \n안 맞는 MBTI: ISTJ",
        "추천직업": {
            "title": "콘텐츠 크리에이터",
            "desc": "아이디어로 사람들 끌어모음.  \n자유로운 표현으로 영향력 발휘.  \n새로운 경험을 콘텐츠로 전환함.",
            "image": "https://cdn-icons-png.flaticon.com/512/6165/6165547.png"
        },
        "스트레스해결": ["새로운 취미로 에너지 채움", "친구들과의 교류로 해소", "자유로운 표현으로 스트레스 분출"]
    },
    "ISTJ": {
        "emoji": "🗂️",
        "연애스타일": "신중하고 안정적인 연애를 선호함.  \n잘 맞는 MBTI: ESFP  \n안 맞는 MBTI: ENFP",
        "추천직업": {
            "title": "회계사/관리자",
            "desc": "규칙과 절차를 정확히 지킴.  \n책임감으로 신뢰를 쌓음.  \n세부사항 관리에 강함.",
            "image": "https://cdn-icons-png.flaticon.com/512/1086/1086933.png"
        },
        "스트레스해결": ["루틴으로 안정 찾기", "체계적으로 문제 정리", "충분한 수면과 규칙적 운동"]
    },
    "ISFJ": {
        "emoji": "🛡️",
        "연애스타일": "헌신적이고 배려 깊은 파트너임.  \n잘 맞는 MBTI: ESFP  \n안 맞는 MBTI: ENTP",
        "추천직업": {
            "title": "간호사/행정",
            "desc": "다른 사람 돌보는 데 강함.  \n세심한 관찰력으로 신뢰 얻음.  \n안정적 환경에서 성과 발휘.",
            "image": "https://cdn-icons-png.flaticon.com/512/2965/2965567.png"
        },
        "스트레스해결": ["돌봄 받기(가까운 사람과 시간)", "작은 일상 루틴 유지", "편안한 환경 만들기"]
    },
    "ESTJ": {
        "emoji": "🧭",
        "연애스타일": "실용적이고 책임감 있는 연애를 함.  \n잘 맞는 MBTI: ISTP  \n안 맞는 MBTI: INFP",
        "추천직업": {
            "title": "운영/관리자",
            "desc": "조직 운영과 관리에 능함.  \n결과 중심으로 일 처리함.  \n명확한 규칙과 절차 선호.",
            "image": "https://cdn-icons-png.flaticon.com/512/149/149071.png"
        },
        "스트레스해결": ["실행 가능한 해결책 세우기", "체력 단련으로 해소", "목표 재설정 및 계획"]
    },
    "ESFJ": {
        "emoji": "🎀",
        "연애스타일": "따뜻하고 세심하게 챙기는 스타일.  \n잘 맞는 MBTI: ISFP  \n안 맞는 MBTI: INTP",
        "추천직업": {
            "title": "이벤트/서비스",
            "desc": "사람을 챙기고 분위기 조성 잘함.  \n대인관계에서 강점 발휘.  \n서비스 마인드로 신뢰 형성.",
            "image": "https://cdn-icons-png.flaticon.com/512/2921/2921822.png"
        },
        "스트레스해결": ["사교적 활동으로 위로받기", "가족/친구와 시간 보내기", "정리로 마음 안정"]
    },
    "ISTP": {
        "emoji": "🔧",
        "연애스타일": "실용적이고 즉흥적인 연애를 즐김.  \n잘 맞는 MBTI: ESFJ  \n안 맞는 MBTI: ENFJ",
        "추천직업": {
            "title": "기술자/정비사",
            "desc": "손으로 하는 문제 해결에 능숙함.  \n실용적 결과를 빠르게 만들어냄.  \n현장 중심 활동에 적합.",
            "image": "https://cdn-icons-png.flaticon.com/512/2721/2721299.png"
        },
        "스트레스해결": ["손으로 무언가 만들기(공예/수리)", "짧은 혼자만의 시간", "신체활동으로 에너지 소비"]
    },
    "ISFP": {
        "emoji": "🌿",
        "연애스타일": "감성적이고 현재를 즐기는 연애.  \n잘 맞는 MBTI: ESFJ  \n안 맞는 MBTI: ENTJ",
        "추천직업": {
            "title": "아티스트/디자이너",
            "desc": "감성 표현으로 사람과 소통함.  \n미적 감각으로 차별화된 결과 창출.  \n자유로운 환경에서 창의력 발휘.",
            "image": "https://cdn-icons-png.flaticon.com/512/4140/4140043.png"
        },
        "스트레스해결": ["예술적 표현으로 정리", "자연 속에서 재충전", "감정 일기로 정리"]
    },
    "ESTP": {
        "emoji": "⚡",
        "연애스타일": "활동적이고 즉흥적인 연애를 선호함.  \n잘 맞는 MBTI: ISFJ  \n안 맞는 MBTI: INFJ",
        "추천직업": {
            "title": "세일즈/응급구조",
            "desc": "즉각적 판단과 행동으로 성과 냄.  \n현장 중심의 빠른 대처 능력 보유.  \n도전적 과제에서 빛남.",
            "image": "https://cdn-icons-png.flaticon.com/512/1051/1051277.png"
        },
        "스트레스해결": ["강도 높은 운동으로 분출", "즉시 행동으로 문제 해결", "친구들과 활동으로 기분 전환"]
    },
    "ESFP": {
        "emoji": "🎉",
        "연애스타일": "사교적이고 즐거움을 주는 연애를 함.  \n잘 맞는 MBTI: ISTJ  \n안 맞는 MBTI: INTJ",
        "추천직업": {
            "title": "퍼포머/이벤트",
            "desc": "무대와 사람 앞에서 기량 발휘.  \n즉흥성과 에너지로 분위기 장악.  \n사람을 즐겁게 하는 능력 탁월.",
            "image": "https://cdn-icons-png.flaticon.com/512/2921/2921822.png"
        },
        "스트레스해결": ["파티나 모임으로 전환", "즉흥적인 여행으로 리셋", "창의적 표현으로 해소"]
    }
}

# ---------- 헬퍼: 이모지 애니메이션 HTML 생성 ----------
def generate_emoji_animation_html(emoji: str, count: int = 10, height_px: int = 220):
    # 랜덤 위치와 애니메이션 설정을 서버 사이드에서 생성해서 HTML에 넣음
    elems = []
    for i in range(count):
        top = random.randint(0, 85)
        left = random.randint(0, 85)
        size = random.randint(24, 48)  # px
        dur = round(random.uniform(2.5, 5.0), 2)
        delay = round(random.uniform(0, 1.5), 2)
        rotate = random.randint(-25, 25)
        opacity = round(random.uniform(0.7, 1.0), 2)
        z = random.randint(1, 999)
        elem = f"""
        <div class="emoji" style="
            top:{top}%; left:{left}%; font-size:{size}px; 
            animation-duration:{dur}s; animation-delay:{delay}s; 
            transform: rotate({rotate}deg);
            opacity:{opacity};
            z-index:{z};
        ">{emoji}</div>
        """
        elems.append(elem)

    html = f"""
    <div class="emoji-wrap" style="position:relative; width:100%; height:{height_px}px; overflow:hidden;">
        {''.join(elems)}
    </div>
    <style>
    .emoji-wrap .emoji {{
        position:absolute;
        user-select:none;
        -webkit-user-select:none;
        pointer-events:none;
        animation-name:floatMove;
        animation-timing-function: ease-in-out;
        animation-iteration-count: infinite;
    }}
    @keyframes floatMove {{
      0% {{ transform: translateY(0px) rotate(0deg); }}
      25% {{ transform: translateY(-12px) rotate(5deg); }}
      50% {{ transform: translateY(0px) rotate(0deg); }}
      75% {{ transform: translateY(8px) rotate(-5deg); }}
      100% {{ transform: translateY(0px) rotate(0deg); }}
    }}
    </style>
    """
    return html

# ---------- UI: 헤더 ----------
st.title("😜 MBTI 연애·직업·스트레스 퀵가이드 긔 😜")
st.caption("니 MBTI 골라서 바로 분석받아라긔 — 결과 나올 때 이모지 10개 튀어나와~")

# ---------- MBTI 인터랙션 ----------
mbti_list = list(mbti_data.keys())
selected_mbti = st.selectbox("👉 니 MBTI 뭐긔? 골라봐", mbti_list, index=mbti_list.index("INTJ") if "INTJ" in mbti_list else 0,
                             format_func=lambda x: f"{mbti_data[x]['emoji']}  {x}")

category = st.radio("📌 카테고리 찍어라 긔", ("연애스타일", "추천직업", "스트레스 해결법"))

mbti_info = mbti_data[selected_mbti]

# 애니메이션 (MBTI 결과가 보일 때마다)
anim_html = generate_emoji_animation_html(mbti_info["emoji"], count=10, height_px=200)
components.html(anim_html, height=200, scrolling=False)

# 결과 헤더
st.markdown(f"### {mbti_info['emoji']}  {selected_mbti} 타입 분석 들어간다긔 😎")

if category == "연애스타일":
    # 연애스타일은 3줄로 고정: 일반설명, 잘맞는MBTI, 안맞는MBTI
    love_md = mbti_info["연애스타일"].replace("\n", "  \n")
    st.markdown(love_md)
elif category == "추천직업":
    job = mbti_info["추천직업"]
    st.markdown(f"**추천 직업 — {job['title']}**")
    st.markdown(job["desc"].replace("\n", "  \n"))
    # 이미지 표시
    try:
        st.image(job["image"], width=160)
    except Exception:
        st.write("이미지 로드 실패했긔")
else:
    st.markdown("**스트레스 받을 때 이렇게 해라긔**")
    for i, s in enumerate(mbti_info["스트레스해결"], 1):
        st.markdown(f"{i}. {s}")

# 전체 목록 보기
with st.expander("🔍 모든 유형 한눈에 보기 긔"):
    cols = st.columns(4)
    for idx, key in enumerate(mbti_list):
        col = cols[idx % 4]
        item = mbti_data[key]
        col.markdown(f"**{item['emoji']} {key}**")
        # 간단 요약 한 줄
        one_line = item["연애스타일"].split("  \n")[0]
        col.write(one_line)

st.markdown("---")

# ---------- 생년월일 분석 파트 (별개) ----------
st.header("🎂 생년월일 기반 5줄 분석 (MBTI 영역과 별개긔)")

birth_date = st.date_input("니 태어난 날짜 찍어봐라 긔", value=date(2000,1,1))
# 날짜가 선택될 때마다 결과를 보여줘야 함 -> 즉시 반영
st.write(f"너 태어난 날: **{birth_date.isoformat()}** 긔")

birth_cat = st.radio("분석 카테고리 골라라 긔", ("연애유형 5줄", "추천직업 5줄", "스트레스 해소법 5줄"))

# 간단히 날짜 기반으로 변화를 주는 deterministic seed
seed = birth_date.year + birth_date.month + birth_date.day
random.seed(seed)

# 템플릿 목록 (각 카테고리에서 랜덤하지만 날짜에 따라 고정)
love_templates = [
    [
        "1. 감정 표현이 진솔하고 깊음.",
        "2. 파트너의 가치관을 중요하게 여김.",
        "3. 안정감 있는 관계를 선호함.",
        "4. 신뢰 구축에 많은 노력을 기울임.",
        "5. 장기적 관계 유지에 강점이 있음."
    ],
    [
        "1. 로맨틱한 행동으로 애정 표현함.",
        "2. 대화로 친밀감 형성함.",
        "3. 상대의 자율성도 존중함.",
        "4. 갈등 시에는 시간 갖고 풀려고 함.",
        "5. 작은 이벤트로 사랑을 표현함."
    ],
    [
        "1. 즉흥적이면서도 진심을 담아 관계에 임함.",
        "2. 공감 능력이 뛰어나 대화가 좋음.",
        "3. 상대의 성장에 관심이 많음.",
        "4. 가끔은 혼자만의 시간이 필요함.",
        "5. 깊은 신뢰를 바탕으로 안정감 제공함."
    ]
]

job_templates = [
    [
        "1. 창의력과 분석력을 모두 살릴 수 있음.",
        "2. 사람과의 협업에서 장점 발휘함.",
        "3. 프로젝트 기획 및 실행에 적합함.",
        "4. 문제 해결 과정에서 뛰어난 집중력 보임.",
        "5. 교육/상담/기획 분야에서 성과 기대됨."
    ],
    [
        "1. 현장 중심의 실무에 강점이 있음.",
        "2. 기술적 문제 해결에 흥미를 느낌.",
        "3. 팀 내 역할 분담에서 신뢰받음.",
        "4. 책임감 있는 포지션에 적합함.",
        "5. 운영/관리 관련 직무에서 잘 맞음."
    ],
    [
        "1. 창작과 표현이 어우러진 직업 추천됨.",
        "2. 자유로운 환경에서 더 좋은 성과를 냄.",
        "3. 대중과 소통하는 역할에서 빛남.",
        "4. 자기주도적으로 성장 가능한 직군.",
        "5. 콘텐츠, 디자인, 문화예술 분야 적합."
    ]
]

stress_templates = [
    [
        "1. 자연 속 산책으로 빠르게 안정됨.",
        "2. 좋아하는 음악을 듣거나 연주하면 회복됨.",
        "3. 신뢰하는 사람과 솔직한 대화로 해소됨.",
        "4. 짧은 휴식과 취미 몰입이 효과적임.",
        "5. 규칙적 운동으로 에너지 정리 가능."
    ],
    [
        "1. 체계적으로 문제를 정리하면 안심함.",
        "2. 글쓰기나 일기로 감정을 털어내기 좋음.",
        "3. 가벼운 신체 활동으로 긴장 완화됨.",
        "4. 취미에 몰입해 스트레스 분산됨.",
        "5. 충분한 수면으로 재충전하기."
    ],
    [
        "1. 친구들과의 소소한 만남으로 해소됨.",
        "2. 창작 활동으로 감정 전환 가능.",
        "3. 즉각적인 행동으로 문제 해결 시 만족감 큼.",
        "4. 명상이나 호흡으로 마음 안정 찾기.",
        "5. 자연이나 예술로 감정 정리하기."
    ]
]

# 선택된 템플릿 인덱스는 seed로 정해짐
idx = seed % 3

if birth_cat.startswith("연애유형"):
    st.markdown("### 연애유형 5줄 풀어줄게 긔")
    for line in love_templates[idx]:
        st.write(line)
elif birth_cat.startswith("추천직업"):
    st.markdown("### 추천직업 5줄 풀어줄게 긔")
    for line in job_templates[idx]:
        st.write(line)
else:
    st.markdown("### 스트레스 해소법 5줄 풀어줄게 긔")
    for line in stress_templates[idx]:
        st.write(line)

# 끝 — 화면 하단 여백
st.markdown("---")
st.caption("원하면 다시 골라라긔. 너는 할 수 있다긔")
