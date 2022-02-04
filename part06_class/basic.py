# 우선 형태를 살펴보자

class Class_name:               # class : 클래스 선언 / 클래스 명
    def __init__(self):         # __init__ : 생성자/ self : 클래스 객체
        pass                    # pass : 클래스가 호출될 때 반드시 실행되는 부분
    def my_function(self):      # 메서드 / 메서드 이름 / self : 클래스 객체
        pass                    # 위 메서드가 호출될 때 수행될 부분

# 생성자

# 클래스의 속성에 해당하는 부분
# 클래스명은 주어 역할을 하기 때문에 반드시 대문자로 시작된다.

# __init__ 라는 생성자 : 클래스 선언 후 호출했을 때 반드시 실행되는 부분
# 생성자는 우리가 따로 생성자를 선언하지 않아도, 기본적으로 실행되는 부분
# 그러므로 이러한 생성자를 이용해서 자동으로 실행되게 한다.

class Class_name:
    def __init__(self):     # 생성자는 습관적으로 정의를 하자
        print("class_name이라는 클래스를 호출했습니다.")
    def my_function(self):
        self

obj = Class_name()      # 클래스를 호출만 해도 자동으로 반드시!!! 생성자 부분은 실행이 된다

# 또한 매개변수를 받을 때 매개변수를 저장하는 용도로 생성자가 쓰인다.

class Class_name:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print(f"{a}는 a {b}는 b")
    def my_function(self):
        pass

obj = Class_name(1,2)       # 클래스로 생성하여 클래스를 호출만 해도 바로 생성자 실행
print(obj.a)
print(obj.b)


# 메서드

# 클래스의 기능에 해당하는 부분
# 클래스를 호출하고 만든 객체를 수행할 함수들을 선언

class Cal:
    def __init__(self):
        pass
    def add(self,a,b):
        return a+b
    def sub(self, a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b
obj = Cal()             # 클래스 선언 및 호출
result = obj.sub(5,1)   # 클래스의 메서드 호출 및 저장
print(result)

# self
# 우리가 생성한 객체, 즉 obj의 주소값
# 생성자에서 self.a = a는 그 생성자가 매개변수로 받은 값을 만들어진 객체에 저장
# 만들어진 객체에서 독립적으로 매개변수 a를 다루겠다는 의미

class Sample:
    def __init__(self,a):
        self.a = a          # 매개변수로 받은 a를 생성한 객체의 self.a변수에 저장
    def sample_method(self):
        print(self)         # 객체의 주소값 확인
        print(self.a)       # 객체가 가지고 있는 a
obj1 = Sample(10)
obj2 = Sample(10)
obj1.sample_method()        # 메서드는 자동으로 실행되지 않으므로 생성된 객체. 메서드로 접근하여 사용
obj2.sample_method()

# 클래스 한 개로 다양한 독립적인 객체들을 관리할 수 있다.
# concept.py에서 본 것처럼 5개의 독립적인 계산기를 만들기 위해 똑같은 코드를 여러 개 만들 필요가 없다.


class Cal:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
    def div(self):
        return self.a / self.b