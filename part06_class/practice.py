# 피자 클래스

# 재료(리스트), 모양, 브랜드를 각각 입력받아서 속성값으로 부여하고

# 기능으로는 1)info, 2)만들어지는 과정, 3) 재료 추가 4) 재료 삭제
import math


class Pizza:
    def __init__(self,재료,모양,브랜드):
        self.재료 =재료
        self.모양= 모양
        self.브랜드 = 브랜드

    def info(self):
        print(f"재료에는 {self.재료}가 있습니다.")
        for i in self.재료:
            print(i)
        print(f"모양은 {self.모양}입니다.")
        print(f"{self.브랜드}에서 출시했습니다.")
    def make(self):
        print(f"{self.재료}로 {self.모양}을 가진 {self.브랜드}피자를 만듭니다.")
    def add(self,추가재료):
        self.재료.append(추가재료)
        print()
    def remove(self):
        pass

# 연습02

class Shape:
    def __init__(self,n,l):
        self.n = n
        self.l = l
    def length(self):
        print(f"둘레의 길이는 {self.n*self.l}입니다.")
        return self.n*self.l
    def area(self):
        print(f"넓이는 {self.l**2/4*(1/math.tan(math.pi/self.n))}입니다.")
        return self.l**2/4*(1/math.tan(math.pi/self.n))

    def across(self,n):
        print(f"정{self.n}각형의 대각선의 개수는 {self.n*((self.n)-3)/2} 이다.")
        return self.n*((self.n)-3)/2
shape1 = Shape(4,10)
print(shape1.length())
print(shape1.area())

# 대각선의 개수를 구하는 메소드 추가

shape2=Shape(6.7,100)
shape2.length()
shape2.area()
shape2.across()

# 연습 03

import random



class My_game:
    def __init__(self,name,score=0):
        self.name = name
        self.score = score
    def number_game(self):
        cnt=1
        val = random.randrange(1,100+1)

        while True:
            num=int(input("1에서 100중 숫자를 입력해주세요>"))
            if num>=1 and num<=100:
                if val == num:
                    break
                elif val > num:
                    print("더 작은 값을 입력하였습니다.")
                else:
                    print("더 큰 값을 입력하였습니다.")
            else:
                print("범위를 다시 확인해주세요!")        # 진짜 중요: 예외상황을 항상 염두해두어야 한다!!
            cnt+=1
        print(f"{self.name}님 {cnt}번 만에 성공하셨습니다!최종 점수는 {self.score}입니다.")
        self.score+=5-cnt

    def time_game(self):
        # 최대한 5초에 가깝게 시간 맞추기
        import time
        print("지금 시간이 시작되어습니다.")
        start = time.time()
        input("입력해주세요 : ")
        stop = time.time()
        print(stop-start)



gamer = My_game("안정민")
gamer.game()