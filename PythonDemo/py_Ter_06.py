# 进程：操作系统进行资源分配和调度的基本单位，运行的程序或软件就是进程
# 进程的状态：1.就绪状态：以满足运行条件正在等待cpu执行    2.执行状态：cpu正在执行      3.等待状态（阻塞）;等待满足某些条件执行，比如sleep
# 进程语法结构：multiprocession模块提供了一个Process类来代表进程对象
# Process类的参数：target（要执行的目标任务名，子进程要执行的任务），args：以元组形式传参，kwargs：以字典形式传参
# Process类的常用方法：start（）,is alive(判断子进程是否存在，存在返回True)，join(主进程等待子进程执行结束)
# Process类的常用属性：name(进程的别名，默认Process-N)，pid(进程的编号)
from multiprocessing import Process,Queue
import os
import time
#from queue import Queue
# def sing():
#
#     print(f"子进程的编号:{os.getpid()}",)        #os.getpid()当前进程id，os.getppid()父进程id
#     print('唱歌')
# def dance():
#     print('跳舞')
# if __name__ == '__main__':
#     p1 = Process(target=sing,name = "子进程1")
#     p2 = Process(target= dance)
#     p1.start()
#     p2.start()
#     print(p1.name)
#     print(p1.pid)

#进程之间不共享全局比变量
# li = []         #定义全局变量
# def wdata():
#     for i in range(5):          #写入数据
#         li.append(i)
#         time.sleep(1)
#     print('写入的数据是：',li)
# def rdate():
#     print("读取的数据是：",li)             #读取数据
# if __name__ == '__main__':
#     p3 = Process(target=wdata)
#     p4 = Process(target=rdate)
#     p3.start()
#     p4.start()

#进程之间的通信：Queue（队列）
# put（）：放入数据
# get（）：取出数据
# empty（）：判断队列是否为空
# qsiz（）：返回当前队列包含的消息数量
# full（）：判断队列是否满了
q = Queue(3)                    #初始化一个队列，最大数量为三，没写或负值则代表没有上线
q.put('miyo')
q.put('yueyueniao')
q.put('huahua')
print(q.get())                  #获取队列中的一条消息，并从队列中移除

li = ['张三','李四','王五','老六']         #定义全局变量
def wdata(q1):
    for i in range(5):          #写入数据
        print(f"{i}已经被放入")
        q1.put(i)
        time.sleep(0.2)
    print('写入的数据是：',li)
def rdata(q2):
    while True:
        if q2.empty():
            break
        else:
            print("取出数据:",q2.get())
    print("读取的数据是：",li)             #读取数据
if __name__ == '__main__':
    #创建队列对象
    q0 = Queue()
    p5 = Process(target=wdata,args=(q0,))
    p6 = Process(target=rdata,args=(q0,))
    p5.start()
    p6.start()
