# # review 삼항연산자
# # A if 조건식 else B --> 조건식 참이면 A, 조건식 거짓이면 B
#
# # if 문 형태
#
# # 01
# # if 조건식 :
# #   조건식이 true일 때 실행
#
# # 예시
# if True:
#     print('안녕하세요!')
#
# if False:
#     print('안녕하세요')
#
# # 연습
# a = 10
# b = 5
# if a>b:
#     print('{}는 {}보다 큽니다'.format(a,b))
#
# # 02 if - else
# # if 조건식:
# #     조건식이 true이면 실행
# # else:
# #     조건식이 false이면 실행
#
# # 예시
# access = input('접근하시겠습니까? (y/n) : ')
# if access == 'y':
#     print('접속하셨습니다.')
# else:
#     print('종료하겠습니다.')

# 연습

# a = 10
# b = 10
# if a>b:
#     print(f'{a}는 {b}보다 큽니다.')
# else:
#     print(f'{a}는 {b}보다 크지 않습니다.')

# 기본예제

# age = int(input('몇 살입니까?'))
# if age >= 20:
#     print('성인입니다.')
# else:
#     print('미성년자입니다.')


# 03 if - elif - else

# if 조건식1:
#     조건식1이 true일때 실행
# elif 조건식2:
#     조건식2이 true 일 때 실행
# elif 조건식3:
#     조건식3이 true 일 때 실행
# else:
#     위의 모든 조건식이 false일 때 실행 (생략가능)

# 연습
# access = input('접근하시겠습니까?(y/n)')
# if access == 'y':
#     print('접속하겠습니다.')
# elif access == 'n':
#     print('종료하겠습니다.')
# else:
#     print('제대로 입력해주세요.')

# 예제

# height = int(input('당신의 키 : '))
# weight = int(input('당신의 몸무게 : '))
#
# temp = (height - 100) / weight
#
# if status < 0.5:
#     print('고도비만')
# elif status <= 0.6:
#     print('비만')
# elif status <= 0.8:
#     print('정상')
# else:
#     print('마름')
#
# # 응용예제 3
#
# 정수1 입력
# 정수2 입력
# 정수3 입력
# 가장 큰 수 출력

a = int(input('정수1을 입력하세요 : '))
b = int(input('정수2를 입력하세요 : '))
c = int(input('정수3을 입력하세요 : '))

if a>b and a>c:
    print(f'{a}가 가장 큰 수 입니다.')
elif b>c and b>a:
    print(f'{b}가 가장 큰 수 입니다.')
else:
    print(f'{c}가 가장 큰 수 입니다.')
























