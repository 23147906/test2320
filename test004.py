#! -*- coding:UTF-8 -*-
# Author:Win_Li   23147
# Date:2018-03-26 22:44


tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11,22,33)}, 44])

tu[1][2]['k2'].append('Seven')
print(tu)

dic = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}

for i in dic.keys():
    print(i)
for i in dic.values():
    print(i)

for key in dic:
    print(key, dic[key])

dic['k4'] = 'v4'
print(dic)
dic['k1'] = 'alex'
print(dic)
dic['k3'].append(44)
print(dic)
dic['k3'].insert(0, 18)
print(dic)

