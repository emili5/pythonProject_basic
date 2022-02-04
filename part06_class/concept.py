# 객체 :

# Class는 붕어빵을 만드는 틀
# 객체는 붕어빵

# 우리가 앞서 배운 함수 review
# 함수 : 어떠한 기능, 즉 무언가를 수행하기 위한 것을 말함

# 객체에는 속성과 기능이 있다.

# 가장 간단한 클래스를 먼저 살펴보자 - 클래스는 반드시 대문자로 시작

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # 더하기
    def add(self):
        return self.a + self.b

my_cal  = Calculator(5,10)
result = my_cal.add()
print(result)

# 단순 더하기 기능을 수행하는 함수와 비교했을 때 복잡한 프로그램을 만드는데 굉장히 유용하기 때문에 학습이 필요



