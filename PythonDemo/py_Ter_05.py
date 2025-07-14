# 线程:cpu调度的基本单位，每一个进程至少有一个线程，需要导入线程模块
# 守护线程（线程执行完之前会向下执行）：需要import threading
import threading
import time
#Thread线程类参数：target（执行的任务名），args(以元组的形式给任务传参),kwargs(以字典的形式给线程传参)
def sing(**name):
    print(name['name'], '在唱歌')
    time.sleep(2)
    print('唱歌结束')
def dance(**name):
    print(name['name'],'在跳舞')
    time.sleep(2)
    print("跳完了")
#主程序入口
if __name__ == '__main__':
    #创建子线程
    #如果要运行的子线程函数有参数，则在第二个参数必须以元组的形式传入参数（targe=函数名，args = （“元组”））
    t1 = threading.Thread(target=sing,kwargs={'name':'月月鸟'})
    t2 = threading.Thread(target=dance,kwargs={'name':'小米呦'})
    #线程保护，最新版本为t1.deamon = true
    t1.setDaemon(True)
    t2.setDaemon(True)
    #开启子线程
    t1.start()
    t2.start()
    #在开启线程之前，主线程执（例如当前这个执行.py文件）行结束子线程也会跟着这结束
    #阻塞主线程（防止主线程运行完结束子线程）：暂停作用，等当前子线程结束之后执行后边的，最后执行主线程，必须在star后
    t1.join()
    t2.join()
    #获取线程名字  t1.geename()
    print(t1.getName())
    print(t2.getName())
    #修改线程名字，t1.setname("修改后的线程名字")
    t1.setName('子线程一')
    t2.setName('子线程二')
    print(t1.getName())
    print(t2.getName())
    print('谢幕结束')

#线程执行是根据cpu调度的，所以是无序的
def task():
    time.sleep(1)
    print('当前线程是：',threading.current_thread().name)

if __name__  ==  "__main__":
    for i in range(5):
        t= threading.Thread(target=task)
        t.start()

#线程之间共享资源
li = []         #定义全局变量
def wdata():
    for i in range(5):          #写入数据
        li.append(i)
        time.sleep(1)
    print('写入的数据是：',li)
def rdate():
    print("读取的数据是：",li)             #读取数据
if __name__ == '__main__':
    wd = threading.Thread(target=wdata)
    rd = threading.Thread(target=rdate)
    wd.start()
    wd.join()
    rd.start()
    rd.join()

#线程竞争
a = 0
b = 1000000
def add():
    for i in range(b):
        global a
        a += 1
    print('第一次累加:',a)
def add2():
    for i in range(b):
        global a
        a += 1
    print('第二次累加:',a)
# add()
# add2()
if __name__ == '__main__':
    a1 = threading.Thread(target=add)
    a2 = threading.Thread(target=add2)
    a1.start()
    a2.start()

#线程同步：用来解决线程竞争问题，方式一（线程等待join）：join（）   方式二（互斥锁）：acquire（）上锁，relase（）释放锁，必须成对出现
#主线程和创建的子线程之间各自执行完自己的代码直至结束
#互斥锁：对共享数据进行锁定，保证多个线程共享数据时会出现数据错误的问题，保证同一时刻只能有一个线程去操作数据，需要导入模块，缺点会影响代码的执行效率
#死锁：没有释放锁，一直等待对方释放锁，会造成应用程序停止响应，不能处理其他任务
from threading import Lock
lock = Lock()
c = 0
d = 1000000
def add3():
    lock.acquire()          #上锁
    for i in range(d):
        global c
        c += 1
    print('第一次累加:',c)
    lock.release()

def add4():
    lock.acquire()          #上锁
    for i in range(d):
        global c
        c += 1
    print('第二次累加:',c)
    lock.release()

if __name__ == '__main__':
    a3 = threading.Thread(target=add3)
    a4 = threading.Thread(target=add4)
    a3.start()
    a4.start()



