# 변수
# 변수는 저장 공간이다.

#변수 파일입니다.

# a = 10
# print(a)
# print('a', a)  # print 안에 , 는 띄어 쓰기를 의미
# print('a는', a, '이다')
#
# name = input('이름을 입력하세요 : ')
# print('내 이름은', name, '입니다')
#
#
# phone_number = input('전화번호를 입력하세요 : ')
# print("내 전화번호는", phone_number, "입니다")
#
# sampleData = 1+2+3+4+5+6+7+8+9+10
# print(sampleData)

# 주의점
# 변수 명에는 공백이 있으면 안된다. 특수 문자 사용이 불가 하다 (_만 사용 가능)

a,b=10,5 # 개수가 적을 때 이렇게 변수 선언할 수 있음
print(a,b)

# a와 b를 바꾸고 싶을 때
# 정석
# temp = a
# a = b
# b = temp
# print(a,b)

# 파이썬 방법
a, b = b, a  # 동시 선언

print('a는', a, 'b는', b) # ,를 쓰지 않고 +를 써서 나타낼 수도 있음
print('a는 '+str(a)+'b는 '+b)

name = 'Alice'
print("")
