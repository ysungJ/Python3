"""
변수란? 데이터를 저장하기 위해 만들어 놓은 메모리 공간
저장되는 데이터는 바뀔 수 있음
= 대입 (저장하는의미), == EQUAL 즉 동등하다는 의미
"""
name = "Yusung"
print("name = ", name)

#변수 데이터는 계속 바낄 수 있음
# 새 데이터 넣으면 기존 대이터는 사라짐
name = "Yonsei"
print(name)

a = 10
b = a 
print(b)

"""
자료형= 데이터형식 
파이썬에서는 문자열, 정수,실수,리스트,튜플,딕셔너리,집합이 대표적인 자료형 
이것 외에도 많은 자료형이 있다.
"""
print(type("문자열")) #str 문자열
print(type("1")) #int 정수형
print(type("1.5")) #float 실수형
print(type("True")) #bool 불형
print(type("[1,2,3]")) #list 리스트형
print(type((4,5,6))) #tuple 튜플형
print(type({"NAME":"yonsei"})) #dict 딕셔너리

#숫자형과 문자형의 차이
print("2024+20") 
print(10+50)
print(type("2024+20")) #str 문자열
print(type(10+50)) #int 정수형

#불 자료형 참과 거짓을 판단
#Ture, Flase는 대소문자를 지켜야한다. 다르면 자료형으로 인식 x
print(3<4) #Ture
print(1>2) #Flase

"""
변수 이름 규칙
1. 변수 이름은 숫자로 인식 x
ex) name1, n2ame는 가능 but, 3name은 불가능
2.변수 이름에 공백 사용 불가 
ex) score = 80 가능 sco re = 80 불가능 -> 오류 발생
3. 예약어는 변수 이름으로 사용 불가 -> 파이썬 뿐만아니라 C/CPP에서도 똑같음
ex) int = 10, True = "참"
--------------------------------
권장
1. 변수 이름은 스네이크 케이스를 따라 짓기

a. 카멜 케이스 - 첫 단어는 모두 소문자, 두번째 단어 부터는 첫 글자를 대문자로 시작
pythonClassName
b.케밥 케이스 - 모두 소문자로 표기, -로 구분
python-class-name
c. 파스칼 케이스 - 단어의 첫 글자는 모두 대문자, 나머지는 소문자로 표기
PythonClassName 
d. 스네이크 케이스 - 모드 소문자 표기, _로구분
python_class_name
파이썬 공식 문서에서는 스네이크 케이스로 작성하는 것을 권장

2. 저장할 데이터의 의미를 담아 짓기
의미 없는 문자나 과도하게 줄임말 사용시 코드 이해 힘들고 가독성 떨어짐
ex) student_name -> stne 무슨 의미인지 모름 
teacher_name = "yon"
student_name = "sei"
이런한 규칙들을 코딩 컨벤션이라고 하는데, 지키면 클린 코드 및 품질을 향상 시킬 수 있음

"""