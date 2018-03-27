#! -*- coding:utf-8 -*-
# Author:Win_Li   23147
# Date:2018-03-19 14:13


user_message = [['win', '123'], ['bing', '452'], ['alex', '567']]  # ['用户名','密码']

user_lock = []
with open('user.txt', 'r') as i:   # 读取锁定用户名到列表
    for username_lock in i.readlines():
        user_lock.append(username_lock.strip())  # 去除用户名后的换行符
    if __name__ == '__main__':
        print(user_lock)  # 检查输出格式是否正确

times = 3  # 允许输错次数
while True:
    username = input('请输入用户名：')
    if username in user_lock:
        print('你的账户已被锁定，请联系管理员！')
        break
    else:
        password = input('请输入密码：')
        user_input = [username, password]
        times -= 1
        if user_input in user_message:
            print('''
            ------Hello %s-------
            恭喜登录成功！
            ''' % username)
            break
        else:
            if times == 0:
                with open('user.txt', 'a') as i:
                    i.write('\n' + username)   # 将输错三次的用户名添加到文件
                print('你输入错误三次，用户已被锁定，请联系管理员！')
                break
            else:
                print('''
                ------sorry------
                用户名和密码不匹配，请重新输入。
                您还有%s次机会。
                ''' % times)



