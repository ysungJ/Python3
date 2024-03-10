#13장 딕셔너리
"""
딕셔너리는 key와 value 값을 가짐 
ex) apple -> 사과, banana -> 바나나 
a = {"키":"벨류"}

리스트, 튜플은 숫자로 된 인덱스로 데이터를 찾음 
딕셔너리는 인덱스가 아니라 key를 이용함 
key와 value는 콜론을 사이에 두고 사용

<주의>
key와 value에 넣을 수 있는 자료형이 다름 
value에는 리스트,튜플,딕셔너리등 어떤 자료형도 가능
key는 그보다 제한적 (변하지 않는 값인 숫자(정수,실수), 문자열, 튜플) 가능
key에서 많이 사용하는건 숫자와 문자열

"""

#간단한 딕셔너리 생성
dic = {"python":"파이썬","CPP":"C++언어","JAVA":"자바"}
#출력
print(dic["python"])
print(dic["CPP"])
print(dic["JAVA"])

# key에 문자열 사용
dic = {"int":1,"str":"문자","list":[1,2],"dict":{"Python":"파이썬"}}
print(dic["int"])
print(dic["str"])
print(dic["list"])
print(dic["dict"])


#딕셔너리 수정 
"""
딕셔너리는 리스트처럼 값을 추가, 삭제 수정 가능
단, key와 value를 쌍으로 추가하거나 삭제해야함, 
key는 수정 불가, value는 수정 가능 

1.한 쌍만 추가
딕셔너리명[key값] = value 값

2. 여러 쌍 추가 update()
딕셔너리명.update({키값1:벨루값1,키값2:벨류값2......})

3. 쌍 삭제하기 del 
del 딕셔너리명[키값]
삭제할 때는 예약어 del 사용 
단 key값으로 접근해서삭제해야함 

4. value 값 수정
딕셔너리명[key 값] = 새로운 value 값 
key값에 접근해 value값ㅇ르 수정 
"""

#한 쌍만 추가하기 
dic = {"a":"apple","b":"banana","c":"cold"}
dic["d"] = "dictionary"
print(dic)

#여러 쌍 추가
dic.update({"c":"cool","d":"dia","e":"elevator"}) 
#update에 동일한 key가 존재하면, 해당 key와 쌍을 이루는 value값이 update한 값으로 바낌
print(dic)

#삭제하기
del dic["a"]
print (dic)

#수정하기
dic["b"] ="benel"
print(dic)

#for문과 딕셔너리
"""
1. 딕셔너리의 키 값 반복
딕셔너리명.keys()
key값을 반환하는 keys()함수 사용가능 
keys()함수 사용시 리스트가 반환됨

2. 딕셔너리의 벨류 값 반복
value 값을 반환하는 values()함수를 사용 가능
value값 또한 리트로 반환 됨

3. 딕셔너리의 키, 벨류 쌍으로 반복 
딕셔너리명.items()
키와 벨류 값을 한꺼번에 반환하는 items()함수 
key와 value를 동시에 받을 수 있음 

"""

#키값 반복
dic = {"a":"apple","b":"banana","c":"cold"}
print(dic.keys())

#for문 키 값 반복
for k in dic.keys():
    print(k,end=" ")
    print(dic[k],end=" ")

#value 값 반복
dic = {"a":"apple","b":"banana","c":"cold"}
print(dic.values())

for v in dic.values():
    print(v,end = " ")

#키와 벨류 쌍으로 반복 
dic = {"a":"apple","b":"banana","c":"cold"}
print(dic.items())

for k,v in dic.items():
    print(k,v)
    

