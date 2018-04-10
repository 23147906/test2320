#! -*- coding:UTF-8 -*-
# Author:Win_Li   23147
# Date:2018-03-26 22:26


li = ['alex', 'eric', 'rain']
print(len(li))
li.append('seven')
print(li)
li.insert(0, 'Tony')
print(li)
li.insert(1, 'Kelly')
print(li)
li.remove('eric')
print(li)
print(li.pop(1), li)

del li[2]
print(li)
del li[1:4]
print(li)
li = ['alex', 'eric', 'rain']
li.reverse()
print(li)
li.sort()
print(li)
for i in range(len(li)):
    print(i)

for a, b in enumerate(li, 100):
    print(a, b)

for i in li:
    print(i)

