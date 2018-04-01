# -*- UTF-8 -*-
# Author:Win_Li   23147
# Date:2018-03-14 15:38


from multiprocessing import Process
import time


def f(name, age):
    time.sleep(2)
    print('Hello,', name, age, time.ctime())


if __name__ == '__main__':
    p_list = []
    for i in range(5):
        p = Process(target=f, args=('win', 32, ))  # p = Process(target=f('win', 32, )) 这样程序能运行，但是看情况不是并行，更像是串行！
        p_list.append(p)
        p.start()

    for p in p_list:
        p.join()

    print('主进程 end!')
