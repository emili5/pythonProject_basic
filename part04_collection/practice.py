# 기본
# 01. 1부터 10까지 리스트에 넣기
listData = []                     # 빈 리스트 선언
for i in range(10):
    listData.append(i+1)        # 리스트에 요소를 추가하는 함수 사용
print(listData)

# 02, 10부터 짝수만 30까지 리스트에 저장
arr = []
for i in range(10,30+1,2):
    arr.append(i)

# 03. 10부터 -10까지 거꾸로 리스트에 넣기
arr =[]
for i in range(10,-10-1,-1):
    arr.append(i)

# 04, 80점 이상 합격자 이름 리스트에 넣기
student = {'짱구': 80, '철수': 60, '훈이': 15,'맹구': 100, '유리': 75}
합격자 = []
for i in student:           # 딕셔너리의 요소 방문- 키, i에 각 요소의 키가 들어감
    if student[i]>=80:      # 딕셔너리의 키의 값에 접근 - 딕셔너리 변수[인덱스]
        합격자.append(i)

# 05 . 리스트에서 가장 큰, 작은 수 찾기
arr = [1,5,26,-6,44,2]
max1 = arr[0]
min1 = arr[0]
for i in arr:       # i에는 각 요소가 들어감
    if max1<i:
        max1=i
    if min1> i:
        min1=i
print("가장 큰 수는 ",max)
print("가장 작은 수는 ", min)

print(max(arr))
print(min(arr))

# 06. 리스트에 1~20까지 홀 수 리스트 한개 짝수 리스트 한개 따로 만들기
arr_odd=[]
arr_even=[]

for i in range(1,20+1):
    if i%2==0:
        arr_even.append(i)
    else :
        arr_odd.append(i)
print(arr_odd)
print(arr_even)

# 심화

# 06 - 리스트에 1부터 12까지 넣고 12의 공약수를 제외하고 전부 삭제하기
arr =[]
for i in range(1,12+1):
    arr.append(i)
print(arr)

# for i in arr:
#     if 12 % i !=0:
#         arr.remove(i)       #
# print(arr)

for i in range(1,12+1):
    if 12 % i!=0:
        arr.remove(i)
print(arr)

# 07- 섭씨 온도 리스트를 화씨 온도로 바꾸기
# (섭씨 *9/5) +32 = 화씨
C = [10.5, 14.7, 4, 56.9]
F = []
for i in C:
    temp=(i*9/5)+32
    F.append(temp)
print(F)

# arr= [1,2,3]
# for i in arr:
#     arr.append(i*4)
# print(arr)



# 08. 현대의 환율로 원화 리스트에서 1~5 요소는 달러, 6~10요소는 엔화. 11~15 는 유로로
won = [1000,1500, 2600, 1100, 2400, 1300, 3000,3400, 2300, 1350, 560, 1230, 2100,750, 2030]
exchange=[]
for i in range(0,15+1):     # range에 숫자가 i로 들어감
    if i<5:
        dollar=won[i]/1192.18
        exchange.append(dollar)
print(exchange)

# 09. 2~9단만 따로 리스트 안에 넣기
gugudan=[]

for i in range(2,9+1):
    gugudan.append([])      # i가 바뀔 때마다 [] 할당
    for j in range(1,9+1):
        gugudan[i-2].append(i*j)

print(gugudan)

# 한 줄 포문 - 리스트를 만들 때 유용하게 쓸 수 있음
one_line= [i for i in range(10)]
print(one_line)

# 구구단 한 줄 포문
gugudan= [[] for _ in range(8)]     # 안에 빈 리스트 만들기
print(gugudan)
for i in range(2,10):
    for j in range(1,10):
        gugudan[i-2].append(i*j)

