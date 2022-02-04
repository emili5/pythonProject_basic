# dictionary / dict (사전)
# 형태
# dictData = {key : Value}

# 예시
obj = {'apple' : '사과','banana': '바나나', 1: [1,2,3,4], 5 : [510,15,20]}
print(obj)

print(obj['apple'])
print(obj[1])

학생1 = {'name': '안정민', 'age': 123, 'hobby':'play'}

#  추가
dictData = {'apple': '사과 수확량', 'grape': '수박 수확량', 'watermelon': '수박 수확량'}
dictData['peach'] ='복숭아 수확량'
print(dictData)

# 수정
dictData['grape'] ='포도 수확량'
print(dictData)

# 삭제
del dictData['grape']
print(dictData)

# 검색 (위치가 아니라 존재유무 확인
print('watermelon' in dictData)
print(dictData['watermelon'])
print(obj[1])

# key 분리
dic_keys = dictData.keys()      # 리스트의 요소둘이 키로 변환되어 딕셔셔리 반환
print(dic_keys)
print(type(dic_keys))

# value 분리
dic_values = (list)(dictData.values())      # 값을 리스트 형태로 저장
print(dic_values)