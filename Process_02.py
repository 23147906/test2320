# -*- UTF-8 -*-
# Author:Win_Li   23147
# Date:2018-03-12 23:25


from multiprocessing import Process
import time


class MyProcess(Process):
    def __init__(self):
        super(MyProcess, self).__init__()
        # self.name = name

    def run(self):
        time.sleep(1)
        print('hello', self.name, time.ctime())  # self.name 进程名


if __name__ == '__main__':
    p_list = []
    for i in range(3):
        p = MyProcess()  # 实例化类方法
        p.start()
        p_list.append(p)

    for p in p_list:
        p.join()
    print('end!')
