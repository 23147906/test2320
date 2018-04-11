#! -*- coding:UTF-8 -*-
# Author:Win_Li   23147
# Date:2018-03-26 23:19

#
# l1 = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
# d = {'k1': [], 'k2': []}
#
# for i in l1:
#     if i > 66:
#         d['k1'].append(i)
#     elif i < 66:
#         d['k2'].append(i)
# print(d)

li = ["手机", "电脑", '鼠标垫', '游艇']

while True:
    for index, i in enumerate(li, 1):
        print(index, i)
    user_input = input('请输入您的选择、‘T’添加或‘Q’退出：')
    if user_input == 'T':
        user_app = input('请添加商品：')
        li.append(user_app)
        print('------添加商品：%s成功' % user_app)
    else:
        if user_input.isnumeric():
            if 0 < int(user_input) <= len(li):
                print('----您的选择是：%s' % li[int(user_input)-1])
            else:
                print('您输入超出范围，请重新输入！')
                continue
        elif user_input == 'Q':
            break
        else:
            print('输入有误，请重新输入！')
            continue

