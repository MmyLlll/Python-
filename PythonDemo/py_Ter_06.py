#进程：操作系统进行资源分配和调度的基本单位，运行的程序或软件就是进程
#进程的状态：1.就绪状态：以满足运行条件正在等待cpu执行    2.执行状态：cpu正在执行      3.等待状态（阻塞）;等待满足某些条件执行，比如sleep
#进程语法结构：multiprocession模块提供了一个Process类来代表进程对象
#Process类的参数：target（要执行的目标任务名，子进程要执行的任务），args：以元组形式传参，kwargs：以字典形式传参
#Process类的常用方法：start（）,is alive(判断子进程是否存在，存在返回True)，join(主进程等待子进程执行结束)
#Process类的常用属性：name(进程的别名，默认Process-N)，pid(进程的编号)
from multiprocessing import Process
import  os
def sing():

    print(f"子进程的编号:{os.getpid()}",)
    print('唱歌')
def dance():
    print('跳舞')
if __name__ == '__main__':
    p1 = Process(target=sing,name = "子进程1")
    p2 = Process(target= dance)
    p1.start()
    p2.start()
    print(p1.name)
    print(p1.pid)