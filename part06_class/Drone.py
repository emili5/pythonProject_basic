# 드론 클래스

class Drone:
    def __init__(self,wing,color, weight):
        print('생성자가 호출되어 객체가 초기화되었습니다.')

        print("드론 소개")
        self.wing = wing
        self.color = color
        self.weight = weight

        print(f"날개 : {self.wing}\n색 : {self.color}\n무게: {self.weight}\n")
    def on(self):
        print("시작")
        print()
    def off(self):
        print("종료합니다.")
    def depart(self,velocity):
        self.velocity= velocity
        print("출발~~")
        print()
    def change(self,plus):
        self.velocity+=plus

if __name__=='main':
    pass
