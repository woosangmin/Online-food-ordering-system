import streamlit as st
import pandas as pd
import control_db as cond
import manage as ma
import text_introduction as ti
import datetime

st.set_page_config(page_title='Order Food Now !', page_icon=None, layout="centered", initial_sidebar_state="collapsed", menu_items=None)
headerSection = st.container()
mainSection = st.container()
checkoutSection = st.container()

# DB 연결
db = cond.connect_db("the_lounge")

# 주문한 메뉴 이름 / 수량 / 가격 리스트
food_list, qty_list, amt_list = [], [], []

# 카트에 메뉴 추가하기
def add_to_cart(menu, qty, amt) :
    food_list.append(menu)
    qty_list.append(qty)
    amt_list.append(amt)

# 주문 버튼
def order_pressed(title, food_list, qty_list, amt_list) :
    customer_name = st.session_state["customer_name"]
    room_number = st.session_state["room_number"]
    order_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if cond.place_order("the_order_lounge", title, food_list, qty_list, amt_list, customer_name, room_number, order_time) :
        st.warning("The order is completed! Please move to Order Status")
        for i in range(100, 314) :
            for key in st.session_state.keys() :
                if str(i) == key :
                    st.session_state[key] = False
    else :
        st.warning("There is something wrong!")

# 취소 버튼
def cancel_pressed(option, change) :
    if cond.get_status("the_order_lounge", change, option) :
        if cond.change_status("the_order_lounge", change, option) :
            st.warning("The status of the order is successfully changed.'")
        else :
            st.warning("There is something wrong!")
    else :
        st.warning("The status of the order is not 'Canceled!'")

# 다시 주문 버튼
def reorder_pressed(option, change) :
    if cond.get_status("the_order_lounge", change, option) :
        if cond.change_status("the_order_lounge", change, option) :
            st.warning("The status of the order is successfully changed.'")
        else :
            st.warning("There is something wrong!")
    else :
        st.warning("The status of the order is not 'Ordered!'")

def show_rounge_page() :
    st.header(f"안녕하세요, {st.session_state['room_number']}호 고객님? :sunglasses:")
    
    br_week, cart, receipt, return_b = st.tabs(['Brunch(Weekday)', 'cart', 'Order Status', '첫 페이지로 돌아가기'])

    with br_week:
        # def get_menu(db, column_list, target, target_value) 
        #브런치(주중) 하위 메뉴에 대한 정보 불러오기
        detail = cond.get_menu(db, ['time'], 'menu', 'title_kr', '브런치(주중)', True) 
        # 주문 가능한 시간을 출력 / detail[0]는 tuple
        start, end, due = ma.return_time(detail[0][0]) 
        sentence = ma.time_sentence(start, end, due)
        st.text(sentence)
        # '브런치(주중)' 하위 메뉴에 대한 탭 생성
        combo, promotion, meal, dessert, beverage, alcohol = st.tabs(['세트', '프로모션', '단품', '디저트', '음료', '주류'])
        with combo :
            # 세트 메뉴에 대한 정보 불러오기
            de_com = cond.get_menu(db, ['name_kr', 'time_weekday', 'table_name'], 'sub_brunch', 'type', 'combo', True)
            # 세트 메뉴의 하위 메뉴에 대한 탭 생성
            dn_2, dn_set, br_set, sw_set, cf_set = st.tabs([de_com[0][0], de_com[1][0], de_com[2][0], de_com[3][0], de_com[4][0]])
            with dn_2 : # 다이닝 2인 세트 메뉴(2 종류)
                st.text(ti.intro_dining_set)
                start, end, due = ma.return_time(de_com[0][1]) 
                sentence = ma.time_sentence(start, end, due)
                st.text(sentence)
                de_dn_2 = cond.get_menu(db, ['menu', 'price'], de_com[0][2], "*", "*", False)
                col1_dn_2, col2_dn_2 = st.columns(2) # 종류 별 컬럼 생성
                col1_dn_2.text(de_dn_2[0][0]) # 첫 번째 종류에 대해 수량 입력받기
                if col1_dn_2.checkbox(label = f'Order menu : {de_dn_2[0][1]} Won', key = 100):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col1_dn_2.text('Enter QTY. -')
                        c_col1_dn_2 = col1_dn_2.number_input(label="101", min_value=1, key = 101, label_visibility="collapsed")
                        add_to_cart(de_dn_2[0][0], int(c_col1_dn_2), int(c_col1_dn_2) * int(de_dn_2[0][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
                col2_dn_2.text(de_dn_2[1][0]) # 두 번째 종류에 대해 수량 입력받기
                if col2_dn_2.checkbox(label = f'Order menu : {de_dn_2[1][1]} Won', key = 102):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col2_dn_2.text('Enter QTY. -')
                        c_col2_dn_2 = col2_dn_2.number_input(label="103", min_value=1, key = 103, label_visibility="collapsed")
                        add_to_cart(de_dn_2[1][0], int(c_col2_dn_2), int(c_col2_dn_2) * int(de_dn_2[1][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
            with dn_set : # 다이닝 세트 메뉴
                st.text(ti.intro_dining_set)
                start, end, due = ma.return_time(de_com[1][1]) 
                sentence = ma.time_sentence(start, end, due)
                st.text(sentence)
                de_dn_set = cond.get_menu(db, ['menu', 'price'], de_com[1][2], "*", "*", False)
                col1_dn_set, col2_dn_set = st.columns(2) # 종류 별 컬럼 생성
                col1_dn_set.text(de_dn_set[0][0]) # 첫 번째 종류에 대해 수량 입력받기
                if col1_dn_set.checkbox(label = f'Order menu : {de_dn_set[0][1]} Won', key = 104):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col1_dn_set.text('Enter QTY. -')
                        c_col1_dn_set = col1_dn_set.number_input(label="105", min_value=1, key = 105, label_visibility="collapsed")
                        add_to_cart(de_dn_set[0][0], int(c_col1_dn_set), int(c_col1_dn_set) * int(de_dn_set[0][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
                col2_dn_set.text(de_dn_set[1][0]) # 두 번째 종류에 대해 수량 입력받기
                if col2_dn_set.checkbox(label = f'Order menu : {de_dn_set[1][1]} Won', key = 106):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col2_dn_set.text('Enter QTY. -')
                        c_col2_dn_set = col2_dn_set.number_input(label="107", min_value=1, key = 107, label_visibility="collapsed")
                        add_to_cart(de_dn_set[1][0], int(c_col2_dn_set), int(c_col2_dn_set) * int(de_dn_set[1][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
            with br_set :
                start, end, due = ma.return_time(de_com[2][1]) 
                sentence = ma.time_sentence(start, end, due)
                st.text(sentence)
                de_br_set = cond.get_menu(db, ['menu', 'price'], de_com[2][2], "*", "*", False)
                col1_br_set, col2_br_set = st.columns(2) # 종류 별 컬럼 생성
                col1_br_set.text(de_br_set[0][0]) # 첫 번째 종류에 대해 수량 입력받기
                if col1_br_set.checkbox(label = f'Order menu : {de_br_set[0][1]} Won', key = 108):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col1_br_set.text('Enter QTY. -')
                        c_col1_br_set = col1_br_set.number_input(label="109", min_value=1, key = 109, label_visibility="collapsed")
                        add_to_cart(de_br_set[0][0], int(c_col1_br_set), int(c_col1_br_set) * int(de_br_set[0][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
                col2_br_set.text(de_br_set[1][0]) # 두 번째 종류에 대해 수량 입력받기
                if col2_br_set.checkbox(label = f'Order menu : {de_br_set[1][1]} Won', key = 110):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col2_br_set.text('Enter QTY. -')
                        c_col2_br_set = col2_br_set.number_input(label="111", min_value=1, key = 111, label_visibility="collapsed")
                        add_to_cart(de_br_set[1][0], int(c_col2_br_set), int(c_col2_br_set) * int(de_br_set[1][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
            with sw_set :
                st.text(ti.intro_sweet)
                start, end, due = ma.return_time(de_com[3][1]) 
                sentence = ma.time_sentence(start, end, due)
                st.text(sentence)
                de_sw_set = cond.get_menu(db, ['menu', 'price', 'sub_menu'], de_com[3][2], "*", "*", False)
                col1_sw_set, col2_sw_set = st.columns(2) # 종류 별 컬럼 생성
                col1_sw_set.text(de_sw_set[0][0]) # 첫 번째 종류에 대해 수량 입력받기
                col1_sw_set.text(de_sw_set[0][2])
                if col1_sw_set.checkbox(label = f'Order menu : {de_sw_set[0][1]} Won', key = 112):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col1_sw_set.text('Enter QTY. -')
                        c_col1_sw_set = col1_sw_set.number_input(label="113", min_value=1, key = 113, label_visibility="collapsed")
                        add_to_cart(de_sw_set[0][0], int(c_col1_sw_set), int(c_col1_sw_set) * int(de_sw_set[0][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
                col2_sw_set.text(de_sw_set[1][0]) # 두 번째 종류에 대해 수량 입력받기
                col2_sw_set.text(de_sw_set[1][2])
                if col2_sw_set.checkbox(label = f'Order menu : {de_sw_set[1][1]} Won', key = 114):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col2_sw_set.text('Enter QTY. -')
                        c_col2_sw_set = col2_sw_set.number_input(label="115", min_value=1, key = 115, label_visibility="collapsed")
                        add_to_cart(de_sw_set[1][0], int(c_col2_sw_set), int(c_col2_sw_set) * int(de_sw_set[1][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
            with cf_set :
                start, end, due = ma.return_time(de_com[4][1]) 
                sentence = ma.time_sentence(start, end, due)
                st.text(sentence)
                de_cf_set = cond.get_menu(db, ['menu', 'price'], de_com[4][2], "*", "*", False)
                col1_cf_set, col2_cf_set = st.columns(2) # 종류 별 컬럼 생성
                col1_cf_set.text(de_cf_set[0][0]) # 첫 번째 종류에 대해 수량 입력받기
                if col1_cf_set.checkbox(label = f'Order menu : {de_cf_set[0][1]} Won', key = 116):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col1_cf_set.text('Enter QTY. -')
                        c_col1_cf_set = col1_cf_set.number_input(label="117", min_value=1, key = 117, label_visibility="collapsed")
                        add_to_cart(de_cf_set[0][0], int(c_col1_cf_set), int(c_col1_cf_set) * int(de_cf_set[0][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
                col2_cf_set.text(de_cf_set[1][0]) # 두 번째 종류에 대해 수량 입력받기
                if col2_cf_set.checkbox(label = f'Order menu : {de_cf_set[1][1]} Won', key = 118):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col2_cf_set.text('Enter QTY. -')
                        c_col2_cf_set = col2_cf_set.number_input(label="119", min_value=1, key = 119, label_visibility="collapsed")
                        add_to_cart(de_cf_set[1][0], int(c_col2_cf_set), int(c_col2_cf_set) * int(de_cf_set[1][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")        
        with promotion :
            # 정보 불러오기
            de_pro = cond.get_menu(db, ['name_kr', 'time_weekday', 'table_name'], 'sub_brunch', 'type', 'promotion', True)
            # 메뉴의 하위 메뉴에 대한 탭 생성
            start, end, due = ma.return_time(de_pro[0][1]) 
            sentence = ma.time_sentence(start, end, due)
            st.text(sentence)
            st.text(de_pro[0][0])
            de_bingsu = cond.get_menu(db, ['menu', 'price'], de_pro[0][2], "*", "*", False)
            col1_bingsu, col2_bingsu = st.columns(2) # 종류 별 컬럼 생성
            col1_bingsu.text(de_bingsu[0][0]) # 첫 번째 종류에 대해 수량 입력받기
            col1_bingsu.text(ti.intro_summer_udo)
            if col1_bingsu.checkbox(label = f'Order menu : {de_bingsu[0][1]} Won', key = 120):
                if ma.weekday_true() and ma.open_true(start, due) :
                    col1_bingsu.text('Enter QTY. -')
                    c_col1_bingsu = col1_bingsu.number_input(label="121", min_value=1, key = 121, label_visibility="collapsed")
                    add_to_cart(de_bingsu[0][0], int(c_col1_bingsu), int(c_col1_bingsu) * int(de_bingsu[0][1]))
                else : st.popover(label="주문 가능한 시간이 아닙니다.")
            col2_bingsu.text(de_bingsu[1][0]) # 두 번째 종류에 대해 수량 입력받기
            col2_bingsu.text(ti.intro_summer_mango)
            if col2_bingsu.checkbox(label = f'Order menu : {de_bingsu[1][1]} Won', key = 122):
                if ma.weekday_true() and ma.open_true(start, due) :
                    col2_bingsu.text('Enter QTY. -')
                    c_col2_bingsu = col2_bingsu.number_input(label="123", min_value=1, key = 123, label_visibility="collapsed")
                    add_to_cart(de_bingsu[1][0], int(c_col2_bingsu), int(c_col2_bingsu) * int(de_bingsu[1][1]))
                else : st.popover(label="주문 가능한 시간이 아닙니다.")
        with meal :
            # 세트 메뉴에 대한 정보 불러오기
            de_meal = cond.get_menu(db, ['name_kr', 'time_weekday', 'table_name'], 'sub_brunch', 'type', 'meal', True)
            start, end, due = ma.return_time(de_meal[0][1]) 
            sentence = ma.time_sentence(start, end, due)
            st.text(sentence)
            st.text(de_meal[0][0])
            de_dine = cond.get_menu(db, ['menu', 'price'], de_meal[0][2], "*", "*", False)
            col1_dine, col2_dine, col3_dine = st.columns(3) # 종류 별 컬럼 생성
            col1_dine.text(de_dine[0][0]) # 첫 번째 종류에 대해 수량 입력받기
            col1_dine.text(ti.intro_dine_btbs)
            if col1_dine.checkbox(label = f'Order menu : {de_dine[0][1]} Won', key = 124):
                if ma.weekday_true() and ma.open_true(start, due) :
                    col1_dine.text('Enter QTY. -')
                    c_col1_dine = col1_dine.number_input(label="125", min_value=1, key = 125, label_visibility="collapsed")
                    add_to_cart(de_dine[0][0], int(c_col1_dine), int(c_col1_dine) * int(de_dine[0][1]))
                else : st.popover(label="주문 가능한 시간이 아닙니다.")
            col2_dine.text(de_dine[1][0]) 
            col2_dine.text(ti.intro_dine_atp)
            if col2_dine.checkbox(label = f'Order menu : {de_dine[1][1]} Won', key = 126):
                if ma.weekday_true() and ma.open_true(start, due) :
                    col2_dine.text('Enter QTY. -')
                    c_col2_dine = col2_dine.number_input(label="127", min_value=1, key = 127, label_visibility="collapsed")
                    add_to_cart(de_dine[1][0], int(c_col2_dine), int(c_col2_dine) * int(de_dine[1][1]))
                else : st.popover(label="주문 가능한 시간이 아닙니다.")
            col3_dine.text(de_dine[2][0]) 
            col3_dine.text(ti.intro_dine_gp)
            if col3_dine.checkbox(label = f'Order menu : {de_dine[2][1]} Won', key = 128):
                if ma.weekday_true() and ma.open_true(start, due) :
                    col3_dine.text('Enter QTY. -')
                    c_col3_dine = col3_dine.number_input(label="129", min_value=1, key = 129, label_visibility="collapsed")
                    add_to_cart(de_dine[2][0], int(c_col3_dine), int(c_col3_dine) * int(de_dine[2][1]))
                else : st.popover(label="주문 가능한 시간이 아닙니다.")
            col4_dine, col5_dine, col6_dine = st.columns(3)
            col4_dine.text(de_dine[3][0]) 
            col4_dine.text(ti.intro_dine_jbs) 
            if col4_dine.checkbox(label = f'Order menu : {de_dine[3][1]} Won', key = 130):
                if ma.weekday_true() and ma.open_true(start, due) :
                    col4_dine.text('Enter QTY. -')
                    c_col4_dine = col4_dine.number_input(label="131", min_value=1, key = 131, label_visibility="collapsed")
                    add_to_cart(de_dine[3][0], int(c_col4_dine), int(c_col4_dine) * int(de_dine[3][1]))
                else : st.popover(label="주문 가능한 시간이 아닙니다.")
            col5_dine.text(de_dine[4][0]) 
            col5_dine.text(ti.intro_dine_cs) 
            if col5_dine.checkbox(label = f'Order menu : {de_dine[4][1]} Won', key = 132):
                if ma.weekday_true() and ma.open_true(start, due) :
                    col5_dine.text('Enter QTY. -')
                    c_col5_dine = col5_dine.number_input(label="", min_value=1, key = 133)
                    add_to_cart(de_dine[4][0], int(c_col5_dine), int(c_col5_dine) * int(de_dine[4][1]))
                else : st.popover(label="주문 가능한 시간이 아닙니다.")
            col6_dine.text(de_dine[5][0]) 
            col6_dine.text(ti.intro_dine_spts) 
            if col6_dine.checkbox(label = f'Order menu : {de_dine[5][1]} Won', key = 134):
                if ma.weekday_true() and ma.open_true(start, due) :
                    col6_dine.text('Enter QTY. -')
                    c_col6_dine = col6_dine.number_input(label="135", min_value=1, key = 135, label_visibility="collapsed")
                    add_to_cart(de_dine[5][0], int(c_col6_dine), int(c_col6_dine) * int(de_dine[5][1]))
                else : st.popover(label="주문 가능한 시간이 아닙니다.")
            col7_dine, col8_dine, col9_dine = st.columns(3)
            col7_dine.text(de_dine[6][0])
            col7_dine.text(ti.intro_dine_tcr)
            if col7_dine.checkbox(label = f'Order menu : {de_dine[6][1]} Won', key = 136):
                if ma.weekday_true() and ma.open_true(start, due) :
                    col7_dine.text('Enter QTY. -')
                    c_col7_dine = col7_dine.number_input(label="137", min_value=1, key = 137, label_visibility="collapsed")
                    add_to_cart(de_dine[6][0], int(c_col7_dine), int(c_col7_dine) * int(de_dine[6][1]))
                else : st.popover(label="주문 가능한 시간이 아닙니다.")
            col8_dine.text(de_dine[7][0])
            col8_dine.text(ti.intro_dine_eb)
            if col8_dine.checkbox(label = f'Order menu : {de_dine[7][1]} Won', key = 138):
                if ma.weekday_true() and ma.open_true(start, due) :
                    col8_dine.text('Enter QTY. -')
                    c_col8_dine = col8_dine.number_input(label="139", min_value=1, key = 139, label_visibility="collapsed")
                    add_to_cart(de_dine[7][0], int(c_col8_dine), int(c_col8_dine) * int(de_dine[7][1]))
                else : st.popover(label="주문 가능한 시간이 아닙니다.")
            col9_dine.text(de_dine[8][0])
            col9_dine.text(ti.intro_dine_ft)
            if col9_dine.checkbox(label = f'Order menu : {de_dine[8][1]} Won', key = 140):
                if ma.weekday_true() and ma.open_true(start, due) :
                    col9_dine.text('Enter QTY. -')
                    c_col9_dine = col9_dine.number_input(label="141", min_value=1, key = 141, label_visibility="collapsed")
                    add_to_cart(de_dine[8][0], int(c_col9_dine), int(c_col9_dine) * int(de_dine[8][1]))
                else : st.popover(label="주문 가능한 시간이 아닙니다.")
            col10_dine, col11_dine = st.columns(2)
            col10_dine.text(de_dine[9][0])
            col10_dine.text(ti.intro_dine_bs)
            if col10_dine.checkbox(label = f'Order menu : {de_dine[9][1]} Won', key = 142):
                if ma.weekday_true() and ma.open_true(start, due) :
                    col10_dine.text('Enter QTY. -')
                    c_col10_dine = col10_dine.number_input(label="143", min_value=1, key = 143, label_visibility="collapsed")
                    add_to_cart(de_dine[9][0], int(c_col10_dine), int(c_col10_dine) * int(de_dine[9][1]))
                else : st.popover(label="주문 가능한 시간이 아닙니다.")
            col11_dine.text(de_dine[10][0])
            if col11_dine.checkbox(label = f'Order menu : {de_dine[10][1]} Won', key = 144):
                if ma.weekday_true() and ma.open_true(start, due) :
                    col11_dine.text('Enter QTY. -')
                    c_col11_dine = col11_dine.number_input(label="145", min_value=1, key = 145, label_visibility="collapsed")
                    add_to_cart(de_dine[10][0], int(c_col11_dine), int(c_col11_dine) * int(de_dine[10][1]))
                else : st.popover(label="주문 가능한 시간이 아닙니다.")           
        with dessert :
            # 메뉴에 대한 정보 불러오기
            de_dess = cond.get_menu(db, ['name_kr', 'time_weekday', 'table_name'], 'sub_brunch', 'type', 'dessert', True)
            start, end, due = ma.return_time(de_dess[0][1]) 
            sentence = ma.time_sentence(start, end, due)
            st.text(sentence)
            st.text(ti.intro_dessert_ice)
            de_more = cond.get_menu(db, ['menu', 'price'], de_dess[0][2], "*", "*", False)
            col1_dess, col2_dess, col3_dess = st.columns(3) # 종류 별 컬럼 생성
            col1_dess.text(de_more[0][0]) # 첫 번째 종류에 대해 수량 입력받기
            if col1_dess.checkbox(label = f'Order menu : {de_more[0][1]} Won', key = 146):
                if ma.weekday_true() and ma.open_true(start, due) :
                    col1_dess.text('Enter QTY. -')
                    c_col1_dess = col1_dess.number_input(label="147", min_value=1, key = 147, label_visibility="collapsed")
                    add_to_cart(de_more[0][0], int(c_col1_dess), int(c_col1_dess) * int(de_more[0][1]))
                else : st.popover(label="주문 가능한 시간이 아닙니다.")
            col2_dess.text(de_more[1][0]) 
            if col2_dess.checkbox(label = f'Order menu : {de_more[1][1]} Won', key = 148):
                if ma.weekday_true() and ma.open_true(start, due) :
                    col2_dess.text('Enter QTY. -')
                    c_col2_dess = col2_dess.number_input(label="149", min_value=1, key = 149, label_visibility="collapsed")
                    add_to_cart(de_more[1][0], int(c_col2_dess), int(c_col2_dess) * int(de_more[1][1]))
                else : st.popover(label="주문 가능한 시간이 아닙니다.")
            col3_dess.text(de_more[2][0]) 
            if col3_dess.checkbox(label = f'Order menu : {de_more[2][1]} Won', key = 150):
                if ma.weekday_true() and ma.open_true(start, due) :
                    col3_dess.text('Enter QTY. -')
                    c_col3_dess = col3_dess.number_input(label="151", min_value=1, key = 151, label_visibility="collapsed")
                    add_to_cart(de_more[2][0], int(c_col3_dess), int(c_col3_dess) * int(de_more[2][1]))
                else : st.popover(label="주문 가능한 시간이 아닙니다.")
            col4_dess, col5_dess, col6_dess = st.columns(3) # 종류 별 컬럼 생성
            col4_dess.text(de_more[3][0]) 
            if col4_dess.checkbox(label = f'Order menu : {de_more[3][1]} Won', key = 152):
                if ma.weekday_true() and ma.open_true(start, due) :
                    col4_dess.text('Enter QTY. -')
                    c_col4_dess = col4_dess.number_input(label="153", min_value=1, key = 153, label_visibility="collapsed")
                    add_to_cart(de_more[3][0], int(c_col4_dess), int(c_col4_dess) * int(de_more[3][1]))
                else : st.popover(label="주문 가능한 시간이 아닙니다.")
            col5_dess.text(de_more[4][0]) 
            if col5_dess.checkbox(label = f'Order menu : {de_more[4][1]} Won', key = 154):
                if ma.weekday_true() and ma.open_true(start, due) :
                    col5_dess.text('Enter QTY. -')
                    c_col5_dess = col5_dess.number_input(label="155", min_value=1, key = 155, label_visibility="collapsed")
                    add_to_cart(de_more[4][0], int(c_col5_dess), int(c_col5_dess) * int(de_more[4][1]))
                else : st.popover(label="주문 가능한 시간이 아닙니다.")
            col6_dess.text(de_more[5][0]) 
            if col6_dess.checkbox(label = f'Order menu : {de_more[5][1]} Won', key = 156):
                if ma.weekday_true() and ma.open_true(start, due) :
                    col6_dess.text('Enter QTY. -')
                    c_col6_dess = col6_dess.number_input(label="157", min_value=1, key = 157, label_visibility="collapsed")
                    add_to_cart(de_more[5][0], int(c_col6_dess), int(c_col6_dess) * int(de_more[5][1]))
                else : st.popover(label="주문 가능한 시간이 아닙니다.")
        with beverage :
            # 세트 메뉴에 대한 정보 불러오기
            de_be = cond.get_menu(db, ['name_kr', 'time_weekday', 'table_name'], 'sub_brunch', 'type', 'beverage', True)
            # 세트 메뉴의 하위 메뉴에 대한 탭 생성
            be_ron, be_wa, be_sd, be_tr, be_ju, be_co = st.tabs([de_be[0][0], de_be[1][0], de_be[2][0], de_be[3][0], de_be[4][0], de_be[5][0]])
            with be_ron :
                start, end, due = ma.return_time(de_be[0][1]) 
                sentence = ma.time_sentence(start, end, due)
                st.text(sentence)
                de_ron = cond.get_menu(db, ['menu', 'price'], de_be[0][2], "*", "*", False)
                col1_ron, col2_ron, col3_ron = st.columns(3) # 종류 별 컬럼 생성
                col1_ron.text(de_ron[0][0]) # 첫 번째 종류에 대해 수량 입력받기
                if col1_ron.checkbox(label = f'Order menu : {de_ron[0][1]} Won', key = 158):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col1_ron.text('Enter QTY. -')
                        c_col1_ron = col1_ron.number_input(label="159", min_value=1, key = 159, label_visibility="collapsed")
                        add_to_cart(de_ron[0][0], int(c_col1_ron), int(c_col1_ron) * int(de_ron[0][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
                col2_ron.text(de_ron[1][0]) 
                if col2_ron.checkbox(label = f'Order menu : {de_ron[1][1]} Won', key = 160):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col2_ron.text('Enter QTY. -')
                        c_col2_ron = col2_ron.number_input(label="161", min_value=1, key = 161, label_visibility="collapsed")
                        add_to_cart(de_ron[1][0], int(c_col2_ron), int(c_col2_ron) * int(de_ron[1][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
                col3_ron.text(de_ron[2][0]) 
                if col3_ron.checkbox(label = f'Order menu : {de_ron[2][1]} Won', key = 162):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col3_ron.text('Enter QTY. -')
                        c_col3_ron = col3_ron.number_input(label="163", min_value=1, key = 163, label_visibility="collapsed")
                        add_to_cart(de_ron[2][0], int(c_col3_ron), int(c_col3_ron) * int(de_ron[2][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
                col4_ron, col5_ron, col6_ron = st.columns(3) # 종류 별 컬럼 생성
                col4_ron.text(de_ron[3][0]) 
                if col4_ron.checkbox(label = f'Order menu : {de_ron[3][1]} Won', key = 164):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col4_ron.text('Enter QTY. -')
                        c_col4_ron = col4_ron.number_input(label="165", min_value=1, key = 165, label_visibility="collapsed")
                        add_to_cart(de_ron[3][0], int(c_col4_ron), int(c_col4_ron) * int(de_ron[3][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
                col5_ron.text(de_ron[4][0]) 
                if col5_ron.checkbox(label = f'Order menu : {de_ron[4][1]} Won', key = 166):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col5_ron.text('Enter QTY. -')
                        c_col5_ron = col5_ron.number_input(label="167", min_value=1, key = 167, label_visibility="collapsed")
                        add_to_cart(de_ron[4][0], int(c_col5_ron), int(c_col5_ron) * int(de_ron[4][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
                col6_ron.text(de_ron[5][0]) 
                if col6_ron.checkbox(label = f'Order menu : {de_ron[5][1]} Won', key = 168):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col6_ron.text('Enter QTY. -')
                        c_col6_ron = col6_ron.number_input(label="169", min_value=1, key = 169, label_visibility="collapsed")
                        add_to_cart(de_ron[5][0], int(c_col6_ron), int(c_col6_ron) * int(de_ron[5][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
                col7_ron, con8_ron = st.columns(2) # 종류 별 컬럼 생성
                col7_ron.text(de_ron[6][0]) 
                if col7_ron.checkbox(label = f'Order menu : {de_ron[6][1]} Won', key = 170):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col7_ron.text('Enter QTY. -')
                        c_col7_ron = col7_ron.number_input(label="171", min_value=1, key = 171, label_visibility="collapsed")
                        add_to_cart(de_ron[6][0], int(c_col7_ron), int(c_col7_ron) * int(de_ron[6][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
            with be_wa :
                start, end, due = ma.return_time(de_be[1][1]) 
                sentence = ma.time_sentence(start, end, due)
                st.text(sentence)
                de_wa = cond.get_menu(db, ['menu', 'price'], de_be[1][2], "*", "*", False)
                col1_wa, col2_wa = st.columns(2) # 종류 별 컬럼 생성
                col1_wa.text(de_wa[0][0]) # 첫 번째 종류에 대해 수량 입력받기
                if col1_wa.checkbox(label = f'Order menu : {de_wa[0][1]} Won', key = 172):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col1_wa.text('Enter QTY. -')
                        c_col1_wa = col1_wa.number_input(label="173", min_value=1, key = 173, label_visibility="collapsed")
                        add_to_cart(de_wa[0][0], int(c_col1_wa), int(c_col1_wa) * int(de_wa[0][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
                col2_wa.text(de_wa[1][0]) 
                if col2_wa.checkbox(label = f'Order menu : {de_wa[1][1]} Won', key = 174):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col2_wa.text('Enter QTY. -')
                        c_col2_wa = col2_wa.number_input(label="175", min_value=1, key = 175, label_visibility="collapsed")
                        add_to_cart(de_wa[1][0], int(c_col2_wa), int(c_col2_wa) * int(de_wa[1][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
            with be_sd :
                start, end, due = ma.return_time(de_be[2][1]) 
                sentence = ma.time_sentence(start, end, due)
                st.text(sentence)
                de_sd = cond.get_menu(db, ['menu', 'price'], de_be[2][2], "*", "*", False)
                col1_sd, col2_sd = st.columns(2) # 종류 별 컬럼 생성
                col1_sd.text(de_sd[0][0]) # 첫 번째 종류에 대해 수량 입력받기
                if col1_sd.checkbox(label = f'Order menu : {de_sd[0][1]} Won', key = 176):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col1_sd.text('Enter QTY. -')
                        c_col1_sd = col1_sd.number_input(label="177", min_value=1, key = 177, label_visibility="collapsed")
                        add_to_cart(de_sd[0][0], int(c_col1_sd), int(c_col1_sd) * int(de_sd[0][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
                col2_sd.text(de_sd[1][0]) 
                if col2_sd.checkbox(label = f'Order menu : {de_sd[1][1]} Won', key = 178):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col2_sd.text('Enter QTY. -')
                        c_col2_sd = col2_sd.number_input(label="179", min_value=1, key = 179, label_visibility="collapsed")
                        add_to_cart(de_sd[1][0], int(c_col2_sd), int(c_col2_sd) * int(de_sd[1][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
                col3_sd, col4_sd = st.columns(2) # 종류 별 컬럼 생성
                col3_sd.text(de_sd[2][0]) 
                if col3_sd.checkbox(label = f'Order menu : {de_sd[2][1]} Won', key = 180):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col3_sd.text('Enter QTY. -')
                        c_col3_sd = col3_sd.number_input(label="181", min_value=1, key = 181, label_visibility="collapsed")
                        add_to_cart(de_sd[2][0], int(c_col3_sd), int(c_col3_sd) * int(de_sd[2][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
                col4_sd.text(de_sd[3][0]) 
                if col4_sd.checkbox(label = f'Order menu : {de_sd[3][1]} Won', key = 182):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col4_sd.text('Enter QTY. -')
                        c_col4_sd = col4_sd.number_input(label="183", min_value=1, key = 183, label_visibility="collapsed")
                        add_to_cart(de_sd[3][0], int(c_col4_sd), int(c_col4_sd) * int(de_sd[3][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
            with be_tr :
                start, end, due = ma.return_time(de_be[3][1]) 
                sentence = ma.time_sentence(start, end, due)
                st.text(sentence)
                de_tr = cond.get_menu(db, ['menu', 'price'], de_be[3][2], "*", "*", False)
                col1_tr, col2_tr, col3_tr = st.columns(3) # 종류 별 컬럼 생성
                col1_tr.text(de_tr[0][0]) # 첫 번째 종류에 대해 수량 입력받기
                if col1_tr.checkbox(label = f'Order menu : {de_tr[0][1]} Won', key = 184):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col1_tr.text('Enter QTY. -')
                        c_col1_tr = col1_tr.number_input(label="185", min_value=1, key = 185, label_visibility="collapsed")
                        add_to_cart(de_tr[0][0], int(c_col1_tr), int(c_col1_tr) * int(de_tr[0][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
                col2_tr.text(de_tr[1][0]) 
                if col2_tr.checkbox(label = f'Order menu : {de_tr[1][1]} Won', key = 186):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col2_tr.text('Enter QTY. -')
                        c_col2_tr = col2_tr.number_input(label="187", min_value=1, key = 187, label_visibility="collapsed")
                        add_to_cart(de_tr[1][0], int(c_col2_tr), int(c_col2_tr) * int(de_tr[1][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
                col3_tr.text(de_tr[2][0]) 
                if col3_tr.checkbox(label = f'Order menu : {de_tr[2][1]} Won', key = 188):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col3_tr.text('Enter QTY. -')
                        c_col3_tr = col3_tr.number_input(label="189", min_value=1, key = 189, label_visibility="collapsed")
                        add_to_cart(de_tr[2][0], int(c_col3_tr), int(c_col3_tr) * int(de_tr[2][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
            with be_ju :
                start, end, due = ma.return_time(de_be[4][1]) 
                sentence = ma.time_sentence(start, end, due)
                st.text(sentence)
                de_ju = cond.get_menu(db, ['menu', 'price'], de_be[4][2], "*", "*", False)
                col1_ju, col2_ju, col3_ju = st.columns(3) # 종류 별 컬럼 생성
                col1_ju.text(de_ju[0][0]) # 첫 번째 종류에 대해 수량 입력받기
                if col1_ju.checkbox(label = f'Order menu : {de_ju[0][1]} Won', key = 190):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col1_ju.text('Enter QTY. -')
                        c_col1_ju = col1_ju.number_input(label="191", min_value=1, key = 191, label_visibility="collapsed")
                        add_to_cart(de_ju[0][0], int(c_col1_ju), int(c_col1_ju) * int(de_ju[0][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
                col2_ju.text(de_ju[1][0]) 
                if col2_ju.checkbox(label = f'Order menu : {de_ju[1][1]} Won', key = 192):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col2_ju.text('Enter QTY. -')
                        c_col2_ju = col2_ju.number_input(label="193", min_value=1, key = 193, label_visibility="collapsed")
                        add_to_cart(de_ju[1][0], int(c_col2_ju), int(c_col2_ju) * int(de_ju[1][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
                col3_ju.text(de_ju[2][0]) 
                if col3_ju.checkbox(label = f'Order menu : {de_ju[2][1]} Won', key = 194):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col3_ju.text('Enter QTY. -')
                        c_col3_ju = col3_ju.number_input(label="195", min_value=1, key = 195, label_visibility="collapsed")
                        add_to_cart(de_ju[2][0], int(c_col3_ju), int(c_col3_ju) * int(de_ju[2][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
                col4_ju, col5_ju, col6_ju = st.columns(3) # 종류 별 컬럼 생성
                col4_ju.text(de_ju[3][0]) # 첫 번째 종류에 대해 수량 입력받기
                if col4_ju.checkbox(label = f'Order menu : {de_ju[3][1]} Won', key = 196):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col4_ju.text('Enter QTY. -')
                        c_col4_ju = col4_ju.number_input(label="197", min_value=1, key = 197, label_visibility="collapsed")
                        add_to_cart(de_ju[3][0], int(c_col4_ju), int(c_col4_ju) * int(de_ju[3][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
                col5_ju.text(de_ju[4][0]) 
                if col5_ju.checkbox(label = f'Order menu : {de_ju[4][1]} Won', key = 198):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col5_ju.text('Enter QTY. -')
                        c_col5_ju = col5_ju.number_input(label="199", min_value=1, key = 199, label_visibility="collapsed")
                        add_to_cart(de_ju[4][0], int(c_col5_ju), int(c_col5_ju) * int(de_ju[4][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
            with be_co :
                start, end, due = ma.return_time(de_be[5][1]) 
                sentence = ma.time_sentence(start, end, due)
                st.text(sentence)
                de_co = cond.get_menu(db, ['menu', 'price'], de_be[5][2], "*", "*", False)
                col1_co, col2_co, col3_co = st.columns(3) # 종류 별 컬럼 생성
                col1_co.text(de_co[0][0]) # 첫 번째 종류에 대해 수량 입력받기
                if col1_co.checkbox(label = f'Order menu : {de_co[0][1]} Won', key = 200):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col1_co.text('Enter QTY. -')
                        c_col1_co = col1_co.number_input(label="201", min_value=1, key = 201, label_visibility="collapsed")
                        add_to_cart(de_co[0][0], int(c_col1_co), int(c_col1_co) * int(de_co[0][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
                col2_co.text(de_co[1][0]) 
                if col2_co.checkbox(label = f'Order menu : {de_co[1][1]} Won', key = 202):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col2_co.text('Enter QTY. -')
                        c_col2_co = col2_co.number_input(label="203", min_value=1, key = 203, label_visibility="collapsed")
                        add_to_cart(de_co[1][0], int(c_col2_co), int(c_col2_co) * int(de_co[1][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
                col3_co.text(de_co[2][0]) 
                if col3_co.checkbox(label = f'Order menu : {de_co[2][1]} Won', key = 204):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col3_co.text('Enter QTY. -')
                        c_col3_co = col3_co.number_input(label="205", min_value=1, key = 205, label_visibility="collapsed")
                        add_to_cart(de_co[2][0], int(c_col3_co), int(c_col3_co) * int(de_co[2][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
                col4_co, col5_co, col6_co = st.columns(3) # 종류 별 컬럼 생성
                col4_co.text(de_co[3][0]) # 첫 번째 종류에 대해 수량 입력받기
                if col4_co.checkbox(label = f'Order menu : {de_co[3][1]} Won', key = 206):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col4_co.text('Enter QTY. -')
                        c_col4_co = col4_co.number_input(label="207", min_value=1, key = 207, label_visibility="collapsed")
                        add_to_cart(de_co[3][0], int(c_col4_co), int(c_col4_co) * int(de_co[3][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
                col5_co.text(de_co[4][0]) 
                if col5_co.checkbox(label = f'Order menu : {de_co[4][1]} Won', key = 208):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col5_co.text('Enter QTY. -')
                        c_col5_co = col5_co.number_input(label="209", min_value=1, key = 209, label_visibility="collapsed")
                        add_to_cart(de_co[4][0], int(c_col5_co), int(c_col5_co) * int(de_co[4][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
                col6_co.text(de_co[5][0]) 
                if col6_co.checkbox(label = f'Order menu : {de_co[5][1]} Won', key = 210):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col6_co.text('Enter QTY. -')
                        c_col6_co = col6_co.number_input(label="211", min_value=1, key = 211, label_visibility="collapsed")
                        add_to_cart(de_co[5][0], int(c_col6_co), int(c_col6_co) * int(de_co[5][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
                col7_co, col8_co, col9_co = st.columns(3) # 종류 별 컬럼 생성
                col7_co.text(de_co[6][0]) # 첫 번째 종류에 대해 수량 입력받기
                if col7_co.checkbox(label = f'Order menu : {de_co[6][1]} Won', key = 212):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col7_co.text('Enter QTY. -')
                        c_col7_co = col7_co.number_input(label="213", min_value=1, key = 213, label_visibility="collapsed")
                        add_to_cart(de_co[6][0], int(c_col7_co), int(c_col7_co) * int(de_co[6][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
                col8_co.text(de_co[7][0]) 
                if col8_co.checkbox(label = f'Order menu : {de_co[7][1]} Won', key = 214):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col8_co.text('Enter QTY. -')
                        c_col8_co = col8_co.number_input(label="215", min_value=1, key = 215, label_visibility="collapsed")
                        add_to_cart(de_co[7][0], int(c_col8_co), int(c_col8_co) * int(de_co[7][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
                col9_co.text(de_co[8][0]) 
                if col9_co.checkbox(label = f'Order menu : {de_co[8][1]} Won', key = 216):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col9_co.text('Enter QTY. -')
                        c_col9_co = col9_co.number_input(label="217", min_value=1, key = 217, label_visibility="collapsed")
                        add_to_cart(de_co[8][0], int(c_col9_co), int(c_col9_co) * int(de_co[8][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
                col10_co, col11_co, col12_co = st.columns(3) # 종류 별 컬럼 생성
                col10_co.text(de_co[9][0]) # 첫 번째 종류에 대해 수량 입력받기
                if col10_co.checkbox(label = f'Order menu : {de_co[9][1]} Won', key = 218):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col10_co.text('Enter QTY. -')
                        c_col10_co = col10_co.number_input(label="219", min_value=1, key = 219, label_visibility="collapsed")
                        add_to_cart(de_co[9][0], int(c_col10_co), int(c_col10_co) * int(de_co[9][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
                col11_co.text(de_co[10][0]) 
                if col11_co.checkbox(label = f'Order menu : {de_co[10][1]} Won', key = 220):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col11_co.text('Enter QTY. -')
                        c_col11_co = col11_co.number_input(label="221", min_value=1, key = 221, label_visibility="collapsed")
                        add_to_cart(de_co[10][0], int(c_col11_co), int(c_col11_co) * int(de_co[10][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
                col12_co.text(de_co[11][0]) 
                if col12_co.checkbox(label = f'Order menu : {de_co[11][1]} Won', key = 222):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col12_co.text('Enter QTY. -')
                        c_col12_co = col12_co.number_input(label="223", min_value=1, key = 223, label_visibility="collapsed")
                        add_to_cart(de_co[11][0], int(c_col12_co), int(c_col12_co) * int(de_co[11][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
                col13_co, col14_co, col15_co = st.columns(3) # 종류 별 컬럼 생성
                col13_co.text(de_co[12][0]) 
                if col13_co.checkbox(label = f'Order menu : {de_co[12][1]} Won', key = 224):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col13_co.text('Enter QTY. -')
                        c_col13_co = col13_co.number_input(label="225", min_value=1, key = 225, label_visibility="collapsed")
                        add_to_cart(de_co[12][0], int(c_col13_co), int(c_col13_co) * int(de_co[12][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
                col14_co.text(de_co[13][0]) 
                if col14_co.checkbox(label = f'Order menu : {de_co[13][1]} Won', key = 226):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col14_co.text('Enter QTY. -')
                        c_col14_co = col14_co.number_input(label="227", min_value=1, key = 227, label_visibility="collapsed")
                        add_to_cart(de_co[13][0], int(c_col14_co), int(c_col14_co) * int(de_co[13][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
                col15_co.text(de_co[14][0]) 
                if col15_co.checkbox(label = f'Order menu : {de_co[14][1]} Won', key = 228):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col15_co.text('Enter QTY. -')
                        c_col15_co = col15_co.number_input(label="229", min_value=1, key = 229, label_visibility="collapsed")
                        add_to_cart(de_co[14][0], int(c_col15_co), int(c_col15_co) * int(de_co[14][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
                col16_co, col17_co, col18_co = st.columns(3) # 종류 별 컬럼 생성
                col16_co.text(de_co[15][0]) 
                if col16_co.checkbox(label = f'Order menu : {de_co[15][1]} Won', key = 230):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col16_co.text('Enter QTY. -')
                        c_col16_co = col16_co.number_input(label="231", min_value=1, key = 231, label_visibility="collapsed")
                        add_to_cart(de_co[15][0], int(c_col16_co), int(c_col16_co) * int(de_co[15][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
                col17_co.text(de_co[16][0]) 
                if col17_co.checkbox(label = f'Order menu : {de_co[16][1]} Won', key = 232):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col17_co.text('Enter QTY. -')
                        c_col17_co = col17_co.number_input(label="233", min_value=1, key = 233, label_visibility="collapsed")
                        add_to_cart(de_co[16][0], int(c_col17_co), int(c_col17_co) * int(de_co[16][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
        with alcohol :
            # 세트 메뉴에 대한 정보 불러오기
            de_al = cond.get_menu(db, ['name_kr', 'time_weekday', 'table_name'], 'sub_brunch', 'type', 'alcohol', True)
            # 세트 메뉴의 하위 메뉴에 대한 탭 생성
            al_db, al_rc, al_ro, al_ld, al_ww, al_bb, al_ch, al_sp, al_rw = st.tabs([de_al[0][0], de_al[1][0], de_al[2][0], \
                                                                                     de_al[3][0], de_al[4][0], de_al[5][0], de_al[6][0], de_al[7][0], de_al[8][0]])
            with al_db :
                start, end, due = ma.return_time(de_al[0][1]) 
                sentence = ma.time_sentence(start, end, due)
                st.text(sentence)
                de_db = cond.get_menu(db, ['menu', 'price'], de_al[0][2], "*", "*", False)
                col1_db, col2_db = st.columns(2) # 종류 별 컬럼 생성
                col1_db.text(de_db[0][0]) # 첫 번째 종류에 대해 수량 입력받기
                if col1_db.checkbox(label = f'Order menu : {de_db[0][1]} Won', key = 234):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col1_db.text('Enter QTY. -')
                        c_col1_db = col1_db.number_input(label="235", min_value=1, key = 235, label_visibility="collapsed")
                        add_to_cart(de_db[0][0], int(c_col1_db), int(c_col1_db) * int(de_db[0][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
                col2_db.text(de_db[1][0]) 
                if col2_db.checkbox(label = f'Order menu : {de_db[1][1]} Won', key = 236):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col2_db.text('Enter QTY. -')
                        c_col2_db = col2_db.number_input(label="237", min_value=1, key = 237, label_visibility="collapsed")
                        add_to_cart(de_db[1][0], int(c_col2_db), int(c_col2_db) * int(de_db[1][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
            with al_rc :
                start, end, due = ma.return_time(de_al[1][1]) 
                sentence = ma.time_sentence(start, end, due)
                st.text(sentence)
                de_rc = cond.get_menu(db, ['menu', 'price'], de_al[1][2], "*", "*", False)
                col1_rc, col2_rc = st.columns(2) # 종류 별 컬럼 생성
                col1_rc.text(de_rc[0][0]) # 첫 번째 종류에 대해 수량 입력받기
                if col1_rc.checkbox(label = f'Order menu : {de_rc[0][1]} Won', key = 238):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col1_rc.text('Enter QTY. -')
                        c_col1_rc = col1_rc.number_input(label="239", min_value=1, key = 239, label_visibility="collapsed")
                        add_to_cart(de_rc[0][0], int(c_col1_rc), int(c_col1_rc) * int(de_rc[0][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
                col2_rc.text(de_rc[1][0]) 
                if col2_rc.checkbox(label = f'Order menu : {de_rc[1][1]} Won', key = 240):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col2_rc.text('Enter QTY. -')
                        c_col2_rc = col2_rc.number_input(label="241", min_value=1, key = 241, label_visibility="collapsed")
                        add_to_cart(de_rc[1][0], int(c_col2_rc), int(c_col2_rc) * int(de_rc[1][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")   
            with al_ro :
                start, end, due = ma.return_time(de_al[2][1]) 
                sentence = ma.time_sentence(start, end, due)
                st.text(sentence)
                de_ro = cond.get_menu(db, ['menu', 'price'], de_al[2][2], "*", "*", False)
                col1_ro, col2_ro = st.columns(2) # 종류 별 컬럼 생성
                col1_ro.text(de_ro[0][0]) # 첫 번째 종류에 대해 수량 입력받기
                if col1_ro.checkbox(label = f'Order menu : {de_ro[0][1]} Won', key = 242):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col1_ro.text('Enter QTY. -')
                        c_col1_ro = col1_ro.number_input(label="243", min_value=1, key = 243, label_visibility="collapsed")
                        add_to_cart(de_ro[0][0], int(c_col1_ro), int(c_col1_ro) * int(de_ro[0][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
            with al_ld :
                start, end, due = ma.return_time(de_al[3][1]) 
                sentence = ma.time_sentence(start, end, due)
                st.text(sentence)
                de_ld = cond.get_menu(db, ['menu', 'price'], de_al[3][2], "*", "*", False)
                col1_ld, col2_ld = st.columns(2) # 종류 별 컬럼 생성
                col1_ld.text(de_ld[0][0]) # 첫 번째 종류에 대해 수량 입력받기
                if col1_ld.checkbox(label = f'Order menu : {de_ld[0][1]} Won', key = 244):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col1_ld.text('Enter QTY. -')
                        c_col1_ld = col1_ld.number_input(label="245", min_value=1, key = 245, label_visibility="collapsed")
                        add_to_cart(de_ld[0][0], int(c_col1_ld), int(c_col1_ld) * int(de_ld[0][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
                col2_ld.text(de_ld[1][0]) 
                if col2_ld.checkbox(label = f'Order menu : {de_ld[1][1]} Won', key = 246):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col2_ld.text('Enter QTY. -')
                        c_col2_ld = col2_ld.number_input(label="247", min_value=1, key = 247, label_visibility="collapsed")
                        add_to_cart(de_ld[1][0], int(c_col2_ld), int(c_col2_ld) * int(de_ld[1][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")   
            with al_ww : 
                start, end, due = ma.return_time(de_al[4][1]) 
                sentence = ma.time_sentence(start, end, due)
                st.text(sentence)
                de_ww = cond.get_menu(db, ['menu', 'price'], de_al[4][2], "*", "*", False)
                col1_ww, col2_ww = st.columns(2) # 종류 별 컬럼 생성
                col1_ww.text(de_ww[0][0]) # 첫 번째 종류에 대해 수량 입력받기
                if col1_ww.checkbox(label = f'Order menu : {de_ww[0][1]} Won', key = 248):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col1_ww.text('Enter QTY. -')
                        c_col1_ww = col1_ww.number_input(label="249", min_value=1, key = 249, label_visibility="collapsed")
                        add_to_cart(de_ww[0][0], int(c_col1_ww), int(c_col1_ww) * int(de_ww[0][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
                col2_ww.text(de_ww[1][0]) 
                if col2_ww.checkbox(label = f'Order menu : {de_ww[1][1]} Won', key = 250):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col2_ww.text('Enter QTY. -')
                        c_col2_ww = col2_ww.number_input(label="251", min_value=1, key = 251, label_visibility="collapsed")
                        add_to_cart(de_ww[1][0], int(c_col2_ww), int(c_col2_ww) * int(de_ww[1][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")  
                col3_ww, col4_ww = st.columns(2) # 종류 별 컬럼 생성
                col3_ww.text(de_ww[2][0]) # 첫 번째 종류에 대해 수량 입력받기
                if col3_ww.checkbox(label = f'Order menu : {de_ww[2][1]} Won', key = 252):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col3_ww.text('Enter QTY. -')
                        c_col3_ww = col3_ww.number_input(label="253", min_value=1, key = 253, label_visibility="collapsed")
                        add_to_cart(de_ww[2][0], int(c_col3_ww), int(c_col3_ww) * int(de_ww[2][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
                col4_ww.text(de_ww[3][0]) 
                if col4_ww.checkbox(label = f'Order menu : {de_ww[3][1]} Won', key = 254):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col4_ww.text('Enter QTY. -')
                        c_col4_ww = col4_ww.number_input(label="255", min_value=1, key = 255, label_visibility="collapsed")
                        add_to_cart(de_ww[3][0], int(c_col4_ww), int(c_col4_ww) * int(de_ww[3][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")   
            with al_bb : 
                start, end, due = ma.return_time(de_al[5][1]) 
                sentence = ma.time_sentence(start, end, due)
                st.text(sentence)
                de_bb = cond.get_menu(db, ['menu', 'price'], de_al[5][2], "*", "*", False)
                col1_bb, col2_bb = st.columns(2) # 종류 별 컬럼 생성
                col1_bb.text(de_bb[0][0]) # 첫 번째 종류에 대해 수량 입력받기
                if col1_bb.checkbox(label = f'Order menu : {de_bb[0][1]} Won', key = 256):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col1_bb.text('Enter QTY. -')
                        c_col1_bb = col1_bb.number_input(label="257", min_value=1, key = 257, label_visibility="collapsed")
                        add_to_cart(de_bb[0][0], int(c_col1_bb), int(c_col1_bb) * int(de_bb[0][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
                col2_bb.text(de_bb[1][0]) 
                if col2_bb.checkbox(label = f'Order menu : {de_bb[1][1]} Won', key = 258):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col2_bb.text('Enter QTY. -')
                        c_col2_bb = col2_bb.number_input(label="259", min_value=1, key = 259, label_visibility="collapsed")
                        add_to_cart(de_bb[1][0], int(c_col2_bb), int(c_col2_bb) * int(de_bb[1][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")   
            with al_ch : 
                start, end, due = ma.return_time(de_al[6][1]) 
                sentence = ma.time_sentence(start, end, due)
                st.text(sentence)
                de_ch = cond.get_menu(db, ['menu', 'price'], de_al[6][2], "*", "*", False)
                col1_ch, col2_ch, col3_ch = st.columns(3) # 종류 별 컬럼 생성
                col1_ch.text(de_ch[0][0]) # 첫 번째 종류에 대해 수량 입력받기
                if col1_ch.checkbox(label = f'Order menu : {de_ch[0][1]} Won', key = 260):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col1_ch.text('Enter QTY. -')
                        c_col1_ch = col1_ch.number_input(label="261", min_value=1, key = 261, label_visibility="collapsed")
                        add_to_cart(de_ch[0][0], int(c_col1_ch), int(c_col1_ch) * int(de_ch[0][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
                col2_ch.text(de_ch[1][0]) 
                if col2_ch.checkbox(label = f'Order menu : {de_ch[1][1]} Won', key = 262):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col2_ch.text('Enter QTY. -')
                        c_col2_ch = col2_ch.number_input(label="263", min_value=1, key = 263, label_visibility="collapsed")
                        add_to_cart(de_ch[1][0], int(c_col2_ch), int(c_col2_ch) * int(de_ch[1][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")   
                col3_ch.text(de_ch[2][0]) 
                if col3_ch.checkbox(label = f'Order menu : {de_ch[2][1]} Won', key = 264):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col3_ch.text('Enter QTY. -')
                        c_col3_ch = col3_ch.number_input(label="265", min_value=1, key = 265, label_visibility="collapsed")
                        add_to_cart(de_ch[2][0], int(c_col3_ch), int(c_col3_ch) * int(de_ch[2][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")   
            with al_sp : 
                start, end, due = ma.return_time(de_al[7][1]) 
                sentence = ma.time_sentence(start, end, due)
                st.text(sentence)
                de_sp = cond.get_menu(db, ['menu', 'price'], de_al[7][2], "*", "*", False)
                col1_sp, col2_sp, col3_sp = st.columns(3) # 종류 별 컬럼 생성
                col1_sp.text(de_sp[0][0]) # 첫 번째 종류에 대해 수량 입력받기
                if col1_sp.checkbox(label = f'Order menu : {de_sp[0][1]} Won', key = 266):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col1_sp.text('Enter QTY. -')
                        c_col1_sp = col1_sp.number_input(label="267", min_value=1, key = 267, label_visibility="collapsed")
                        add_to_cart(de_sp[0][0], int(c_col1_sp), int(c_col1_sp) * int(de_sp[0][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
                col2_sp.text(de_sp[1][0]) 
                if col2_sp.checkbox(label = f'Order menu : {de_sp[1][1]} Won', key = 268):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col2_sp.text('Enter QTY. -')
                        c_col2_sp = col2_sp.number_input(label="269", min_value=1, key = 269, label_visibility="collapsed")
                        add_to_cart(de_sp[1][0], int(c_col2_sp), int(c_col2_sp) * int(de_sp[1][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")   
                col3_sp.text(de_sp[2][0]) 
                if col3_sp.checkbox(label = f'Order menu : {de_sp[2][1]} Won', key = 270):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col3_sp.text('Enter QTY. -')
                        c_col3_sp = col3_sp.number_input(label="271", min_value=1, key = 271, label_visibility="collapsed")
                        add_to_cart(de_sp[2][0], int(c_col3_sp), int(c_col3_sp) * int(de_sp[2][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")   
                col4_sp, col5_sp, col6_sp = st.columns(3) # 종류 별 컬럼 생성
                col4_sp.text(de_sp[3][0]) # 첫 번째 종류에 대해 수량 입력받기
                if col4_sp.checkbox(label = f'Order menu : {de_sp[3][1]} Won', key = 272):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col4_sp.text('Enter QTY. -')
                        c_col4_sp = col4_sp.number_input(label="273", min_value=1, key = 273, label_visibility="collapsed")
                        add_to_cart(de_sp[3][0], int(c_col4_sp), int(c_col4_sp) * int(de_sp[3][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
                col5_sp.text(de_sp[4][0]) 
                if col5_sp.checkbox(label = f'Order menu : {de_sp[4][1]} Won', key = 274):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col5_sp.text('Enter QTY. -')
                        c_col5_sp = col5_sp.number_input(label="275", min_value=1, key = 275, label_visibility="collapsed")
                        add_to_cart(de_sp[4][0], int(c_col5_sp), int(c_col5_sp) * int(de_sp[4][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")   
                col6_sp.text(de_sp[5][0]) 
                if col6_sp.checkbox(label = f'Order menu : {de_sp[5][1]} Won', key = 276):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col6_sp.text('Enter QTY. -')
                        c_col6_sp = col6_sp.number_input(label="277", min_value=1, key = 277, label_visibility="collapsed")
                        add_to_cart(de_sp[5][0], int(c_col6_sp), int(c_col6_sp) * int(de_sp[5][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")   
                col7_sp, col8_sp, col9_sp = st.columns(3) # 종류 별 컬럼 생성
                col7_sp.text(de_sp[6][0]) # 첫 번째 종류에 대해 수량 입력받기
                if col7_sp.checkbox(label = f'Order menu : {de_sp[6][1]} Won', key = 278):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col7_sp.text('Enter QTY. -')
                        c_col7_sp = col7_sp.number_input(label="279", min_value=1, key = 279, label_visibility="collapsed")
                        add_to_cart(de_sp[6][0], int(c_col7_sp), int(c_col7_sp) * int(de_sp[6][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
                col8_sp.text(de_sp[7][0]) 
                if col8_sp.checkbox(label = f'Order menu : {de_sp[7][1]} Won', key = 280):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col8_sp.text('Enter QTY. -')
                        c_col8_sp = col8_sp.number_input(label="281", min_value=1, key = 281, label_visibility="collapsed")
                        add_to_cart(de_sp[7][0], int(c_col8_sp), int(c_col8_sp) * int(de_sp[7][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")   
                col9_sp.text(de_sp[8][0]) 
                if col9_sp.checkbox(label = f'Order menu : {de_sp[8][1]} Won', key = 282):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col9_sp.text('Enter QTY. -')
                        c_col9_sp = col9_sp.number_input(label="283", min_value=1, key = 283, label_visibility="collapsed")
                        add_to_cart(de_sp[8][0], int(c_col9_sp), int(c_col9_sp) * int(de_sp[8][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")   
                col10_sp, col11_sp, col12_sp = st.columns(3) # 종류 별 컬럼 생성
                col10_sp.text(de_sp[9][0]) # 첫 번째 종류에 대해 수량 입력받기
                if col10_sp.checkbox(label = f'Order menu : {de_sp[9][1]} Won', key = 284):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col10_sp.text('Enter QTY. -')
                        c_col10_sp = col10_sp.number_input(label="285", min_value=1, key = 285, label_visibility="collapsed")
                        add_to_cart(de_sp[9][0], int(c_col10_sp), int(c_col10_sp) * int(de_sp[9][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
                col11_sp.text(de_sp[10][0]) 
                if col11_sp.checkbox(label = f'Order menu : {de_sp[10][1]} Won', key = 286):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col11_sp.text('Enter QTY. -')
                        c_col11_sp = col11_sp.number_input(label="287", min_value=1, key = 287, label_visibility="collapsed")
                        add_to_cart(de_sp[10][0], int(c_col11_sp), int(c_col11_sp) * int(de_sp[10][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")   
                col12_sp.text(de_sp[11][0]) 
                if col12_sp.checkbox(label = f'Order menu : {de_sp[11][1]} Won', key = 288):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col12_sp.text('Enter QTY. -')
                        c_col12_sp = col12_sp.number_input(label="289", min_value=1, key = 289, label_visibility="collapsed")
                        add_to_cart(de_sp[11][0], int(c_col12_sp), int(c_col12_sp) * int(de_sp[11][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")   
                col13_sp, col14_sp, col15_sp = st.columns(3) # 종류 별 컬럼 생성
                col13_sp.text(de_sp[12][0]) # 첫 번째 종류에 대해 수량 입력받기
                if col13_sp.checkbox(label = f'Order menu : {de_sp[12][1]} Won', key = 290):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col13_sp.text('Enter QTY. -')
                        c_col13_sp = col13_sp.number_input(label="291", min_value=1, key = 291, label_visibility="collapsed")
                        add_to_cart(de_sp[12][0], int(c_col13_sp), int(c_col13_sp) * int(de_sp[12][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
                col14_sp.text(de_sp[13][0]) 
                if col14_sp.checkbox(label = f'Order menu : {de_sp[13][1]} Won', key = 292):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col14_sp.text('Enter QTY. -')
                        c_col14_sp = col14_sp.number_input(label="293", min_value=1, key = 293, label_visibility="collapsed")
                        add_to_cart(de_sp[13][0], int(c_col14_sp), int(c_col14_sp) * int(de_sp[13][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")   
                col15_sp.text(de_sp[14][0]) 
                if col15_sp.checkbox(label = f'Order menu : {de_sp[14][1]} Won', key = 294):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col15_sp.text('Enter QTY. -')
                        c_col15_sp = col15_sp.number_input(label="295", min_value=1, key = 295, label_visibility="collapsed")
                        add_to_cart(de_sp[14][0], int(c_col15_sp), int(c_col15_sp) * int(de_sp[14][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")                   
                col16_sp, col17_sp, col18_sp = st.columns(3) # 종류 별 컬럼 생성
                col16_sp.text(de_sp[15][0]) 
                if col16_sp.checkbox(label = f'Order menu : {de_sp[15][1]} Won', key = 296):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col16_sp.text('Enter QTY. -')
                        c_col16_sp = col16_sp.number_input(label="297", min_value=1, key = 297, label_visibility="collapsed")
                        add_to_cart(de_sp[15][0], int(c_col16_sp), int(c_col16_sp) * int(de_sp[15][1])) 
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")       
            with al_rw : 
                start, end, due = ma.return_time(de_al[8][1]) 
                sentence = ma.time_sentence(start, end, due)
                st.text(sentence)
                de_rw = cond.get_menu(db, ['menu', 'price'], de_al[8][2], "*", "*", False)
                col1_rw, col2_rw, col3_rw = st.columns(3) # 종류 별 컬럼 생성
                col1_rw.text(de_rw[0][0]) # 첫 번째 종류에 대해 수량 입력받기
                if col1_rw.checkbox(label = f'Order menu : {de_rw[0][1]} Won', key = 298):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col1_rw.text('Enter QTY. -')
                        c_col1_rw = col1_rw.number_input(label="299", min_value=1, key = 299, label_visibility="collapsed")
                        add_to_cart(de_rw[0][0], int(c_col1_rw), int(c_col1_rw) * int(de_rw[0][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
                col2_rw.text(de_rw[1][0]) 
                if col2_rw.checkbox(label = f'Order menu : {de_rw[1][1]} Won', key = 300):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col2_rw.text('Enter QTY. -')
                        c_col2_rw = col2_rw.number_input(label="301", min_value=1, key = 301, label_visibility="collapsed")
                        add_to_cart(de_rw[1][0], int(c_col2_rw), int(c_col2_rw) * int(de_rw[1][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")   
                col3_rw.text(de_rw[2][0]) 
                if col3_rw.checkbox(label = f'Order menu : {de_rw[2][1]} Won', key = 302):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col3_rw.text('Enter QTY. -')
                        c_col3_rw = col3_rw.number_input(label="303", min_value=1, key = 303, label_visibility="collapsed")
                        add_to_cart(de_rw[2][0], int(c_col3_rw), int(c_col3_rw) * int(de_rw[2][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")   
                col4_rw, col5_rw, col6_rw = st.columns(3) # 종류 별 컬럼 생성
                col4_rw.text(de_rw[3][0]) # 첫 번째 종류에 대해 수량 입력받기
                if col4_rw.checkbox(label = f'Order menu : {de_rw[3][1]} Won', key = 304):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col4_rw.text('Enter QTY. -')
                        c_col4_rw = col4_rw.number_input(label="305", min_value=1, key = 305, label_visibility="collapsed")
                        add_to_cart(de_rw[3][0], int(c_col4_rw), int(c_col4_rw) * int(de_rw[3][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
                col5_rw.text(de_rw[4][0]) 
                if col5_rw.checkbox(label = f'Order menu : {de_rw[4][1]} Won', key = 306):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col5_rw.text('Enter QTY. -')
                        c_col5_rw = col5_rw.number_input(label="307", min_value=1, key = 307, label_visibility="collapsed")
                        add_to_cart(de_rw[4][0], int(c_col5_rw), int(c_col5_rw) * int(de_rw[4][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")   
                col6_rw.text(de_rw[5][0]) 
                if col6_rw.checkbox(label = f'Order menu : {de_rw[5][1]} Won', key = 308):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col6_rw.text('Enter QTY. -')
                        c_col6_rw = col6_rw.number_input(label="309", min_value=1, key = 309, label_visibility="collapsed")
                        add_to_cart(de_rw[5][0], int(c_col6_rw), int(c_col6_rw) * int(de_rw[5][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")   
                col7_rw, col8_rw, col9_rw = st.columns(3) # 종류 별 컬럼 생성
                col7_rw.text(de_rw[6][0]) # 첫 번째 종류에 대해 수량 입력받기
                if col7_rw.checkbox(label = f'Order menu : {de_rw[6][1]} Won', key = 310):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col7_rw.text('Enter QTY. -')
                        c_col7_rw = col7_rw.number_input(label="311", min_value=1, key = 311, label_visibility="collapsed")
                        add_to_cart(de_rw[6][0], int(c_col7_rw), int(c_col7_rw) * int(de_rw[6][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")
                col8_rw.text(de_rw[7][0]) 
                if col8_rw.checkbox(label = f'Order menu : {de_rw[7][1]} Won', key = 312):
                    if ma.weekday_true() and ma.open_true(start, due) :
                        col8_rw.text('Enter QTY. -')
                        c_col8_rw = col8_rw.number_input(label="313", min_value=1, key = 313, label_visibility="collapsed")
                        add_to_cart(de_rw[7][0], int(c_col8_rw), int(c_col8_rw) * int(de_rw[7][1]))
                    else : st.popover(label="주문 가능한 시간이 아닙니다.")   
    with cart:
        hide_table_row_index = """
        <style>
        thead tr th:first-child {display:none}
        tbody th {display:none}
        </style>
        """
        st.markdown(hide_table_row_index, unsafe_allow_html=True)

        # 메뉴 리스트를 카트에 담을 수 있도록 전처리    
        order = {
                'Food Name': food_list,
                'Qty' : qty_list,
                'Amount': amt_list
        }
                
        cart = pd.DataFrame(order)
        cart_final = cart.dropna()
        cart_final['Qty'].astype(int)
        st.table(cart_final)
        st.button ("Order Now", on_click=order_pressed, args = ('브런치(주중)', food_list, qty_list, amt_list))

    with receipt :
        hide_table_row_index = """
        <style>
        thead tr th:first-child {display:none}
        tbody th {display:none}
        </style>
        """
        st.markdown(hide_table_row_index, unsafe_allow_html=True)

        details = {
                'order_id' : [],
                'title' : [],
                'room_number' : [],
                'order_total' : [], 
                'order_time' : [],
                'status' : []
        }
        order_list = {
                'order_id' : [],
                'item_name' : [],
                'quantity' : [], 
                'price' : []          
        }
        detail, order_lists = cond.make_receipt("the_order_lounge", st.session_state["customer_name"])
        order_ids = []
        for i in range(len(detail)) :
            order_ids.append(detail[i][0])
        option = st.selectbox("If the status of an order is 'ordered' than you can cancel it.", order_ids) 
        for i in range(len(detail)) :
            order_id, title, room_number, order_total, order_time, status = detail[i]
            if option == order_id :
                details['order_id'].append(order_id)
                details['title'].append(title)
                details['room_number'].append(room_number)
                details['order_total'].append(order_total)
                details['order_time'].append(order_time)
                details['status'].append(status)
        for key in details['order_id'] :
            if key == option :
                for i in range(len(order_lists[key])) :
                    item_name, quantity, price = order_lists[key][i]
                    order_list['order_id'].append(key)
                    order_list['item_name'].append(item_name)
                    order_list['quantity'].append(quantity)
                    order_list['price'].append(price)
        details_final = pd.DataFrame(details)
        st.dataframe(details_final)
        order_list_final = pd.DataFrame(order_list)
        st.dataframe(order_list_final)

        st.button ("Cancel the order", on_click=cancel_pressed, args = (option, 'Canceled'))
        st.button ("Reorder the order", on_click=reorder_pressed, args = (option, 'Reordered'))
        
    with return_b :
        st.page_link("main_ui.py", label="처음페이지로 돌아가기")

    st.text(ti.alert_the_lounge)

with headerSection:
    if 'room_number' not in st.session_state :
        st.session_state['room_number'] = "305"
    if 'customer_name' not in st.session_state :
        st.session_state['customer_name'] = "Charlie"
    st.title("Online Food Ordering System 😋")
    show_rounge_page()