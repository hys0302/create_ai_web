import streamlit as st
import google.generativeai as genai

# 사이드바에서 API 키 입력 받기
st.sidebar.title("API 설정")
api_key = st.sidebar.text_input("Google Gemini API 키를 입력하세요", type="password")

# API 키가 입력되었는지 확인
if api_key:
    # API 키 설정
    genai.configure(api_key=api_key)

    # Streamlit 페이지 제목 설정
    st.title("원영적 사고 생성기")

    # 생성 설정
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    # 모델 초기화
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    # 사용자 입력 받기
    user_input = st.text_area("당신의 슬픈 기분을 입력하세요", 
                              "예: 오늘 급식이 맛이 없어서 슬퍼.")

    if st.button("상장 생성"):
        # 인공지능 모델을 사용하여 상장 생성
        response = model.generate_content([
            "중고등학생에게 부정적인 사고를 긍정적 사고로 바꿔주는 역할을 합니다. 예를 들어 출력물은 오늘은 비가와서 추워. 그런데 빗 소리를 들어서 완전 럭키비키 잖아!. 여기에서 럭키비키는 꼭 들어가야되.입력의 내용을 참고하여 재치있는 원영적 사고를 생성해주세요.",
            f"input: {user_input}",
        ])

        # 결과 출력
        st.subheader("생성된 상장")
        st.write(response.text)
else:
    st.warning("API 키를 사이드바에 입력하세요.")