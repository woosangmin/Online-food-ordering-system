# import requests, json

# url = 'http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService/getRestDeInfo'
# params ={'serviceKey' : 'YourAPIkey', 'pageNo' : '1', 'numOfRows' : '30', 'solYear' : '2024', 'solMonth' : '', '_type' : 'json' }

# response = requests.get(url, params=params)
# print(json.loads(response.text))


import datetime
holidays_2024 = [ "2024-01-01",   "2024-02-09", "2024-02-10", "2024-02-11", "2024-02-12", "2024-03-01", "2024-04-10", "2024-05-05", "2024-05-06", "2024-05-15", 
                 "2024-06-06", "2024-08-15", "2024-09-16", "2024-09-17", "2024-09-18", "2024-10-03", "2024-10-09", "2024-12-25" ]
                 # 신정 / 설날 연휴 시작 / 설날 / 설날 연휴 끝 / 설날 대체 공휴일 / 삼일절 / 국회의원 선거일 / 어린이날 / 어린이날 대체 공휴일 / 석가탄신일 / 현충일 /
                 # 광복절 / 추석 연휴 시작 / 추석 / 추석 연휴 끝 / 개천절 / 한글날 / 성탄절

now = datetime.datetime.now()
weekday = now.weekday()
date = now.date()
time=now.strftime('%H:%M:%S')

# 주말인지 휴일인지 확인
def weekday_true() :
    if weekday <= 4 and date not in holidays_2024 :
        today = True
    else :
        today = False
    return today

# 시간이 도래했는지 확인
def open_true(start, due) :
    if (time < start) or (time > due) :
        return False
    else :
        return True

# 시간을 시작, 종료, 주문 마감 시간으로 분할
def return_time(time) :
    start, end, due = time.split(",")
    return start, end, due

# 시작, 종료, 주문 마감 시간을 문장으로 구성
def time_sentence(start, end, due) :
    sentence = f"{start} ~ {end} / last order {due}"
    return sentence