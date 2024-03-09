#12장 집합
"""
집합 - 다른 자료형들과 달리 중복 허용 X, 순서 없음
리스트, 튜플처럼 인덱스를 이용해 접근 불가 

set을 이용하거나 중괄호를 이용해 만들 수 있음 
중괄호 사용시, 데이터를 1개 이상 넣어야함 
-> 안하면 딕셔너리 자료형으로 인식됨 

"""

#set
a = set([5,2,3,2,1,4])
b = set("apple")
c = {3,6,4,7,1,7}
print(a,type(a))
print(b,type(b))
print(c,type(c))

#중복을 허용하지 않기 때문에 중복 값을 제거하려고 할 때 사용
#리스트나 튜플 값을 잡합으로 만들어 중복된 값이 있는지 확인할 수 있음
#집합으로 중복값 제거한 후, 다시 튜플이나 리스트로 만들어서 사용할 수 있음

#합집합, 교집합, 차집합
"""
1.합집합 | 또는 union()
합집합은 지집합의 모든 요소를 포함하되, 중복 값은 단 1번만 구함.
파이프 | 기호를 사용하거나 union()함수를 이용하여 구할 수 있음

2. 교집합 & 또는 intersection()
두 집합에서 중복되는 요소만 구함 
앰퍼샌드 & 사용하거나 intersection()함수를 사용

3.차집합 - 또는 difference()
다른 집합과 중복되지 않는 요소만 구함
빼기 - 기호를 사용하거나 difference()를 사용
"""
#합집합
a = set([1,2,3])
b= set([2,3,4])
print(a|b)
print(a.union(b))
print(b.union(a))

#교집합 
print(a&b)
print(a.intersection(b))
print(b.intersection(a))

#차집합
print(a-b)
print(a.difference(b))
print(b.difference(a))

#집합 유용 함수 
"""
집합은 값을 추가하거나 제거 가능 

1. 데이터 추가 add()
집합.add(데이터)
집합에 데이터 추가, 동일한 데이터가 이미 존재하면 변화 x
-> 집합은 자동으로 중복 제거 

2. 데이터 여러 개 추가 update()
집합.update(데이터)
중복 데이터는 추가 x, 여러 개의 데이터를 한번에 추가할 때 사용 

3.원하는 값 찾아 삭제하기 remove()
집합.remove(데이터)
리스트처럼 특정한 값을 삭제 가능
단 집합에 없는 요소를 삭제할시 오류 발생
"""

#집합 add 
a = set([1,2,3])
a.add(-1)
a.add(2) # 중복값으로 반영 안됨 
print(a)

#집합 update
a = set([3,4,5])
a.update(3,5,7,8) #중복값인 3,5는 반영 x
print(a)

#집합 remove
a = set([3,4,5,7])
a.remove(3)
print(a)