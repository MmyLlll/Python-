#python中函数的定义
#格式：            def 函数名()：
#                           函数体
def login():
    print("这是登录函数")
login()

#返回值
def buy():
    return '小米呦','月月鸟'          #返回多个值时，以元组的形式返回
print(buy())

#可变参数作为函数的参数：传入的值的数量可以是改变的，可以传入多个，也可以不传   格式 def func(*arge),传入多个参数时以元组的形式接收
def func(*arge):
    print(arge)
    print(type(arge))
func('小米呦','月月鸟')

#关键字参数：格式    def func(**kwarges)以字典的形式接受参数
def fun(**kwarges):
    print(kwarges)
    print(type(kwarges))            #字典类型
fun(name = '小米呦',age = 18)          #采用键值的形式传值

#变量的作用域
#Python中想要在函数体内声明全局变量使用global关键字  global 变量名 ,global也可对以声明的全局变量进行修改（在函数体内修改）
a = 111
def func1():
    global s
    s = 999
func1()
print('输出函数内定义的全局变量s：',s)

#nonlocal关键字    用来声明外层的局部变量，在外部函数先进行声明，内部函数使用nonlocal进行声明
a = 10   #全局变量
def outer():              #外函数
    a = 5
    def inner():           #内函数
        nonlocal a              #nonloacl只能对上一层函数内的变量进行修改
        a = 20
        print('inner函数中a的值：',a)
    inner()
    print('outer函数中a的值：',a)
outer()
print('全局变量a的值:',a)

#匿名函数 基本语法 ：函数名 = lambda 形参：返回值（表达式），lambda不需要写return来返回值，表达式本身就是返回
#调用：结果 = 函数名（实参）
def add(a,b):
    return a+b
print(add(1,3))

addd = lambda a,b,c:a+b+c            #匿名函数
print(addd(1,3,5))

#lambda的应用
#lambda结合if判断
#特点lambda只能实现简单的的逻辑，如果逻辑复杂且代码量比较大不建议实用lambda降低代码的可读性
comper  = lambda a,b:'a大于b' if a>b else 'a小于等于b'
print(comper(10,8))

#内置函数
import builtins
print(dir(builtins))            #显示所有内置函数及变量，大写字母开头一般是内置常名，小写开头一般是内置函数名



