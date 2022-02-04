# 삼항 연산자
# 항이 3개 필요한 연산자

# 일항 연산자, 이항 연산자

# A if 조건 else B
# 조건이 참이면 A 틀리면 B

# temp = '안녕하세요' if 1 else '안녕히가세요'
# print(temp)
#
# age_형 = int(input("형의 나이를 입력하시오"))    # 정수로 캐스팅
# age_동생 = int(input("동생이 나이를 입력하시오"))
# temp =  '형' if age_형 > age_동생 else '동생'
# print(temp)

# 예제
height =150
weight = 60

temp= (height-100)/weight
result='고도비만' if temp <0.5  else '비만' if temp<=0.6 else '정상' if temp<=0.8 else '마름'
print(result)