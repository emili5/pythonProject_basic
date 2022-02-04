# %연산자 : 따옴표 안으로 ooo을 가지고 올 수 있다.

# %d : decimal(정수)
# %f : float(실수)
# %c : character(문자)
# %s : string(문자열)

height= 130
print('그 사람의 키는 %dcm이다' %height)

국어 = 80.5
수학 = 98
print('국어 점수는 %.1f점 \n수학 점수는 %d점이다.\n평균은 %.2f이다' %(국어, 수학, (국어+수학)/2)) # 변수 개수가 많으면 ()안에 ,로 구분


# 01 format

# 예제1

# msg = "환영합니다"
# name = input("이름을 적어주세요 : ")
# print("{}님\n{}".format(name,msg))

# 예제2
# 국어 = 89.5
# 수학 = 96
# mean = (국어+수학)/2
# print("국어 점수는 {}점\n수학 점수는 {}점\n평균은 {}점".format(국어,수학, mean))

# 02 format

# 예제3
국어 = 89.5
수학 = 96
평균 = (국어+수학)/2
print("국어 점수는 {lan}점\n수학 점수는 {math}점\n평균은 {mean}점".format(lan=국어,math=수학,mean=평균))
print("국어 점수는 {math}점\n수학 점수는 {lan}점\n평균은 {mean}점".format(lan=국어,math=수학,mean=평균)) # 문자 지정하면 순서 고려 안함

# 03 f-string

# 예제1
국어 = 89.5
수학 = 92
평균 = (국어+수학)/2

print(f'국어 점수는 {국어}점\n수학 점수는 {수학}점\n평균은 {평균}점')
