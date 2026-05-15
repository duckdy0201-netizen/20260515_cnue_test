import streamlit as st

st.set_page_config(
    page_title="자기소개 페이지",
    page_icon="👋",
    layout="centered",
)

st.title("👋 안녕하세요!")
st.subheader("간단한 자기소개 페이지에 오신 것을 환영합니다.")

st.markdown("---")

st.header("소개")
st.write(
    "안녕하세요, 저는 곽다연입니다.\n"
    "청주교육대학교 대학생으로, 관심 분야를 차차 채워갈 예정입니다."
)

st.header("나에 대해")
st.write(
    "저는 교육학과 26학번 07년생 곽다연입니다.\n"
    "동아리는 버터플라이와 청운복지회를 하고 있습니다."
)

st.header("기술 / 관심사")
st.write(
    "- 동기들과 뽀로로처럼 놀기"
)

st.header("연락처")
st.write(
    "이메일: duckdy0201@gmail.com"
)

st.markdown("---")
st.info("이 페이지는 기본 자기소개 템플릿입니다. 내용을 수정하며 원하는 스타일로 바꿔보세요.")
