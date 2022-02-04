# 연산자 : 기능을 수행하는 특수 문자

# 우선순위 : 외우지 말고 괄호를 사용하자

# 1순위
# 산술 연산자 ( 괄호() > 부호(+/-) > 제곱(**) > *,/,//,% > +,- )

# 2순위
# 관계 연산자( >, <, >=, <=, ==, !=) # True, False

# 3순위
# 논리 연산자(and or not)  #True, False

# 4순위
# 대입 연산자( = )는 무조건 마지막에 실행!

# string + ->문자열은 더하거나 곱할 수 있다.
name = '안정민'
print(name *3)
print('제 이름은'+name)


# 산술 연산자 실습

# obj= 7//2
# print(obj)
# obj2= 7/2
# print(obj2)

# 관계 연산자 실습


# 대입 연산자

# 중요 : 복합 대입 연산자
temp = 10
temp += 5
print(temp)

temp -=5
temp *=2
temp /=4

print(temp)

# 논리 연산자
a=10
b=20
print(a>b and a==10)
print(not a>b and b==20)


# 중요
print(not 0)
print(not 1)
print([]) # False
print(not [])  # True
print(not '')
print(not '123') #False