#가위 바위 보 게임
"""
컴퓨터와 Rock Scissors Paper하기

조건
1. 랜덤 라이브러리 사용
2. 가위,바위,보 중 하나 입력하면 게임 진행
3. 함수 2개 이상 사용
4. 게임 결과 - win draw lose로 출력 
"""
import random #조건 1 랜덤 라이브러리 사용

def rsp_num(rsp):
    if rsp == "가위":
        return 1
    elif rsp == "바위":
        return 2
    elif rsp == "보" :
        return 3
    else : 
        print("가위,바위,보 중에서 하나 입력 하십쇼")
        return None

def rsp_result(a,b):
    if a is None or b is None :
        return "입력 오류"
    
    gap = a - b 
    if gap == 0 : 
        txt = "draw"
    elif gap in[-2,1]:
        txt = "you're win"
    else:
        txt = "you're lose"
    return txt

rsp_list = ["가위","바위","보"]

print("가위바위보 시작")
you = input("뭐 낼꺼야 ? : ")
com = random.choice(rsp_list)

print(f"\n당신 :  {you}")
print(f"컴퓨터 : {com}\n")

y= rsp_num(you)
c= rsp_num(com)
result = rsp_result(y,c)

print("결과 : ", result)