#线程:cpu调度的基本单位，每一个进程至少有一个线程，需要导入线程模块
#守护线程（线程执行完之前会向下执行）：需要import threading
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
    #阻塞主线程（防止主线程运行完结束子线程）：暂停作用，等子线程结束之后主线程继续执行，必须在star后
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