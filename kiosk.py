'''** 호텔 내 마트 물건 판매 키오스크 시스템 **'''
import turtle # turtle 모듈 사용
import datetime # datetime 모듈 사용
t = turtle.Turtle()
t.shape("turtle")
t.speed(3)
now = datetime.datetime.now()
customer_id = ["kim", "park", "choi", "lee"] # 리스트 기능 추가
customer_password = ["kim1", "park2", "choi3", "lee4"]
stop_count = 0
buy_sum = 0
item_num = []
item_count = 0
restart_count = 0
rental_items = {'가습기' : 2000,'아기침대' : 0,'아기욕조' : 0,'유모차' : 5000,
                '스탠드' : 0, '체온계' : 0, '휠체어' : 0, '라디에이터' : 2000,
                '선풍기' : 2000, '블루투스스피커' : 3000, '핸드폰충전기' : 1000,
                '5구멀티탭' : 2000}
selling_items = {'일회용세면도구세트' : 3000, '클렌징폼' : 5000, '로션' : 6500,
                 '마스크팩' : 5000, '잠옷' : 20000, '빗' : 3000, '입욕제' : 10000,
                 '디퓨저' : 23000, '와인잔' : 20000, '머그잔' : 15000, '우산' : 5000,
                 '보조배터리' : 15000, '삼각대' : 8000, '담요' : 5000, '손소독제' : 3000,
                 '일회용마스크' : 2000}
shopping_basket = {}
# 딕셔너리 활용 추가
IDTF = 0
PWDTF = 0
count = 0
logintab = 0
YN = "none"
def register_user(): # 회원가입 함수
    print("신규 회원 가입을 진행합니다.")
    register_id = input("아이디를 입력하세요 : ")
    customer_id.append(register_id)
    register_pwd = input("비밀번호를 입력하세요 : ")
    customer_password.append(register_pwd)
    print("회원가입이 성공적으로 진행되었습니다.")
    print("가입을 축하드립니다.")

def init_location(): # turtle 위치 초기화 함수
    t.penup()
    t.right(90)
    t.forward(400)
    t.left(180)
    t.pendown()

def direct_location(section_count, way): # 물품 경로 추출 함수
    i = 0
    while i < section_count:
        t.forward(50)
        i += 1
    if way == 1:
        t.left(90)
    elif way == 2:
        t.right(90)
    t.forward(350)
    t.penup()
    t.forward(25)
    t.right(90)
    t.forward(25)
    t.pendown()

def square(): # 사각형 제작 함수
    t.color("red")
    for i in range(4):
        t.right(90)
        t.forward(50)
    t.penup()
    t.color("black")
    
def location_service(key, way): # 물품 경로 안내 함수
    if choice_item == key:
        print("선택 물품 : "+key)
        print('경로를 안내해드리겠습니다.')
        print("****************거북이의 출발위치는 현재 고객님의 위치입니다.****************")
        direct_location(section_count, way)
        square()

print("퀵 마트 방문을 환영합니다!") # print()기능 추가
while(logintab != 1): #반복문 사용
    try: #예외처리
        choicemenu = int(input("로그인을 진행해주세요. (1:로그인 / 2:회원가입) : ")) # 로그인 기능
        if(choicemenu == 1):
            while(IDTF == 0 or PWDTF == 0):
                id = input("아이디를 입력하세요 : ")
                count = 0
                for i in customer_id:
                    if(id == i):
                        IDTF = 1
                        break;
                    count += 1
                if(IDTF == 1):
                    pwd = input("비밀번호를 입력하세요 : ")
                    if(pwd == customer_password[count]):
                        print(customer_id[count]+'님,'+'방문을 환영합니다!')
                        PWDTF = 1
                        logintab = 1
                    else:
                        print("아이디 또는 비밀번호가 올바르지 않습니다. 다시 입력해주세요.")

                else:
                    print("아이디 또는 비밀번호가 올바르지 않습니다. 다시 입력해주세요.")
        elif(choicemenu == 2):
            register_user()
        else:
            print("제시된 번호 중에 선택해주세요!")
    except ValueError:
        print("주어진 번호를 입력해주세요!")
print("---------------------------- 물품 정보(대여) ----------------------------")
for key, value in rental_items.items():
    print('대여제품 : ['+key + '] \t\t대여가격 : ['+str(value)+'원]') #int str변환
print("---------------------------- 물품 정보(구매) ----------------------------")
for key, value in selling_items.items():
    print('구매제품 : ['+key + '] \t\t구매가격 : ['+str(value)+'원]')


while(stop_count == 0):
    t.home()
    init_location()
    t.pendown()
    try:
        choice_action = int(input("원하는 작업을 선택하세요 : (1.구매 / 2.물품위치탐색) : "))
        if(choice_action == 1): # 구매 기능
            choice_item = input("구매하실 물품 이름을 정확히 입력해주세요 : ")
            for key, value in rental_items.items():
                if choice_item == key:
                    print(key+"의 가격은 : "+str(value)+"원입니다.")
                    try:
                        item_sum = int(input("몇 개를 담으시겠습니까? "))
                        item_num.append(item_sum) # 리스트 추가 기능
                    except ValueError:
                        print("정수를 입력해주세요!")
                        break
                    YN = input("장바구니를 더 채우시겠습니까? (네/아니오) : ")
                    if(YN == "네"):
                        shopping_basket[key] = value
                        print("---------------------------- 현 장바구니 현황 ----------------------------")
                        item_count = 0
                        for key, value in shopping_basket.items():
                            item_add = value * item_num[item_count]
                            print('제품 : ['+key + '] \t\t수량 :'+str(item_num[item_count])+'개 \t구매가격 : ['+str(item_add)+'원]')
                            item_count += 1
                    else:
                        shopping_basket[key] = value
                        item_count = 0
                        for key, value in shopping_basket.items():
                            item_add = value * item_num[item_count]
                            buy_sum += item_add
                            print('제품 : ['+key + '] \t\t수량 :'+str(item_num[item_count])+'개 \t구매가격 : ['+str(item_add)+'원]')
                            item_count += 1
                        print("총 금액 : ", buy_sum, "원")
                        YN = input("결제하시겠습니까? (네/아니오) : ")
                        if(YN == "네"):
                            print("결제하신 시각은 ", now.month,"월", now.day,"일", now.hour,"시", now.minute, "분", now.second, "초입니다.") #datetime 모듈 기능 사용
                            stop_count = 1
                        else:
                            stop_count = 1
                            restart_count = 1
            for key, value in selling_items.items():
                if choice_item == key:
                    print(key+"의 가격은 : "+str(value)+"원입니다.")
                    try:
                        item_sum = int(input("몇 개를 담으시겠습니까? "))
                        item_num.append(item_sum)
                    except ValueError:
                        print("정수를 입력해주세요!")
                        break
                    YN = input("장바구니를 더 채우시겠습니까? (네/아니오) : ")
                    if(YN == "네"):
                        shopping_basket[key] = value
                        print("---------------------------- 현 장바구니 현황 ----------------------------")
                        item_count = 0
                        for key, value in shopping_basket.items():
                            item_add = value * item_num[item_count]
                            print('제품 : ['+key + '] \t\t수량 :'+str(item_num[item_count])+'개 \t구매가격 : ['+str(item_add)+'원]')
                            item_count += 1
                    else:
                        shopping_basket[key] = value
                        item_count = 0
                        for key, value in shopping_basket.items():
                            item_add = value * item_num[item_count]
                            buy_sum += item_add
                            print('제품 : ['+key + '] \t\t수량 :'+str(item_num[item_count])+'개 \t구매가격 : ['+str(item_add)+'원]')
                            item_count += 1
                        print("총 금액 : ", buy_sum, "원")
                        YN = input("결제하시겠습니까? (네/아니오) : ")
                        if(YN == "네"):
                            print("결제하신 시각은 ", now.month,"월", now.day,"일", now.hour,"시", now.minute, "분", now.second, "초입니다.")
                            stop_count = 1
                        else:
                            stop_count = 1
                            restart_count = 1
        elif(choice_action == 2): # 탐색 기능
            choice_item = input("탐색하실 물품 이름을 정확히 입력해주세요 : ")
            section_count = 0
            way = 0
            for key, value in rental_items.items():
                section_count += 1
                way = 1
                location_service(key, way) #함수를 통해 turtle기능 간소화
            section_count = 0
            for key, value in selling_items.items():
                section_count += 1
                way = 2
                location_service(key, way)
        else:
            print("제시된 번호 중에 선택해주세요!")
    
    except ValueError:
        print("주어진 번호를 입력해주세요!")
    t.penup()

#미구매시 재시작요청
if restart_count == 1:
    print("Please Restart")

#영수증 출력 부분
else:
    item_count = 0
    print("")
    print("")
    print("")
    print("=========================================================================")
    print("                                 영수증                                 ")
    print("상  호 : 퀵마트(본점)")
    print("사업자번호 : XXXXXXXX 대표자 : XXX")
    print("주  소 : 서울특별시 XX구 XX동 XXXX")
    print("전화번호 : 02-XXXX-XXXX")
    print("")
    print(now.year, "년", now.month,"월", now.day,"일", now.hour,"시", now.minute, "분", now.second, "초", end="")
    print("\t\t No. \t 01-ADMIN")
    print("=========================================================================")
    print("메 뉴 명 \t\t 단가 \t\t수량 \t\t 금액")
    print("=========================================================================")
    for key, value in shopping_basket.items():
        print(key)
        print("\t\t\t",value ,"\t\t",item_num[item_count],"\t\t",value*item_num[item_count])
        item_count += 1
    print("=========================================================================")
    print("소  계 \t\t\t\t\t\t\t{0:,.0f}원".format(buy_sum)) #format()함수 사용
    print("승인번호 : XXXX-XXXX-XXXX-XXXX")
    print("즐거운 이용 되십시오!!")
