import streamlit as st

# 1. 웹 페이지 제목 및 설명 설정
st.set_page_config(page_title="냉방 전기세 계산기", page_icon="❄️")
st.title("❄️ 냉방 전기세 계산기")
st.write("선풍기와 에어컨의 하루 사용 시간을 입력하여 한 달 예상 전기세를 계산해 보세요.")

# 2. 기본 데이터 정의 (기존 코드의 변수 활용)
appliances = ['선풍기', '에어컨']
wattages = [60, 1800]
avg_bill = 50000       # 평균 전기세 (50,000원)
electric_rate = 200    # 기존 코드의 'k20'을 1kWh당 200원으로 가정 (보정)

st.divider()

# 3. 입력 UI 구성 (st.number_input 활용)
st.subheader("🔌 가전제품별 하루 사용 시간 입력")

# 두 대의 가전제품 입력을 깔끔하게 배치하기 위해 레이아웃 분할
col1, col2 = st.columns(2)

with col1:
    st.image("https://img.icons8.com/fluency/96/fan.png", width=50) # 시각적 효과를 위한 아이콘
    hours_fan = st.number_input(
        f"{appliances[0]} ({wattages[0]}W)", 
        min_value=0.0, max_value=24.0, value=0.0, step=0.5, key="fan"
    )

with col2:
    st.image("https://img.icons8.com/fluency/96/air-conditioner.png", width=50)
    hours_ac = st.number_input(
        f"{appliances[1]} ({wattages[1]}W)", 
        min_value=0.0, max_value=24.0, value=0.0, step=0.5, key="ac"
    )

st.divider()

# 4. 계산 및 결과 출력 버튼
if st.button("⚡ 전기세 계산하기", type="primary"):
    
    # 소비전력량 계산 (W * 시간 * 30일 / 1000 = kWh)
    k_fan = (hours_fan * wattages[0] * 30) / 1000
    k_ac = (hours_ac * wattages[1] * 30) / 1000
    total_k = k_fan + k_ac
    
    # 예상 요금 계산
    my_bill = int(total_k * electric_rate)
    
    # 결과 화면 출력
    st.subheader("📊 계산 결과")
    
    # 요약 정보 제공
    st.metric(label="나의 예상 냉방 전기세", value=f"{my_bill:,} 원")
    st.caption(f"💡 총 전력 사용량: {total_k:.2f} kWh (30일 기준, 1kWh당 {electric_rate}원 계산)")
    
    # 평균 전기세와 비교 (st.success, st.warning 활용)
    if my_bill < avg_bill:
        st.success(f"🎉 평균 냉방 전기세({avg_bill:,}원)보다 **낮습니다!** 에너지를 잘 절약하고 계시네요!")
    else:
        st.warning(f"⚠️ 평균 냉방 전기세({avg_bill:,}원)보다 **높습니다!** 사용 시간을 조금 줄여보는 건 어떨까요?")