#15장 파이썬 응용
"""
모듈 - 함수,변수,클래스 등을 모아 놓은 파이썬 파일 1 개 
패키지 - 모듈을 여러개 모아 관리하는 하나의 폴더
라이브러리 - 다른 사람들이 사용할 수 있도록 유용한 기능을 모듈이나 패키지로 만들어 놓은 것
프레임워크 - 목적에 따라 코드를 쉽게 작성할 수 있도록 미리 만들어 놓은 뼈대 

모듈을 사용하기 위해선 import가 필요하다. 
""" 
import gugudan
gugudan.gugu2()

# 라이브러리 또한 import 사용, 라이브러를 설명한 문서나 웹사이트 확인하고 활용하면 됨
"""
파이썬에 속한 기본 라이브러리 

1. rabdom
랜덤은 실행할 때 마다 새로운 난수가 생성
임의의 수를 원하는 범위, 원하는 형식으로 생성가능
random(), randint()등의 함수가 포함되어 있음

2. time
시간과 관련된 라이브러리. time(), ctime()등이 포함되어 있음
time() - UTC기준으로 한 시간을 실수 형태로 반환 함수 
(1970-01-01-0-0-0부터 지난 시간을 초단위 형태로 표현)
ctime() - 현재 시각을 문자열로 반환하는 함수
"""
#랜덤 라이브러리
import random
print(random.random()) #난수 생성 
print(random.randint(1,100)) # 1~100 중 임의의 수 하나 출력

#시간 라이브러리
import time
print(time.time()) #utc기준
print(time.ctime()) #현재 시간을 문자열로 표현 

#sleep()함수
print("3초 뒤에 시작합니다.")
time.sleep(3) # 3초뒤에 실행
print("hello Python")

# 오류의 종류
"""
1. 구문 오류 - 문법 오류
Syntax Error는 문법, 즉 오타가 있는경우 발생함 

2. 런타임 오류 - 문법은 맞으나 명령어를 잘못 사용하여 발생한 오류
Runtime Error는 코드를 실행하는 중에 발생하는 오류
숫자를 0으로 나누는거나, 정의하지는 변수를 사용하거나 모듈이 없거나 등 다양한 런타임 오류가 발생

자주 발생하는 런타임 오류의 종류 
NameError - 정의하지 않은 변수를 사용했을 떄 발생하는 오류
ZeroDivisionError - 숫자를 0으로 나누었을 때 발생하는 오류
IndexError - 주로 리스트나 튜플에서 존재하지 않는 인덱스 위치로 인덱싱했을 떄 발생하는 오류
KeyError - 주로 딕셔너리에 존재하지 않는 key 값으로 값을 가져오려 할 경우 발생하는 오류
AttributeError - 클래스와 라이브러리에서 존재하지 않는 속성이나 함수를 사용할 때 발생하는 오류
TypeError - 잘못된 타입이나 연산을 사용한 경우에 발생하는 오류
특히, 숫자 변수와 문자변수를 연산하게 되면 흔하게 발생

3. 논리 오류 - 실행은 되지만, 프로그램의 논리가 맞지않아 원하는 결과가 나오지 않는 오류 
Logic Error - 구문 오류나 런타임 오류 없이 잘 실행되지만 원하는 대로 동작하지 않는 오류
코드의 알고리즘을 잘못 구성하여 발생하는 버그 
별도의 오류가 출력되지 않아, 직접 버그를 찾아야함 

"""

#논리 오류의 예
# a+b를 더하고 그 둘의 평균을 구하고 싶음
a = 10
b= 20
aver = a+b/2 # 논리 오류로 a+b/2가아닌 (a+b)/2로 수정해야함
print(aver)

#예외 처리 
"""
런타임 오류는 예외 처리로 오류 발생을 대비할 수있음
적절한 예외 처리는 프로그램 성능 향상에 도움이 됨
try:
    코드
except:
    오류가 발생했을 때 실행문 

여러 예외처리를 하고싶으면 except 오류1: 를 추가하면 된다.

"""
#예외처리 1
try:
     x= int(input("첫 번째 숫자를 입력 : "))
     y = int(input("두 번쨰 숫자를 입력 : "))
     print(x/y)
except:
     print("오류발생, 다시 시도") 

#예외처리2
x = [10,20,30]

try:
     index= int(input("인덱스를 입력 : "))
     num = x[index]
     y = int(input("나눌 숫자를 입력 : "))
     print(num/y)
except IndexError:
     print("오류발생, 인덱스는 0부터 2까지 입력 가능합니다.") 
except ZeroDivisionError:
     print("숫자는 0으로 나눌수 없습니다.")

#파이썬 내장 함수 
"""
자주 사용하는 내장 함수
1. enumerate()
enumerate(시퀀스형 데이터)
리스트로 for반복문 작성할 때 유용한 함수
리스트,튜플,문자열 등 순서가 있는 시퀀스형 데이터를 enumerate 함수에 넣고 그 모든 요소를 인덱스와 쌍으로 추출하는데 사용

2. round()
round(숫자, 반올림할 자릿수)
숫자를 반올림하는 함수, 실수 하나만 넣으면 정수로 반올림된 값이 반환됨

3. filter()
filter(함수, 시퀀스형 또는 딕셔너리형 데이터)
리스트, 튜플 등의 시퀀스형 데이터나 딕셔너리형 데이터에서 필터링한 결과를 반환하는 함수
전달인자로 어떤 함수와 데이터를 함꼐 넣고, filter함수 내에서 ㅈ동으로 데이터를 순서대로 반복하며 함수를 실행
함수의 반화값이 "참"인 데이터만 반환

4. map()
map(함수,시퀀스형 또는 딕셔너리 )
시퀀스형 데이터나 딕셔너리형 데이터의 값을 자동으로 반복하여 함수에 전달인자를 넣고
그 함수의 결과를 묶어 반환하는 함수
filter함수와 사용 방법이 비슷, 함수와 데이터를 함께 넣으면 map함수 내에서 자동으로 데이터를 순서대로 반복하며 함수를 실행.
"""

# enumerate()
for index, value in enumerate(["a","b","c","d","e"]):
     print(index,value)

# round()
print(round(3.4))
print(round(3.46,1))

# filter()
def isEven(num):
     return num % 2 == 0
filtered = list(filter(isEven,[1,4,3,2,6,5,3,4]))
print(filtered)

# map()
def multiply(num):
     return num * 2
mapped = list(map(multiply,[1,3,4,2,5,3]))
print(mapped)