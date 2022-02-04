# global /local 변수

# global (전역)변수 : 현재 파이썬 전체에서 지속적으로 사용 가능한 변수
# local (지역) 변수 : 함수 내에서 사용되었다가 사라져서 함수 밖에서는 사용 불가능한 변수

# temp1 = 100         # 실행 순서01
# def add(number):    #
#     global temp1       # global 전역변수를 알여주면 함수가 전역변수를 받아들임
#     temp1 +=number  # 함수가 저장될 떄 전역변수인 temp1에 무엇이 일어났느지 모른다.-> 함수 내에서변슈가 선언이 되어있지 않아 오류
#
#     return temp1
# print(add(40))

# temp1 = 0
# def calculate(num):
#     temp = 5
#     temp *=num
#     return temp

temp=0
def calculate():
    # temp+=1
    # global temp
    # temp=1
    print(temp)
calculate()

# temp1 = 0
# def calculate(num):
#     temp1 = 5
#     temp1 *=num
#     return temp1
# calculate(4)
#
# temp1 = 4
# temp2 =7
#
# def calculate(num):
#     global temp1
#     temp1+=100
#     temp1*=2
#     print(' 100을 더한 후 2를 곱해습니다.')
#     print(temp1)
#     return temp1
#
# def calculate(num):
#     global temp1        # 변수 선언이 x, global 을 써서 전역변수 정보를 가져옴
#     temp2+=50
#     temp2*=2
#     print(' 50을 더한 후 2를 곱해습니다.')
#     print(temp2)
#     return temp2