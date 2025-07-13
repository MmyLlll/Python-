#python中的文件操作
#文件对象的方法
#open():创建一个file对象，默认是以只读模式打开,使用open一定要close关闭文件
#read(n):n表示从文件中读取的数据的长度，没有传入n的值就默认一次性读取文件的全部内容
#write():将指定内容写入文件
#close():关闭文件
#文件的属性
#文件名.name:返回要打开的文件的文件名，可以包含文件的具体路径
#文件名.mode:返回文件的访问模式
#文件名.closed:用来检测文件是否关闭，关闭了返回True否则返回False
f = open('test.txt')
print(f.name)
print(f.mode)
print(f.closed)
f.close()
print(f.closed)
#读写操作
#read(n）：n表示从文件中读取的数据的长度，没有传入n的值或是负数就默认一次性读取文件的全部内容
ff = open('test.txt',encoding='utf-8')
print(ff.read())
ff.close()

#readline():一次只读取一行内容，执行后文件指针指向下一行，准备再次读取
fff = open('test.txt',encoding='utf-8')
# while True:
#     text = fff.readline()
#     if not text:
#         break
#     print(text)

# for i in fff.read():
#     if not i:
#         break
#     print(i,end = '')

for i in fff:
    print(i,end='')
fff.close()

#readlines():按照行的方式把文件内容一次性读取，返回的是一个列表，每一行数的数据就是列表中的一个元素
ffff = open('test.txt',encoding='utf-8')
text = ffff.readlines()
print(text,type(text))
f.close()

#访问模式：r（只读），r+（可读可写），w/a（写入），w+/a+（可读可写）
#r:只读模式，文件必须存在，不然会报错
#w:只写模式，文件存在就会想清空文件，在写入添加内容，不存在就创建新文件，重新编辑原有内容，覆盖原有内容，写入后文件指针会在末尾，直接读取将读不到数据
#a:append的缩写，追加模式，不存在就创建进行写入，存在则在原有内容的基础上添加新的内容
#+：表示可以同事读写某个文件内容，使用+会影响读写效率
#文件定位操作：tell()和seek()
#tell()显示文件内当前位置，及文件指针当前位置
#seek(offset,whence)：移动文件读取指针到指定位置，offset:表示要移动的字节数  whence:表示要移动字节的参考位置，默认值0（文件开头，1（当前位置），2（文件结尾）

file = open('test.txt','a+',encoding='utf-8')
print(file.read())
file.write('写入第七行数据')
print(file.read())
file.close()

#with open:作用是代码执行完，系统会自动调用f.close（）方法，可以省略文件关闭步骤
with open('test.txt','a',encoding='utf-8') as wf:           #wf是文件对象
    wf.write('mimimimimi')
print(wf.closed)

#读取图片，读取到的会是二进制文件
with open(r"C:\Users\1\Desktop\photo.jpg",'rb')as file1:
    img = file1.read()
    # print(img)
#将读取到的文件写入到当前文件
with open(r"D:\ChatData\WeChat\GitPython\PythonDemo\photo.jpg",'wb') as file2:
    file2.write(img)

#目录常用操作，首先要导入模块（os）
import os
#1.文件重命名 os.rename(原文件名，修改后的文件名) 2.删除文件 os.remove(文件名 ) 3.创建文件夹os.mkdir(文件夹名) 4.删除文件夹os.rmdir(文件夹名)
# 5.获取当前文件所在目录os.getcwd() 6.获取目录列表（os.listdir(目录名（默认当前目录列表）)）

#可迭代对象（iterable）的条件:1.实现了_iter_()方法 2.返回了迭代器对象
#for循环工作原理：
#首先透过__iter__()获取可迭代对象的迭代器，然后对获取的迭代器不断调用__next__()方法来获取下一个值并将获取的值返回给临时变量i
#isinstance（o(对象),t（类型(可以传入多个类型)））:判断一个对象是否是可迭代对象，或者是一个已知的数据类型，需要导入模块,from collections import Iterable
from collections.abc import Iterable
st = '123'
print(isinstance(st,Iterable))
print(isinstance(st,int))

#迭代器：可以记住遍历位置的对象，iter():获取可迭代对象的迭代器     next():一个个去取元素，取完元素后会引发一个异常
#iter（）就是调用__iter__()这个魔法方法，并把__iter__()方法的返回值作为自己的返回值
#通过next()方法去一个个的去取元素，最后引发异常（因为取空了）
li = [1,2,3,4,5]
it = iter(li)  #等同 it = li.__iter__()
print(it)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
#取完元素后再用用next（）会触发stopIteration异常
#print(next(it))

#可迭代对象包含__iter__()方法，迭代器包含__iter__()和__next__()方法
#迭代器协议:对象必须提供一个next()，执行该方法要么返回下一项要么返回异常，结束迭代
#自定义迭代器类
class Test(object):
    def __init__(self):
        self.num = 1
    def funa(self):
        print(self.num)
        self.num += 1
te = Test()
for i in range(5):
    te.funa()

class Myiterator(object):
    def __init__(self):
        self.num = 0
    def __iter__(self):
        return self                 #迭代器返回当前迭代器类的实例对象
    def __next__(self):
        if self.num == 10:
            raise StopIteration
        self.num += 1
        return self.num
my = Myiterator()
print(isinstance(my,Iterable))
for i in my:
    print(i)

#生成器（generator）：python中一边循环一边计算的机制叫做生成器
#生成器表达式：类似于列表推导式（[i*5]for i in range(5）)
gen = ([i*5]for i in range(5))                  #生成器表达式，仅把列表推导式的[]改为()
for i in gen:
    print(i)
#python中使用了yiel关键字的函数就称之为生成器函数，
# yield作用:1.类似于return，将指定值或者多个值返回给调用者  2.yield语句一次返回一个结果，在每个结果中间，挂起函数，执行next（）,再重新从挂起点继续往下执行
#是函数中的断，并保存终端的状态
def gen():
    print('生成器函数')
    yield ('a')
    yield ('b')
    yield ('c')
g = gen()
print(next(g))
print(next(g))
print(next(g))

def gen1(m):
    a = 0
    li=[]
    while a<m:
        li.append(a)
        yield a
        a += 1
    print('li:',li)
# for i in gen1(5):
#     print(i)
print(list(gen1(5)))

#可迭代对象包含迭代器，迭代器包含生成器