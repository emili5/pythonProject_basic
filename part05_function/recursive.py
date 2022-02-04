# 심화 - 재귀함수(함수 안에서 함수가 재사용되는 것)

# 반복되는 규칙을 찾아 return을 활용하여 사용

# def factorial(n):
#     result = 1
#     for i in range(n,1-1,-1):
#         result *=i
#     return result
# obj = factorial(6)
# print(obj)

# # 재귀함수를 활용한 factorial
# def factorial(n):
#     if n == 1:
#         return 1
#     return n* factorial(n-1)
# obj = factorial(6)
# print(obj)
#
# # 피보나치수열
# def fibonacchi(n):
#     if n<=2:
#         return 1
#     return fibonacchi(n-1)+fibonacchi(n-2)
#
# # n까지의 합
# def sum_all(n):
#     if n == 1:
#         return 1
#     return n+sum_all(n-1)
# obj  = sum_all(10)
# print(obj)

# n부터 m까지의 합
def sum_m(n,m):
    if n == m:
        return m
    return n+sum_m(n-1,m)
obj = sum_m(7,3)
print(obj)
