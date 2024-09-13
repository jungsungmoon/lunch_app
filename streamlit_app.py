import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="점심 메뉴 선정", layout="centered")

# 세션 상태 초기화
if 'name' not in st.session_state:
    st.session_state.name = None
if 'menu_options' not in st.session_state:
    st.session_state.menu_options = []
if 'selected_menu' not in st.session_state:
    st.session_state.selected_menu = None

# 1. 이름 입력 페이지
def input_name():
    st.title("이름을 입력하세요")
    name = st.text_input("이름", key="name_input")
    
    if st.button("다음"):
        if name:
            st.session_state.name = name
            st.experimental_rerun()

# 2. 점심 메뉴 입력 페이지
def input_lunch_menu():
    st.title(f"{st.session_state.name}님, 점심 메뉴를 입력하세요!")
    
    menu = st.text_input("점심 메뉴 입력")
    
    if st.button("추가"):
        if menu:
            st.session_state.menu_options.append(menu)
    
    st.subheader("다른 사람들이 입력한 메뉴")
    if st.session_state.menu_options:
        st.write(st.session_state.menu_options)
    
    if st.button("메뉴 선택하기"):
        st.experimental_rerun()

# 3. 메뉴 선택 페이지
def select_lunch_menu():
    st.title(f"{st.session_state.name}님, 오늘의 점심 메뉴를 선택하세요!")
    
    selected_menu = st.radio("점심 메뉴", st.session_state.menu_options)
    
    if st.button("선택 완료"):
        st.session_state.selected_menu = selected_menu
        st.experimental_rerun()

# 페이지 구성 로직
if st.session_state.name is None:
    input_name()
elif not st.session_state.selected_menu:
    input_lunch_menu() if not st.session_state.menu_options else select_lunch_menu()
else:
    st.title(f"{st.session_state.name}님, 오늘의 점심 메뉴는 {st.session_state.selected_menu}입니다!")
