#14장 클래스와 객체
"""
클래스를 잘 사용하면 코드의 중복을 줄일 수 있고, 전역변수를 무한정 만들 수 없다.
클래스의 기본틀을 만들어 놓으면, 원할 떄 마다 객체를 생성할 수 있음.
객체마다 고유한 속성을 주고 활용 가능 

class 클래스명:
    클래스에 들어갈 코드

객체명 = 클래스명()

클래스 안에는 클래스에서만 쓰이는 변수를 선언 가능 
객체로 클래스 안에 있는 변수나 함수에 접근 할 때에는 객체명.변수명
객체명.함수명()라고 적음
"""
#와플로 통한 클래스 예시
class Waffle:
    name = "waffle"

choco = Waffle()
print(choco.name)

banana = Waffle()
print(banana.name)

#이렇게 클래스 안에 변수를 직접 선언하면, 변수가 모든 객체에 동일하게 적용됨으로 추천하지않는 방식임
#클래스의 변수가 변경할 때, 모든 객체의 변수가 바뀌는 코드
Waffle.name = "choco waffle"
print(choco.name)
print(banana.name)

#클래스와 메소드 
"""
클래스 안에서 직접 변수를 사용하는 대신 함수를 사용하면 객체들이 서로 다른 속성을 가지게 만들 수 있음 
이러한 클래스 내부의 함수를 메소드라고 함.
"""

class Waffle:
    def setName(self,n):
        self.name = n


choco = Waffle()
choco.setName("Choco Waffle")
print(choco.name)

banana = Waffle()
banana.setName("banana Waffle")
print(banana.name)

#클래스 안에 변수를 직접 선언하는게 아니라 메소드를 이용해 각 객체에 변수를 선언하면
#객체별로 독립적인 속성을 나타낼 수 있음. 

#Avatar클래스로 통해 알아보자
class Avatar:
    def setAvatar(self,height,skill):
        self.height = height
        self.skill = skill

#클래스 안에는 메소드를 자유롭게 선언할 수 있다.
    def printAvatar(self):
        print("키는",self.height,"cm","스킬은",self.skill,"입니다.")

Yonsei = Avatar()
Yonsei.setAvatar(140,"점프")

print(Yonsei.height)
print(Yonsei.skill)
Yonsei.printAvatar()

#클래스와 생성자
"""
생성자는 한 클래스의 객체들을 생성할 때, 일정한 속성을 적용하기 위해 존재하는 것 
객체가 생성될 때 자동으로 호출되는 메소드 
메소드 이름으로 __init__입력하면 파이썬은 생성자임을 자동으로 인식함 
"""
class Avatar2:
#   def setAvatar2(self,name,hp):
    def __init__(self,name,hp): #생성자 입력 
        self.name = name
        self.hp = hp
    
    def increaseHp(self):
        self.hp = self.hp + 10
    
    def decreaseHp(self):
        self.hp = self.hp -10
    
    def printHp(self):
        print("현재",self.name,"의 hp는",self.hp,"입니다.")
    
Yose = Avatar2("yose",0)
Yose.printHp()
