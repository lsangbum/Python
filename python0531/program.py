import sys


# def write():
#     number = input('수를 입력하세요 : ')
#     if number.isdigit() == False :
#         print('정수가 아닙니다.')
#     # elif number < 0 :
#     #     print('음수 입니다.')
#         sys.exit(0)
#     else :
#         number = int(number)
#         if number % 3 == 0 and number > 0 :
#             print('양수 3의 배수 입니다.')
#             write()
#         elif number % 3 == 0 and number < 0 :
#             print('음수 3의 배수 입니다.')
#             write()
#         else :
#             print('3의 배수가 아닙니다.')
#             write()
# write()

# def write() :
#     number = input('수를 입력하세요 : ')
#     try :
#         number = int(number)
#     except ValueError :
#         print('정수가 아닙니다.')
#         sys.exit(0)
#     if(number < 0) :
#         print('음수 입니다.')
#     else :
#         print('양수 입니다.')
#
#     if number % 3 == 0 :
#         print('3의 배수 입니다.')
#         write()
#     else :
#         print('3의 배수가 아닙니다.')
#         write()
#
# write()

# def isOdd() :
#     number = input('수를 입력하세요 ..')
#     if number.isdigit() == False :
#         print('정수가 아닙니다.')
#         sys.exit(0)
#     else :
#         number = int(number)
#         if number % 2  == 0 :
#             print(number, '는 짝수 입니다.')
#             isOdd()
#         else :
#             print(number, '는 홀수 입니다.')
#             isOdd()
# isOdd()

# number = input('수를 입력하세요.')
#
# if number.isdigit() == False :
#     print('정수가 아닙니다.')
#     sys.exit(0)
#
# number = int(number)
# for i in range(1, number + 1, ) :#range 시작수 , 마지막 수 전까지 , 증감수 없을 시 +1
#     print('*' * i)


# for i in range(1, 10) :
#     for j in range(2, 10) :
#         print(j, '*', i, '=', i * j, end = '\t')
#     print()
# from random import *
#
# list = []
# for i in range(0, 10) :
#     list.append(randint(1, 100))
#
# cnt = 0
# sum = 0
#
# for i in list :
#     print(i, end = '\t')
#     if i % 3 == 0 :
#         cnt += 1
#         sum += i
#
# print()
# print('주어진 리스트에서 3의 배수의 개수 =>', cnt)
# print('주어진 리스트에서 3의 배수의 합 =>', sum)

# t = 10, 20, 30, 'python'
# a, b, c, d = t
# print(a, b, c, d)


t = (1, 2, 3)
s = set(t)
print(s, type(s))

l = list(s)
print(l, type(l))

t = tuple(l)
print(t, type(t))












