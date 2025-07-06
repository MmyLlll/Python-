#python中的异常问题
#Python assert（断言）用于判断一个表达式，在表达式条件为 false 的时候触发异常。（try.....except......）
while True:
    try:
        x=int(input('请输入一个数字：'))
        break
    except:                                     #输入的不是数字时出发异常
        print('你输入的不是数字')

#形式二：try/except.....else.else 子句将在 try 子句没有发生任何异常的时候执行。
while True:
    try:
        x = int(input('请输入一个数字：'))
    except:
        print('你输入的不是数字')
    else:
        print(f'你输入的数字是：{x}')
        break

#形式三：try ...finally,try-finally 语句无论是否发生异常都将执行最后的代码。
while True:
    try:
        x = int(input('请输入一个数字：'))
    except:
        print('你输入的不是数字')
    else:
        print(f'你输入的数字是：{x}')
    finally:
        print(f'你输入的数字是：{x}')
        print('finally一定执行的代码')
        break

#Python 使用 raise 语句抛出一个指定的异常。raise语法格式如下：raise [Exception [, args [, traceback]]]
#raise Exception('米呦不回我消息')
def login():
    pwd = input('请输入你的密码：')
    if len(pwd) >= 6:
        return '密码输入成功'
    raise Exception('密码长度不足6位')
try:                            #捕获异常是为了检测到异常时，代码还能继续向下执行
    print(login())
except Exception as err:
    print(err)


#python中的模块，一个py文件就是一个模块，导入模块就是执行一个py文件，模块分类：1.内置模块 2.第三方模块 3.自定义模块
#方式一：import 模块名
#方式二：from ... import 功能一，功能二...   从模块中导入指定的部分，使用时直接使用函数名调用
#方式三：from... import *

#as 起别名 语法：import 模块名 as 别名
import py_08_function as pt
print(pt.add(2,9))

#as给功能起别名   from 模块名 import 功能名 as 别名
from py_08_function import buy as pn
print(pn())

#内置全局变量_name_  语法 if _name_  == "__main__"  用来控制py文件在不同的场景执行不同的逻辑
#文件在当前程序执行（自己执行）：__name__ = "__main__",文件被当做模块导入其他的py文件：__name__ = 模块名

#包：项目结构中的文件（目录），将与联系的模块放在同一个文件夹下
#与普通文件夹的区别，包文件夹自带_init_.py文件夹
#作用：有效避免模块名冲突的问题，让结构更清晰
#import导入包时，先执行_init_.py文件的代码
#可以在包的_init_.py文件中先导入包 内的.py文件
#__all__：本质上是一个列表，可一个控制要引入的东西（模块，函数...）列表里面的元素就代表要导入的模块,在使用from ....import *导入时就只能导入此列表中的元素

# print('方式一')
# import pack_01

# print('方式二')
# from pack_01 import register

print('方式三')
from pack_01 import *
