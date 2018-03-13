# -*- UTF-8 -*-
# Author:Win_Li   23147
# Date:2018-03-13 22:49


from multiprocessing import Process
import time


def f(name, age):
    time.sleep(1)
    print('hello,', name, age, time.ctime())


if __name__ == '__main__':
    p_list = []
    for i in range(3):
        P = Process(target=f, args=('win', 32, ))
        p_list.append(P)
        P.start()
    for p in p_list:
        p.join()
    print('主进程end!')