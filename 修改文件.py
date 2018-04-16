#! coding:utf-8 -*-
# Author:Win_Li   23147
# Date:2018-04-03 22:16


# import os
#
#
# file_name = 'file01.txt'
# new_file_name = 'new_%s' % file_name
#
# old_str = '三部门'
# new_str = '很多部门'
#
# f_old = open(file_name, 'r', encoding='utf-8')
# f_new = open(new_file_name, 'w', encoding='utf-8')
#
# for line in f_old:
#     if old_str in line:
#         line = line.replace(old_str, new_str)
#     f_new.write(line)
# print(type(line))
# f_new.close()
# f_old.close()
#
# os.rename(new_file_name, file_name)

file_name = 'file01.txt'

new_str = '三部门'
old_str = '很多部门'

f_old = open(file_name, 'r+', encoding='utf-8')
f = f_old.readlines()
for index, line in enumerate(f):
    if old_str in line:
        line = line.replace(old_str, new_str)
        f[index] = line
print(f)
f_old.seek(0)
f_old.truncate()
f_old.writelines(f)
f_old.close()
