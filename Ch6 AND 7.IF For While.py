#6장 조건문
"""
조건문의 if의 기본 구조

if 조건식1 : 
    실행문1
else:
    실행문2
조건식1이 참이면 실행문1 실행, 거짓이면 실행문2 실행

"""

money = 1500
if money >= 3000:
    print("결제 가능")
else:
    print("결제 불가")
#조건문 작성시 들여쓰기 조심하기 
print("다른카드로 결제해주세요") # 조건식에 속하지 않은 출력문

#elif 조건문  c/cpp에서의 else if랑 같다.
""" 
조건을 여러개 사용시 사용 
if 조건1 :
    실행1
elif 조건2 : -> elif는 갯수제한이 없다.
    실행2
else:
    실행3
"""
click = int(input("1번~3번 중에서 입력해주세요 : "))

if click == 1:
    print("된찌")
elif click == 2 : 
    print("순두부찌개")
elif click == 3 :
    print("김찌")
else:
    print("다른번호을 입력해서 오류 발생")

print("한식은 맛있습니다.")

#else가 필요 없으면 생략해도 됨
#else 사용시 마지막에 적어야함 

#중첩 반복문

x = 20
if x >= 10:
    if x == 20:
        print("20입니다")
    else:
        print("숫자가 큽니다.")
else:
    if x == 7:
        print("7입니다.")
    else:
        print("숫자가 작습니다.")

#7장 반복문 For While
"""
for문
for 변수 in range(시작숫자, 끝나는 숫자):
    실행문

range(끝나는 숫자) -> 0 부터 끝나는 숫자 -1 까지 1간격으로 반복 
시작 숫자는 0으로 자동 설정
range(시작 숫자, 끝나는 숫자) -> 시작 숫자부터 끝나는 숫자-1까지 1간격으로 반복
ragne(시작,끝,간격) -> 시작부터 끝나는 숫자 -1까지 지정된 가격으로 반복 
간격을 적을때 반드시 시작숫자를 적어야함 
음수도 가능
"""
for i in range(10):
    print(i)

for i in range(10,20,3):
    print(i)

for i in range(20,0,-6):
    print(i)

#중첩 반복문
for i in range(2,10):
    for j in range(1,10):
        print(i*j,end = " ")
    print()

#while 반복문
"""
while 조건 :
    실행
"""

y = 1
while y <= 3: 
    print(y)
    y += 1

#반복문 속에 조건문과 break 
"""
반복문 안에 조건식으로 넣어서 멈출 수 있음
또는 브레이크로 반복문에서 탈출할 수 있게함 

"""
hit = 0 
while hit < 5 : 
    hit = hit + 1
    print("나무를",hit,"번 찍었습니다.")
    if hit == 5:
        print("나무가 쓰러집니다.")

num = 0 
while 1:
    num = int(input("문을 여시겠습니까? (1:yes/2:no) : "))
    if num == 1 :
        print("문이 열렸습니다.")
        break
    elif num == 2: 
        print("문을 열 수 없습니다.")
        break
    else : 
        print("오류 발생")
 

#7-3번 문제
sum = 0
i = 1 
while i < 10 :
    sum += i
    i = i + 1
print("합 : ", sum)

#7-4번 문제 팩토리얼 출력
fact = 1 
for i in range(1,6):
    fact = fact * i
print(fact)

#7-4번 문제 팩토리얼 출력
fact = 1 
for i in range(5,0,-1):
    fact = fact * i
print(fact)