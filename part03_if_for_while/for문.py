# for 문 (반복문)
#  기본틀

# for i in range(시작, 끝, 얼만큼씩): # 끝은 i에 포함되지 않는다
#     i 와 관련된 실행문

# for i in range(1,10,1):
#     print(i)
#
# for i in range(2, 20, 3):
#     print(i)

# 연습1
#
# sum = 0
#
# for i in range(1,11,1):
#     sum += i
#
# print(sum)
#
# 연습2
#
# sum = 0
#
# for i in range(1,20):
#     if i % 2 == 1:
#         sum += i
#
# print(sum)

# for i in range(시작 , 끝) # 얼만큼씩을 생략하면 default 값인 1로 실행된다.

# for i in range (1,10):
#     print(i)

# for i in range(10):
#     print(i) # 0으로 시작 1씩 늘림.

# 연습

# for i in range(10, 0, -1):
#     print(i)

# for i in range(10):
#     print(10-i)

# 피보나치 수열

# obj1 = 1
# obj2 = 1
# result = 1
#
# for _ in range (10):
#     result = (obj1 + obj2)
#     obj1 = obj2
#     obj2 = result
#     print(result)

# 구구단 - 이중 for문

# for i in range(2,10):
#     print('----------------')
#     print(f'{i}단 시작입니다.')
#     print('----------------')
#     for j in range(1,10):
#         print(f'{i}*{j} = {i*j}')

# break : 현재 수행 중인 루프 전체 종료
# continue : 현재 돌고 있는 루프 1회를 바로 마친다. 밑에 있는 코드를 수행하지 않는다.

# for i in range(10):
#     if i == 5:
#         break
#         print(i)    #if문에 속해 있는 코드
#
#
# for i in range(10):
#     if i == 5:
#         break
#     print(i)    #for문에 속해 있는 코드
#

# 예시- 구구단에서 o*5까지만 출력
# for i in range(2,10):
#     for j in range(1,10):
#         print(f"{i}x{j}={i*j}") #출력 후 나와야 함
#         if j==5:
#             break


# 예시 - 구구단에서 o*5만 제외하고 출력
# for i in range(2,10):
#     for j in range(1,10):
#         if j==5:
#             continue
#         print(f"{i}x{j}={i*j}") #본인이 속한 루프의 아래에 있는 모든 조건 다 생략

# 연습 -*
for i in range(5):
    print("*"*(i+1))

for i in range(5):
    print("*"*(5-i))

for i in range(5):
    print(' '*(5-i)+'*'*(i+1))