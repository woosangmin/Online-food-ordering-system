import streamlit as st
import text_introduction as ti
import os

st.set_page_config(page_title='Order Food Now !', page_icon=None, layout="centered", initial_sidebar_state="collapsed", menu_items=None)
headerSection = st.container()
mainSection = st.container()
checkoutSection = st.container()

directory = os.path.abspath(os.path.dirname(__file__))

def show_restaurant_page() :
    with mainSection :
        st.header(f"안녕하세요, {st.session_state['room_number']}호 고객님? :sunglasses:")
        the_lge, seven_sq, tao, oys = st.tabs(['더 라운지 / The Lounge', '세븐 스퀘어 / Seven Square', '도원 / TAOYUAN', '오이스터배 / Oyster배'])
        with the_lge :
            st.subheader('더 라운지 / The Lounge')
            st.image(f"{directory}/data/The_Lounge/the_lounge.jpg")
            st.text(ti.intro_the_lounge)
            col1, col2, col3, col4 = st.columns(4)
            with col1 :
                st.page_link("pages/sub_ui_lounge_br_week.py", label="브런치 주중 주문")
            with col2 :
                st.page_link("pages/sub_ui_lounge_br_holi.py", label="브런치 주말/휴일 주문")
            with col3 :
                st.page_link("pages/sub_ui_lounge_dn_week.py", label="다인 주중 주문")
            with col4 :
                st.page_link("pages/sub_ui_lounge_dn_holi.py", label="다인 주말/휴일 주문")
        with seven_sq :
            st.subheader('세븐 스퀘어 / Seven Square')
            st.image(f"{directory}/data/Seven Square/seven_square.jpg")
            st.text(ti.intro_seven_square)
            st.button ("주문하기 / Order now", on_click="None", args= ("seven_square"), key = 2)
        with tao :
            st.subheader('도원 / TAOYUAN')
            st.image(f"{directory}/data/Taoyuan/TAOYUAN.jpg")
            st.text(ti.intro_taoyuan)
            st.button ("주문하기 / Order now", on_click="None", args= ("taoyuan"), key = 3)
        with oys :
            st.subheader('오이스터배 / Oyster배')
            st.image(f"{directory}/data/OysterBae/oysterbae.jpg")
            st.text(ti.intro_oyster)
            st.button ("주문하기 / Order now", on_click="None", args= ("oyster_bae"), key = 4)

with headerSection:
    if 'room_number' not in st.session_state :
        st.session_state['room_number'] = "305"
    if 'customer_name' not in st.session_state :
        st.session_state['customer_name'] = "Charlie"
    st.title("Online Food Ordering System 😋")
    show_restaurant_page()
    
