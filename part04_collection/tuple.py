# 튜플

# 튜플은 () 안에 요소가 들어있는 형태
# 튜플은 list와 다르게 immutable, 즉 변하지 않는 collection

# # 예시
# obj = (1,2,3)
# print(type(obj))
#
# # print(obj[1])     # 튜플은 수정과 추가가 불가
# # obj[1]=6
#
# obj=1,2,3
# print(obj)
#
# # 소괄호 생략가능, ','를 남겨놔도 상관없다
# obj1=1,2,
# print(obj1)
#
# obj2=1,
# print(type(obj2))

# 리스트와 인덱싱 동일
obj = 1,2,3
print(obj[1])

# 리스트와 슬라이싱도 동일
obj = 1,2,3,4,5,6,7,8,9
print(obj[3:6])