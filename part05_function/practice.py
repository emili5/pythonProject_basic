# 참고
import random

def random_int(num):
    rand_int=[]
    for _ in range(num):                 # num회 반복하는 반복문
        temp =random.randrange(1, 10)    # temp에 1부터 10사이 랜덤변수 저장
        rand_int.append(temp)            # rand_int 리스트에 temp추가
    return rand_int                      # 함수가 종료되면서 rand_int 반환
num=10
arr = random_int(num)
print(arr)

# 연습01 - 원하는 단의 구구단 출력하는 함수
def gugudan(num):
    for i in range(1,9+1):
            print(f"{num}x{i}={num*i}")
    return
gugudan(5)

# 연습 02- 원의 넓이 구하는 함수
def get_area(r):
    return r**2*3.14
area=get_area(4)        # 리턴값을 사용하려면 반드시 값에 저장 후 출력
print(area)

import math
print(math.pi)

def get_area(r):
    return r**2*math.pi
area=get_area(10)
print(area)

# 연습 03 -' '-'없이 전화번호를 받았을 때 '-'를 서 반환해주는 함수

# 슬라이싱 사용
def change(phone_number):
    return phone_number[:3]+'-'+phone_number[3:7]+'-'+phone_number[7:]
ch = change('01012345678')
print(ch)

# 리스트와 for문 사용
def change1(phone_number):
    arr = []                                 # 문자열 -> 리스트
    for i in range(len(phone_number)):      # 문자열의 각 문자의 인덱스에 접근
        if i==3 or i==7:
            arr.append('-')
        arr.append(phone_number[i])
    result = ''                             # 리스트 -> 문자열
    for i in arr:
        result+=i
    return result
ch = change1('01012345678')
print(ch)

# 연습04 - 임의의 숫자 구간을 받아서 합산을 구하는 함수 만들기
def add(a,b):
    sum=0
    for i in range(a,b+1):
        sum+=i
    return sum
result= add(1,10)
print(result)

# 연습 05 - 삼각형 밑변과 높이 입력받아서 넓이를 구하는 함수
# def get_area(a,b):
#     area=a*b/2
#     return area
#
# a=int(input('밑면: '))
# b=int(input('높이: '))
# result=get_area(a,b)
# print(result)

# 연습 06 - 문자열을 받아서 한 글자씩 리스트에 넣어서 리스트 반환
def turnT0List(a):
    arr=[]
    for i in range(len(a)):         #   for i in a:
        arr.append(a[i])            #       arr.append(i)
    return arr
result=turnT0List('Hello')
print(result)

# 연습 07 - 문자열을 받아서 문자열을 거꾸로 출력하는 함수
def String_reverse(a):
    b=''
    for i in range(-1,-len(a)-1,-1):
        b+=a[i]
    return b
result=String_reverse('Hello')
print(result)

# 다른 간단한 방법
def reverse(a):
    return a[::-1]