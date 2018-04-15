#! -*- coding:UTF-8 -*-
# Author:Win_Li   23147
# Date:2018-03-27 21:18


# l1 = [11, 22, 33]
# l2 = [22, 33, 44]
#
# s1 = set(l1)
# s2 = set(l2)
#
# s3 = s1.difference(s2)
# s4 = s1 - s2
# print(s3, s4)
#
# s3 = s2.difference(s1)
# s4 = s2 - s1
# print(s3, s4)
#
# s3 = s1.symmetric_difference(s2)
# s4 = s1 ^ s2
# print(s3, s4)
#
# s3 = s1.intersection(s2)
# s4 = s1 & s2
# print(s3, s4)
#
# s3 = s1.union(s2)
# s4 = s1 | s2
#
# print(s3, s4)
#
#
# for i in range(0, 101):
#     print(i)

# a = 100
# while a > 0:
#     print(a)
#     a -= 1
#
# a = 1
# while a <= 100:
#     print(a)
#     a += 1

# for i in range(100, 0, -1):
#     print(i)

for i in range(1, 10):
    for a in range(1, i+1):
        s = i * a
        print('%s*%s=%s  ' % (i, a, s), end='')
    print('')


# 1*1 = 1
# 2*1 = 2 2*2 = 4
# 3*1 = 3 3*2 = 6 3*3 =9


add = 0
for i in range(2, 100):
    for a in range(2, i):
        if (i % a) == 0:
            break
    else:
        print(i)
        add += i
print(add)
