#! -*- coding:utf-8 -*-
# Author:Win_Li   23147
# Date:2018-03-19 10:57


username = ['seven', 'alex']
password = '123'

time = 0
again_time = 0

while again_time < 2:

    while time < 3:

        input_name = input('请输入用户名：')
        input_password = input('请输入密码：')

        if input_name in username and input_password == password:
            print('登录成功！')
            again_time = 1
            break
        else:
            time += 1
            times = 3 - time
            print('登录失败，还有%s次机会。' % times)
            if time == 3 and again_time == 1:
                break
    if again_time == 1:
        break
    user_input = input('是否继续？“Y” “N”')
    if user_input == 'Y':
        time = 0
        again_time += 1
    elif user_input == 'N':
        break
    else:
        print('输入有误，请重新输入。')



