# testList = [1, 2, 'python']
#
# print(testList[0], testList[1], testList[2])
# print(testList[0], testList[-1], testList[-2])
#
# print(testList[1:3])
# print(testList * 2)
# print(testList + [3, 4, 5])
# print(len(testList))
# print(2 in testList)
#
# del(testList[0])
# print(testList)

# a = ['apple', 'banana', 10, 20]
# a[2] = a[2] + 90
# print(a)
#
# a = [1, 12, 123, 1234]
#
# a[0:2] = [10,20]
# print(a)
#
# a[0:2] = [10]
# print(a)
#
# a[1:2] = [20]
# print(a)
#
# a[2:3] = [30]
# print(a)
#
# a[3:4] = [40]
# print(a)
# a = a + [1, 2, 3]
# print(a)

a = [1, 12, 123, 1234]
# a[1:2] = []
# print(a)
# print(len(a))
# a[0:] = []
# print(a)

# a[1:1] = ['a']
# print(a)
#
# a[5:] = [12345]
# print(a)
#
# a[:0] = [-12, -1, 0]
# print(a)


# a = [1, 12, 123, "hello", 3.14, 1000]
# print(a)
# a.append(5)
# print(a)
# a.insert(3, 1000)
# print(a)
# a.extend([6, 7, 8])
# print(a)
# a.remove(1000)
# print(a)
# a.pop(2)
# print(a)
# a.pop()
# print(a)


# t = (1, 2, 3)
# print(t, type(t))
# t = 1, 2, 'python'
# print(t, type(t))
#
# print(t[-2], t[-1], t[0], t[1], t[2])
# print(t[1:3])
# print(t[:])
# print(t * 2)
# print(t + (3, 4, 5))


# a = {}
# a['r38'] = "빅데이타"
# a['r32'] = 'c언어'
# print(a)
#
# d = {'basketball': 5, 'soccer': 11, 'baseball': 9, 'volleyball': 6}
# print(d)
#
# print(d['basketball'])
# print(d.get('basketball'))
# del(d['basketball'])
# print(d)
#
# # d = {}
# # print(d)
# print(len(d))
# print(type(d))
#
# print('soccer' in d)
# print('volleyball' not in d)

# d = {'basketball' : 5, 'soccer' : 11, 'baseball' : 9}
# keys = d.keys()
# print(keys)
# print(type(keys))
#
# for key in keys:
#     print('{0}:{1}'.format(key, d[key]))
#
# values = d.values()
# print(values)
# print(type(values))
#
# items = d.items()
# print(items)

# a = {1, 2, 3}
# print(a, type(a))
#
# print(len(a))
# print(2 in a)
# print(2 not in a)

s1 = set([1, 2, 3, 4, 5, 6, 7, 9 ,10])
s2 = set([10, 20, 30])
print(type(s1), type(s2))

# s3 = s1.union(s2)
s3 = s1 | s2 #합집합
print(s3)

# s4 = s1.intersection(s2)
s4 = s1 & s2 # 교집합
print(s4)

s5 = s1.difference(s2)
s5 = s1 - s2 #차집합
print(s5)

