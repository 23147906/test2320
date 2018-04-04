#! -*- coding:utf-8 -*-
# Author:Win_Li   23147
# Date:2018-03-20 16:09


import copy


menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车战': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}


input_list = []  # 保存用户的地名输入记录
times = 0  # 记录用户的当前层数
user_menu = copy.deepcopy(menu)  # 记录用户当前层的数据
while True:
    print(user_menu.keys())
    user_menu.clear()
    user_input = input('请输入地名、F-返回、Q-退出：')
# 处理用户输入的数据和记录层数
    if user_input == 'F':
        times -= 1
        input_list.pop()    # 倒序删除用户的输入的地名记录
        # print(input_list.pop())
    elif user_input == 'Q':
        break
    else:
        input_list.append(user_input)
        times += 1
# 根据层数处理地址
    if times > 0:
        for i in range(times):
            if i == 0:
                user_menu1 = copy.deepcopy(menu[input_list[i]])
            else:
                user_menu2 = copy.deepcopy(user_menu1)
                user_menu1.clear()
                user_menu1.update(user_menu2[input_list[i]])
        user_menu.update(user_menu1)  # 记录用户最后调用的字典
        del user_menu1
    else:
        user_menu.update(menu)


# user_menu = menu
        # for i in range(times):
        #     user_menu1 = menu[input_list[i]]
        #     if __name__ == '__main__':
        #         print(user_menu1)
        # user_menu.update(user_menu1[user_input])

