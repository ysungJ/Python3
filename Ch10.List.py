#10장 리스트
"""
리스트 여러 개의 데이터를 묶어 하나의 변수에 저장한 것 

리스트는 원하는 자료형을 모두 저장할 수 있다. 
하나의 리스트안에 여러 자료형 저장 가능

빈 리스트 만들기 -> list()사용
ex) value = list()
ps
리스트와 배열은 비슷하지만 다른 개념임
배열은 메모리상 데이터가 연속적으로 저장, 그냥 일반적인 자료구조
리스트는 메모리 상에 데이터가 비연속적으로 저장, ADT
"""
Val = [10,5,6,8,9,9]
print(Val[0])
print(Val[4])
print(Val[-1]) #문자인덱스처럼 음수로도 가능

ex = [1,"Python",2.6]
print(ex[-3])
print(ex[1])
print(ex[-1])

#for문과 list
"""
for  변수 in 리스트:
    실행문1

for 인덱스 in range(len(리스트)):
    print(리스트[인덱스])
"""
a = [11,25,1,3,6]

for i in a:
    print(i)

for x in range(len(a)):
    print("인덱스",x,"값 :",a[x])

for x in range(len(a)):
    a[x] = 'b'
print(a)

#리스트 슬라이싱
#변수명[시작번호:끝번호+1]

s = [1,2,3,4,5,6,7,8,9,10]
print(s)
print(s[0:5])
print(s[5:10])
print(s[:5])
print(s[-5:])

#리스트 응용 함수
"""
1.리스트에 데이터 삽입 하는 append()
리스트.append(데이터)

리스트에 추가하고 싶을 때 사용, 데이터를 리스트 맨 뒤에 추가

2. 리스트의 원하는 인덱스에 데이터 삽입하는 insert()
리스트.insert(값을 추가할 인덱스, 데이터)
insert는 원하는 위치에 데이터 추가 가능 

3. 인덱스로 데이터 삭제하기 del()
del 리스트[삭제할 값의 인덱스]
del은 예약어, 리스트 앞에 적음 
지정한 인덱스에 해당하는 값을 삭제 가능, 범위를 지정하여 여러 값 삭제도 가능 

4. 원하는 값 찾아 삭제하는 remove()
리스트.remove(삭제할 값)
remove는 특정 값을 찾아 삭제 가능

5. 리스트 정렬하는 sort()
리스트.sort()
sort는 리스트 안의 데이터를 오름차순 (작은 값 부터 큰 값)로 정렬

6.리스트의 인덱스를 거꾸로 하는 reverse()
리스트.reverse()
reverse는 리스트 안의 데이터 순서를 거꾸로 바꿈 
"""
#append 사용
b = []
b.append(0)
print(b)
b.append(2)
print(b)

#insert 사용 
c = [1,2,3,4,5]
print(c)
c.insert(3,6) # c의 인덱스 3번쩨에 6을 삽입
print(c)

#del 사용
d = [1,3,5,7,9]
del d[1] #인덱스 값 1를 삭제 즉 데이터 3를 삭제
print(d)

#연습문제 del 활용 
avengers = ["아이언맨","토르","슈퍼맨","배트맨","캡틴","헐크","블랙위도우"]
del avengers[2:4]
print(avengers)

#remove 활용 
e = [1,5,9,3,4,7]
e.remove(9)
print(e)

#sort 활용
f = [5,-1,6,7,-7,2]
f.sort()
print(f)

#reverse 활용 
g = [-1,6,-6,8,7,3,5]
g.reverse()
print(g)

 #2차원 리스트

arr_2div = [["2","차","원"],["리","스","트"]]
for arr in arr_2div:
    print(arr)

#중첩
for arr in arr_2div:
    for w in arr:
        print(w,end = ' ')
    print()

#문제 
arr_2d = [[10,20,30],[40,50,60],[70,80,90]]
for i in range(3):
    print(arr_2d[i][0:2], end = ',')