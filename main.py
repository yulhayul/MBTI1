import streamlit as st

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="MBTI 단짝 포켓몬 찾기",
    page_icon="⚡",
    layout="centered"
)

# 2. 따뜻한 크림/노란색 톤 스타일 및 큰 글씨 Custom CSS
st.markdown("""
    <style>
    /* 전체 배경 및 기본 폰트 */
    .stApp {
        background-color: #FFFDF0;
        color: #424242;
        font-size: 1.15rem;
    }

    /* 메인 타이틀 스타일 */
    .main-title {
        text-align: center;
        font-size: 2.6rem;
        font-weight: 800;
        color: #E65100;
        margin-bottom: 8px;
    }

    .sub-title {
        text-align: center;
        font-size: 1.25rem;
        color: #795548;
        margin-bottom: 24px;
    }

    /* 포켓몬 카드 스타일 */
    .pokemon-card {
        background-color: #FFFFFF;
        border: 3px solid #FFE082;
        border-radius: 24px;
        padding: 28px;
        box-shadow: 0 10px 20px rgba(255, 193, 7, 0.15);
        text-align: center;
        margin-top: 10px;
    }

    .mbti-badge {
        display: inline-block;
        background-color: #FFE082;
        color: #E65100;
        font-weight: bold;
        font-size: 1.2rem;
        padding: 6px 18px;
        border-radius: 20px;
        margin-bottom: 12px;
    }

    .pokemon-title {
        font-size: 2.2rem;
        font-weight: 800;
        color: #212121;
        margin-bottom: 12px;
    }

    .type-badge {
        display: inline-block;
        background-color: #FFF3E0;
        border: 2px solid #FFB74D;
        color: #E65100;
        font-size: 1.1rem;
        font-weight: bold;
        padding: 4px 14px;
        border-radius: 12px;
        margin-bottom: 16px;
    }

    .info-box {
        background-color: #FFFDE7;
        border-left: 5px solid #FF8F00;
        padding: 16px;
        border-radius: 12px;
        text-align: left;
        font-size: 1.15rem;
        line-height: 1.6;
        color: #37474F;
        margin-top: 16px;
        word-break: keep-all;
    }

    /* 셀렉트박스 글씨 크기 키우기 */
    .stSelectbox label {
        font-size: 1.3rem !important;
        font-weight: bold;
        color: #E65100 !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. MBTI별 단짝 포켓몬 데이터 정의 (구문 오류 수정 완료)
POKEMON_DATA = {
    "ISTJ": {
        "name": "거북왕 (Blastoise)",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/9.png",
        "type": "💧 물",
        "feature": "단단한 껍질과 강력한 물대포를 가진 철벽의 수호자",
        "reason": "책임감이 강하고 규칙을 철저히 지키는 원칙주의자입니다. 거북왕의 단단한 껍질처럼 묵묵하고 신뢰할 수 있는 든든한 조력자입니다."
    },
    "ISFJ": {
        "name": "해피너스 (Blissey)",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/242.png",
        "type": "⚪ 노말",
        "feature": "상처받은 이를 치유해주는 따뜻하고 상스런 포켓몬",
        "reason": "주변 사람들을 지극정성으로 챙기고 배려하는 마음이 깊습니다. 상처받은 동료를 보살피며 언제나 안식처가 되어주는 최강의 수호자입니다."
    },
    "INFJ": {
        "name": "가디안 (Gardevoir)",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/282.png",
        "type": "🔮 초능력 / 🧚 페어리",
        "feature": "트레이너를 지키기 위해 모든 힘을 다하는 신비로운 포켓몬",
        "reason": "통찰력이 뛰어나고 타인의 감정을 깊게 이해하는 마음을 가졌습니다. 소중한 사람을 지키기 위해 강한 직관과 헌신을 발휘합니다."
    },
    "INTJ": {
        "name": "뮤츠 (Mewtwo)",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/150.png",
        "type": "🔮 초능력",
        "feature": "압도적인 지능과 전투 능력을 갖춘 비범한 전략가",
        "reason": "독립적이고 철저한 전략가 타입으로 명확한 분석을 즐깁니다. 깊은 사색과 뛰어난 지능으로 언제나 한발 앞서 문제의 본질을 구상합니다."
    },
    "ISTP": {
        "name": "루카리오 (Lucario)",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/448.png",
        "type": "🥊 격투 / ⚙️ 강철",
        "feature": "파동을 감지하고 냉철하게 문제를 해결하는 장인",
        "reason": "조용하지만 필요할 때 압도적인 행동력을 발휘하는 실용주의자입니다. 상황을 냉철하게 판단하고 순식간에 난관을 헤쳐나갑니다."
    },
    "ISFP": {
        "name": "잠만보 (Snorlax)",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/143.png",
        "type": "⚪ 노말",
        "feature": "느긋하고 온화하며 온 세상을 평화롭게 만드는 포켓몬",
        "reason": "온화하고 마이페이스를 즐기며 현재의 평화를 중요하게 생각합니다. 남에게 피해 주지 않고 자신만의 소소한 행복을 누릴 줄 압니다."
    },
    "INFP": {
        "name": "메타몽 (Ditto)",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/132.png",
        "type": "⚪ 노말",
        "feature": "무엇으로든 변신할 수 있는 무한한 가능성의 포켓몬",
        "reason": "상상력이 풍부하고 타인의 마음에 깊이 공감하는 능력이 있습니다. 말랑말랑하고 유연한 마음을 가져 무한한 가능성을 품고 있습니다."
    },
    "INTP": {
        "name": "고라파덕 (Psyduck)",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/54.png",
        "type": "💧 물",
        "feature": "항상 깊은 생각에 잠겨 있다가 예상치 못한 잠재력을 발휘하는 아이디어파",
        "reason": "호기심이 많고 깊은 생각에 잘 빠지는 독창적인 호기심천국입니다. 고뇌 끝에 예상치 못한
