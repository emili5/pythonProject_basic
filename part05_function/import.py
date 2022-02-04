# from 파이썬 파일 import 경로 함수

# my_file에 있는 함수를 불러와보자
# from my_file import my_function
#
# my_function()

# from my_file import my_function,my_function2
# my_function()
# result = my_function2(3,4)
# print(result)

from my_file import *
my_function()

result=my_function2(3,4)
my_function3('안정민')
print(result)

# 경로 활용
from sample.hide.my_file2 import sample
sample()

