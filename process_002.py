# -*- UTF-8 -*-
# Author:Win_Li   23147
# Date:2018-03-13 23:06


from multiprocessing import Process
import time


class My_Process(Process):
    def __init__(self):
        super(My_Process, self).__init__()  # 这里没有理解

    def run(self):
        time.sleep(1)
        print('hello,', self.name, time.ctime())


if __name__ == '__main__':
    p_list = []
    for i in range(4):
        p = My_Process()
        p_list.append(p)
        p.start()

    for p in p_list:
        p.join()

    print('主进程，end！')
