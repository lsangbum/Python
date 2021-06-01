# num = input("숫자 입력 : ")
# num = int(num)
#
# if num > 0:
#     print("양수 입니다.")
# elif num < 0:
#     print("음수 입니다.")
# else:
#     print("0 입니다.")




# while True:
#     print("1. 국어")
#     print("2. 영어")
#     print("3. 수학")
#     print("4. 과학")
#     print("0. 종료")
#     choice = input("과목번호를 입력하세요.>>>\n")
#     choice = int(choice)
#     if choice == 1:
#         print("[ R101호 국어강의실 입니다. ]\n")
#     elif choice == 2:
#         print("[ R202호 영어강의실 입니다. ]\n")
#     elif choice == 3:
#         print("[ R303호 수학강의실 입니다. ]\n")
#     elif choice == 4:
#         print("[ R404호 과학강의실 입니다. ]\n")
#     elif choice == 0:
#         print("[ 강의실 탐색을 종료합니다. ]\n")
#         break
#     else:
#         print("[ 상담원에게 문의하세요. ]\n")


# num = int(input("숫자를 입력하세요.>>>\n"))
# value = "Big" if num >= 5 else "small"
# print(value)

# animalList = ['cat', 'cow', 'tiger']
#
# for animal in animalList:
#     print(animal, end = '\t')

# friendList = [('둘리', 10), ('마이콜',20), ('도우넛', 30)]
#
# for i in friendList:
#     print("이름 : ", i[0], ", 나이 : ", i[1])

# for i in range(5, -6, -1):
#     print(i, end = '\t')

# num = int(input("원하는 단 수를 입력하세요.>>"))
# for i in range(num, num + 1, 1):
#     print("[ ", num, "단 ]")
#     print("+--------------------------------+")
#     for j in range(1, 10, 1):
#         print(i, "X", j, "=", (i*j))
# 원하는 단만 출력하시오.>>
# for i in range(1, 10, 1):
#     print(num, 'X', i, '=', (num * i))


# for i in range(2, 10, 1):
#     for j in range(1, 10, 1):
#         print(i, "X", j, "=", (i*j))

# fruitList = ['red', 'orange', 'yellow', 'green', 'blue']
#
# for index, color in enumerate(fruitList):
#     print(index, color)

# num = int(input("시작할 수를 입력하세요.>>>\n"))
# sum = 0
# while num < 11:
#     print(num, end = '\t')
#     sum +=num
#     num += 1
# print('\n합 : ', sum)
# num = int(input("시작할 수를 입력하세요.>>>\n"))
# while True:
#     if num % 6 == 0 and num % 14 ==0 :
#         print("6과 14의 배수 중 최소값 : ",num)
#         break
#     else:
#         num += 1


# money = int(input("금액을 적어주세요.>>\n"))
#
# if money.isdigit() == False:
#     print("정수가 아닙니다.")
#     sys.exit(0)
# else:
#     a = money / 50000
#     b = a / 10000
#     c = b / 5000
#     d = c / 1000
#     e = d / 500
#     f = e / 100
#     g = f / 50
#     h = g / 10
#     print(a, b, c, d, e, f, g, h)

# import sys
# money_list = [50000, 10000, 5000, 1000, 500, 100, 10, 5, 1]
# money = input("금액 : ")
# if money.isdigit() == False:
#     print("정수가 아닙니다.")
#     sys.exit(0)
# money = int(money)
# for i in money_list:
#     j = money // i
#     if j != 0:
#         print("[ %d ] %d개" %(i, j))
#     money = money % i
#     if money == 0:
#         break


# write = input("입력 : ")
# result = write[ : : -1]#값을 -1번부터 역순으로 넣어준다.
# print("결과 : ", result)

# for i in range(len(write)-1, -1, -1):
#     print(write[i],end="")

# for i in enumerate(write):
#     print(i)
# for i, v in enumerate(write):
#     print("index : %d, value : %s"%(i, v))

def reverse():
    write = input("입력 : ")
    mylist = list(write)
    result = ''
    for i in range(len(mylist), 0 ,-1):
        result += mylist[i-1]
    print("결과 >>", result)
reverse()

