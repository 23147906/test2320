#! -*- coding:utf-8 -*-
# Author:Win_Li   23147
# Date:2018-03-19 9:42


age = 33
add = 0
print(id(add))
while True:
    while add < 3:
        add += 1
        guess = int(input('请输入你猜的年龄：'))
        if guess == age:
            print('恭喜你答对了！')
            break
        elif guess < age:
            print('小了')
        else:
            print('大了')

    user_add = input('三次用完，继续“Y”“y”，结束“N”“n”')
    if user_add == 'Y' or user_add == 'y':  # user_add = 'Y' or 'y'
        add = 0
    elif user_add == 'N' or user_add == 'n':
        break
    else:
        print('输入有误，请重新输入！')



