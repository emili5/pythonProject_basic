# method와 함수의 차이점

# 메서드 : 어떠한 객체 내부에서 기능을 수행하는 함수

# 예시
# temp= []
# temp.append(4)       # 객체.메서드()
# print(temp)

# 함수: 어떠한 객체와 상관없이 독립적으로 기능을 수행하는 것

# 예시
# print("")
# input("키를 입력하세요:")
# int('123')

# 함수의 정의
def add(num1,num2):     # def : 정의 / add: 함수명 / num1,num2 : 매개변수(입력값)
    sum = num1+num2     # 실행부
    return sum          # return : 반환하라 /sum : 반환값

# 예시
def add(a,b):
    result = a+b
    return result

obj = add(5,10)
print(obj)

temp1=5
temp2=10
obj= add(temp1,temp2)

a=9
b=10
print(add(a,b))

# 함수의 종류
# 입력 o,반환값 o
# 입력 x,반환값 o
# 입력 o,반환값 x
# 입력 x,반환값 x

# 예시-입력 x, 반환값 o
def do_something():
    return 5
a = do_something()      # a에 5 저장
print(a)

# 예시- 입력 o, 반환값 x
#  대표 예시- print()
a = print("Hello")
print(a)        # None

def do_something(a,b):
    print(f"{a}와 {b}를 입력받았습니다.")

obj1 = [1,2,3,4]
obj2 = '안녕하세요'
maybe=do_something(obj1,obj2)
print(maybe)

#  입력 x, 반환값 x
def do_something():
    print("파이썬 실행")

do_something()