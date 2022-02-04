# 상속

# 상속을 통해 속성과 기능을 일부 변경할 수 있다.

# from 위치 import 가져올 것(전부 면 :* 사용)

from Drone import Drone


# class Drone_pro(Drone):             # 상속받는 클래스를 ()안에 써준다.
#     pass                            # Drone과 같은 속성과 기능을 가짐
#
#
# my_drone= Drone_pro(4, "pink",2.1)
# my_drone.on()
# my_drone.depart(40)
# my_drone.change(-10)
# my_drone.off()

# class Drone_pro2(Drone, 다른 클래스) :         # 여러 클래스를 상속받는 다중클래스

class Drone_pro(Drone):
    def __init__(self,wing,color, weight,type):
        super().__init__(wing, color, weight)
        print("Drone_Pro 객체가 생성되었습니다.")
        self.wing = wing                # 상속을 해도 변수는 다 적어줘야 함
        self.color = color
        self.weight = weight
        self.type =type
        print(f"타입 : {self.type}")
    # 추가 - 그냥 메소드 추가하듯이 하면 됨
    def new(self):
         print("새로운 타입이 추가됨")

    # 수정 - 이름을 갖게 가지고 와서 내용을 변경하면 됨
    def off(self):
        print("시스템 종료")

my_drone = Drone_pro(1,'red',5.6,'A')
my_drone.new()
my_drone.off()
