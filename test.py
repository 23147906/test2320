#! -*- coding:utf-8 -*-
# Author:Win_Li   23147
# Date:2018-03-25 23:26


# li = ['alex', 'eric', 'rain']
# li2 = '_'.join(li)
# print(li2)

li = ["alex ", " ar ic", "Alec ", "Tony", "rain"]
li2 = []
li3 = []
for i in li:
    s = i.replace(' ', '')
    li2.append(s)
    if (s.startswith('a') or s.startswith('A')) and s.endswith('c'):
        li3.append(s)
print(li2, li3)

tu = ("alex", " aric", "Alec", "Tony", "rain")
tu1 = []
tu2 = ()
for i in tu:
    s = i.replace(' ', '')
    if (s.startswith('a') or s.startswith('A')) and s.endswith('c'):
        tu1.append(s)
print(tu1)

dic = {'k 1': "al ex", 'k 2': ' ari c', "k3": "Alex", "k4": "Tony", 'k5': 'arr'}
dic1 = {}
dic3 = {}
for i in dic:
    d_key = i.replace(' ', '')
    d_value = dic[i].replace(' ', '')
    dic2 = {d_key: d_value}
    dic1.update(dic2)
    if (d_key.startswith('a') or d_key.startswith('A')) and d_key.endswith('c'):
        dic3.update(dic2)
    elif (d_value.startswith('A') or d_value.startswith('a')) and d_value.endswith('c'):
        dic3.update(dic2)
print(dic1, dic3)




