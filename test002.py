#! -*- coding:UTF-8 -*-
# Author:Win_Li   23147
# Date:2018-03-28 0:27


# L1 = [5, 3, 2, 7, 6, 23, 41, 24, 33, 4, 1]
#
# for i in range(len(L1)-1):
#     for a in range(len(L1)-i-1, 0, -1):
#         if L1[a-1] > L1[a]:
#             L1[a-1], L1[a] = L1[a], L1[a-1]
#
#     print(L1)

# list1 = [1, 3, 2, 7, 6, 23, 41, 24, 33, 85, 5]
#
# # for i in range(len(list1)-1):  # 因为是两个元素相比较，所以n(元素个数)-1次就够了
# #     for index in range(len(list1)-i-1):  # 同上
# #         if list1[index] < list1[index + 1]:
# #             list1[index], list1[index + 1] = list1[index+1], list1[index]
# #             print(list1)
#
# add = 0
# for i in range(2, 100):
#     for a in range(2, i):
#         if i % a == 0:
#             break
#     else:
#         print(i)
#         add += i
# print(add)


print('\033[31;1m%s\033[0m' % '输出红色字符')



