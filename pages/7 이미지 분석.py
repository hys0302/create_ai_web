import streamlit as st
import openai
from PIL import Image, ImageOps
import numpy as np
import time

# 사이드바에서 API 키 입력 받기
try:
    st.sidebar.title("API 설정")
    api_key = st.sidebar.text_input("OpenAI API 키를 입력하세요", type="password")

    # API 키가 입력되었는지 확인
    if api_key:
        # OpenAI 클라이언트 초기화
        openai.api_key = api_key

        # Streamlit 페이지 제목 설정
        st.title("염색체 그림 변환기")

        # 사용자로부터 이미지 업로드 받기
        uploaded_file = st.file_uploader("이미지를 업로드하세요", type=["jpg", "jpeg", "png"])

        # 버튼을 클릭했을 때 염색체 그림으로 변환
        if st.button("염색체 그림으로 변환") and uploaded_file is not None:
            try:
                # 업로드된 이미지 열기
                image = Image.open(uploaded_file)
                image_gray = ImageOps.grayscale(image)

                # 엣지 검출을 사용하여 염색체 형태 강조 (간단한 엣지 검출 적용)
                image_np = np.array(image_gray)
                edges = np.where(image_np > 128, 255, 0).astype(np.uint8)

                # 결과 이미지를 PIL 이미지로 변환
                chromosome_image = Image.fromarray(edges)

                # 이미지 출력
                st.image(chromosome_image, caption="염색체 그림으로 변환된 이미지")
            except Exception as e:
                if "408" in str(e):
                    st.error("요청 시간이 초과되었습니다. 다시 시도해 주세요.")
                    time.sleep(1)  # 잠시 대기 후 재시도 권장
                else:
                    st.error(f"오류가 발생했습니다: {e}")
        elif uploaded_file is None:
            st.warning("이미지를 업로드하세요.")
    else:
        st.warning("API 키를 사이드바에 입력하세요.")
except Exception as e:
    st.error(f"스크립트 실행 중 오류가 발생했습니다: {e}")