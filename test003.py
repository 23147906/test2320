#!-*- coding:UTF-8 -*-
# Author:Win_Li   23147
# Date:2018-03-26 22:36


li = ["hello", 'seven', ["mon", ["h", "kelly"], 'all'], 123, 446]

print(li[2][1][1])

li[-3][-1] = 'All'
print(li)

tu = ('alex', 'eric', 'rain')
print(len(tu))
print(tu[1])
print(tu[0:2])
for i in tu:
    print(i)
for i in range(len(tu)):
    print(i)
for index, i in enumerate(tu, 10):
    print(index, i)



