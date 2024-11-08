import mysql.connector


# 스키마 불러오기
def connect_db(db_name) :
    db = mysql.connector.connect(
    host='localhost',
    user='test',
    password='zoqtmxhs1!',
    database=db_name
    )
    return db

# 메뉴 불러오기
def get_menu(db, column_list, table_name, target, target_value, true) :
    mc = db.cursor()
    columns = ""
    for i in range(len(column_list)) :
        if i < len(column_list) - 1 :
            columns += column_list[i] + ", "
        else :
            columns += column_list[i]
    if true == True :
        if type(columns) == str and type(table_name) == str and type(target) == str and type(target_value) == str :
            sentence = f"SELECT {columns} FROM {table_name} where {target} = '{target_value}'"
    else :
        if type(columns) == str and type(table_name) == str :
            sentence = f"SELECT {columns} FROM {table_name}"
    mc.execute(sentence)
    detail = mc.fetchall()
    return detail

# 주문 상태 확인
def get_status(db_name, change, order_id) :
    db = connect_db(db_name)
    mc = db.cursor()
    st_bool = True
    sentence = f"SELECT status FROM orders where order_id = {order_id}"
    mc.execute(sentence)
    status = mc.fetchall()[0][0]
    if change == "Canceled" :
        if status == "Ordered" or status == 'Reordered' :
            st_bool = True
        else :
            st_bool = False
    elif change == "Reordered" :
        if status == "Canceled" :
            st_bool = True
        else :
            st_bool = False
    return st_bool

# 주문 상태 바꾸기
def change_status(db_name, change, order_id) :
    db = connect_db(db_name)
    mc = db.cursor()
    try :
        query = "UPDATE orders SET status = %s where order_id = %s"
        values = (change, order_id)
        mc.execute(query, values)
        db.commit()
        return True
    except :
        return False

# order id 불러오기
def get_order_id(db) :
    mc = db.cursor()
    sentence = "SELECT order_id FROM order_count"
    mc.execute(sentence)
    order_id = mc.fetchall()[0][0]
    if update_order_id(db, order_id) :
        return order_id

# order id 업데이트
def update_order_id(db, order_id) :
    mc = db.cursor()
    try :
        query = "UPDATE order_count SET order_id = %s WHERE order_id = %s"
        new_order_id = order_id + 1
        parameters = (new_order_id, order_id)
        mc.execute(query, parameters)
        db.commit()
        return True
    except :
        return False
    
# 주문 입력
def place_order(db_name, title, food_list, qty_list, amt_list, customer_name, room_number, order_time) :
    try :
        db = connect_db(db_name)
        mc = db.cursor()
        order_id = get_order_id(db)
        order_total = 0
        for i in range(len(qty_list)) :
            order_total += (qty_list[i] * amt_list[i])
            if type(order_id) == int and type(food_list[i]) == str and type(qty_list[i]) == int and type(amt_list[i]) == int :
                food_name = food_list[i].replace("\n", " ")
                mc.execute(f"INSERT INTO order_items (order_id, item_name, quantity, price) VALUES ({order_id}, '{food_name}', {qty_list[i]}, {amt_list[i]})")
        if type(order_id) == int and type(title) == str and type(customer_name) == str and type(room_number) == str and type(order_total) == int and type(order_time) == str :
            mc.execute(f"INSERT INTO orders (order_id, title, customer_name, room_number, order_total, order_time, status) VALUES ({order_id}, '{title}', '{customer_name}', '{room_number}', {order_total}, '{order_time}', 'Ordered')")
        db.commit()
        return True
    except :
        db.rollback()
        return False
    
# 영수증 제작
def make_receipt(db_name, customer_name) :
    try :
        order_lists = dict()
        db = connect_db(db_name)
        mc = db.cursor()
        if type(customer_name) == str :
            mc.execute(f"SELECT order_id, title, room_number, order_total, order_time, status from orders WHERE customer_name = '{customer_name}'")
        detail = mc.fetchall()
        for i in range(len(detail)) :
            order_id = detail[i][0]
            if type(order_id) == int :
                mc.execute(f"SELECT item_name, quantity, price from order_items where order_id = {order_id}")
            order_list = mc.fetchall()
            order_lists[order_id] = order_list
        return detail, order_lists
    except :
        return False