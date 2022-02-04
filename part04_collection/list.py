# list

# list는 [ ] 안에 요소들이 들어있는 것
# 쉽게 서랍이라고 생각하면 됨

# # 예시
# obj=[1,2,3,4]
# print(type(obj))

# 위의 예시는 길이가 4인 리스트 즉, 요소의 개수가 4
# 리스트 안에는 어떠한 종류의 요소도 들어갈 수 있다.

# # 예시
# a = "Hello"
# b = 31
# obj= ['어서오세요',121212, a,b, [3,4]]
# print(obj)
#
# # 길이는 len() 함수를 이용
# print(len(obj))

# 인덱싱 (index)
# obj= ['a','b','c']
# print(obj[0])
# print(obj[1])
# print(obj[2])
#
# # 마지막 요소 출력
# print(obj[-1])

# # for문 적용 - 인덱싱
# obj=['a','b','c','d','e']
# for i in range(len(obj)):
#     print(obj[i])
#
# # for문 적용 - 리스트 안에 있는 요소들을 순서대로 가져오는 리스트의 내재된 기능
# for i in obj:
#     print(i)

# 리스트의 추가 삭제 수정 검색

# 추가

# listData=[1,2,3,4]
# listData.append(5)     # 뒤에서 부터 추가
# listData.append([6,7]) #리스트 자체를 요소로 넣음
# print(listData)

# listData.extend([6,7])
# print(listData)
#
# a = [1,2,3,4]
# b = [5,6,7,8]
# a.extend(b)
# print(a)


# list=[1,2,3,4,5]
# list.insert(3,100)      #insert(원하는 위피, 값)
# print(list)
#

# # 삭제 01
# listData=[1,2,3,4,3]
# listData.remove(3)  # 앞에서 부터 순서대로 찾아서 가장 먼저 보이는 것을 삭제
# print(listData)

# 삭제 02
# listData=[1,2,3,4,3]
# del listData[-1]
# print(listData)

# # 삭제 03
# listData = [1,2,3,4]
# a=listData.pop()         # 가장 많이 쓰임
# print(a,listData)       # 끝에 있는 요소를 가져와서 삭제하고 싶음
# b= listData.pop(0)      # 보통은 pop() 안에 아무 것도 적지 않음
# print(b, listData)

# # 삭제 04
# listData= [1,2,3,4]
# listData.clear()
# print(listData)

# # 수정
# listData = [1,2,100,4,5]
# listData[2]=3       # 그냥 대입
# print(listData)

# # 검색
# listData=[3,1,5,2,77]
# print(listData.index(77))       # 값에 대한 인덱스 위치 알려줌

# 정리
# 추가 : append(), extend()
# 삭제 : remove(), del, pop(), clear()
# 수정 : 특정 위치에 대입
# 검색 : index()

# # 어떤 값의 유무 확인 - 자주 쓰임
# listData = [4,2,8,6]
# print(6 in listData)
# print(3 in listData)
#
# print(6 not in listData)
# print(3 not in listData)

# slicing
listData = [1,2,3,4,5,6,7,8,9,10]
print(listData[3:6])        # 인덱스, 마지막 숫자 포함 안됨
print(listData[:6])         # 시작 생략이면 시작=0
print(listData[3:])         # 끝 생략이면 끝=-1
print(listData[:])

print(listData[4:5])        #한 개의 요소를 리스트 형태로 반환

print(listData[3:6:2])      # 2칸씩 띄어서 -> for문과 같다
print(listData[::1])
print(listData[::2])
print(listData[1::2])
print(listData[::-1])       # 리스트 요소를 거꾸로 가져오기
print((listData[::-2]))

# 참고
listData.reverse()
print(listData)

# 2차원 배열 -> 더 자세히 공부~~
obj = [[1,2],[3,4]]
print(len(obj))
print(obj[0])
print(obj[0][0])
print(obj[1][0])

