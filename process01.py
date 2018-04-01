# -*- UTF-8 -*-
# Author:Win_Li   23147
# Date:2018-03-14 15:28


from multiprocessing import Process
import time


class My_Process(Process):
    def __init__(self, name):
        super(My_Process, self).__init__()
        self.name = name

    def run(self):
        time.sleep(2)
        print('hello, ', self.name, time.ctime())


if __name__ == '__main__':
    p_list = []
    for i in range(5):
        p = My_Process('win')
        p.start()
        p_list.append(p)

    for p in p_list:
        p.join()

    print('主进程end！')
