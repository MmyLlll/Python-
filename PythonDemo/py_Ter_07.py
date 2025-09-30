from greenlet import greenlet   #导入greentlet模块
import gevent                   #导入gevent模块
import time                     #导入时间模块

#gevent:遇到IO操作 时，会进行自动切换，属于主动式切换
#注意：文件命名不要和第三方模块或内置模块重名

#3.1使用
#gevent.spawn(函数名):      #创建携程对象
#gevent.sleep():            #耗时操作,执行后执行下一个进程
#gevent.join():             #阻塞，等待某个协程执行完毕
#gevent.joinall():          #等待所有协成对象执行结束再退出，参数是一个协程对象列表

#3.2  耗时操作
# def sing():
#     print('在唱歌')
#     time.sleep(2)
#     print('唱完歌了')
#
# def dance():
#     print('在跳舞')
#     time.sleep(3)
#     print('跳完舞了')
#
# if __name__ == '__main__':
#     #创建协成对象
#     g1 = gevent.spawn(sing)
#     g2 = gevent.spawn(dance)
#     #阻塞，等待协成执行完毕
#     g1.join()
#     g2.join()

# 3.3 joinall()              #等待所有的协程执行完毕在退出
# def sing1(name):
#     for i in range(3):
#         gevent.sleep(1)
#         print(f"{name}再唱歌，被送走的第{i}次")
# if __name__  ==  '__main__':
#     gevent.joinall([
#         gevent.spawn(sing1,'huahua'),
#         gevent.spawn(sing1,'miyou')
#     ])

#monkey补丁：拥有在模块运行时替换的功能
#导入模块
from gevent import monkey
monkey.patch_all()                  #将用到的time.sleep（）代码替换成gevent里面自己实现的耗时操作gevent.sleep（）代码
#注意：monkey.patch_all()   必须放在被打补丁者的前面
def sing1(name):
    for i in range(3):
        time.sleep(1)
        print(f"{name}再唱歌，被送走的第{i}次")
if __name__  ==  '__main__':
    gevent.joinall([
        gevent.spawn(sing1,'huahua'),
        gevent.spawn(sing1,'miyou')
    ])


# 4.总结
# 4.1 线程是CPU调度的基本单位，进程是资源分配的基本单位
# 4.2 进程，线程，协程的对比
#         进程：切换需要的资源最大，效率最低
#         线程：切换需要的资源一般，效率一般
#         协程：切换需要的资源最小，效率高
# 4.3 多线程适合IO密集型操作（文件操作，爬虫），多进程适合CPU密集型操作（科学及计算，对视频进行高清解码，计算圆周率等操作）
# 4.4 进程，线程，协程都是可以完成多任务的，可以根据自己实际开发的需要选择使用