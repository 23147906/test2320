#! -*- coding:utf-8 -*-
# Author:Win_Li   23147
# Date:2018-03-19 12:00


# add = 2
# adds = 0
# while 2 <= add <= 100:
#     if add % 2 == 0:
#         adds += add
#     else:
#         adds -= add
#     print(add)
#     add += 1
# print(adds)
#
# add = 0
#
# while 0 <= add <= 12:
#     add += 1
#     if add == 10:
#         continue
#     print(add)

# add1 = 0
# add2 = 0
# while add1 <= 50:
#     while add2 <= 50:
#         print(100 - add2)
#         add2 += 1
#     print(add1)
#     add1 += 1

# add = 0
# while add < 100:
#     add += 1
#     if add % 2 == 0:
#         print(add)

# name = input('Your name :')
# age = input('Your age:')
# hometown = input('Hometown:')
# hobby = input('Hobby:')
#
# print('''
# ----------welcome %s to here----------
# 我是%s
# 今年%s
# 来自%s
# 爱好%s
# ''' % (name, name, age, hometown, hobby))

# while True:
#     user_input = input('请输入年份，退出“Q”：')
#     if user_input == 'Q':
#         break
#     elif user_input.isdigit():
#         user_input = int(user_input)
#         if user_input % 400 == 0:
#             print('润年')
#         elif user_input % 4 == 0:
#             print('闰年！')
#         else:
#             print('不是闰年！')
#
#     else:
#         print('输入有误，请重新输入！')


principal = 10000
tate = 0.0325
times = 2
years = 0
principal_interest = principal

while principal_interest < principal*times:
    years += 1
    principal_interest *= (1 + tate)
    print('第%s年，本息%s元！' % (years, principal_interest))

print('需要%s年，才能增加到%s倍，为%s元。' % (years, times, principal_interest))










