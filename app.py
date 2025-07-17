import streamlit as st

st.set_page_config(page_title="5등급제 → 9등급제 환산기", page_icon="📊")

st.title("📊 5등급제 → 9등급제 환산기")

st.markdown("""
이 웹앱은 5등급제의 등급과 백분위를 입력하면,  
누적 기준으로 9등급제의 등급으로 자동 환산해줍니다.
""")

# 사용자 입력
five_grade = st.selectbox("5등급제 등급 (1~5)", [1, 2, 3, 4, 5])
percentile = st.slider("해당 백분위 (%)", 0, 100, 50)

# 환산 함수
def convert_to_9grade(p):
    if p <= 4:
        return 1
    elif p <= 11:
        return 2
    elif p <= 23:
        return 3
    elif p <= 40:
        return 4
    elif p <= 60:
        return 5
    elif p <= 77:
        return 6
    elif p <= 89:
        return 7
    elif p <= 96:
        return 8
    else:
        return 9

# 결과 출력
if st.button("9등급으로 환산하기"):
    result = convert_to_9grade(percentile)
    st.success(f"✔ 9등급제 환산 결과: **{result}등급**입니다.")
