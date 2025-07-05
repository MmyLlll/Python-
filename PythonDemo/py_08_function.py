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
#abs:绝对值  sum：求和，必须是可迭代对象   min/max:求最小/大值
# zip：j将可迭代对象作为参数，将对象中对应的元素打包成一个元组
li = [1,2,3]
li1 = ['a','b','c','d']
data = zip(li,li1)
print(data,'zip返回的数据类型是：',type(data))
for i in zip(li,li1):   #方式一：for循环取出其中的元素，如果元素不一致，就按照长度最短的返回
    print(i)

li2 = [1,2,3]
li3 = ['a','b','c','d']
print(list(zip(li,li1)))            #转换为列表输出，参数都必须是可迭代元素


#map：可以对可迭代对象中的没一个元素进行映射，分别去执行,map(func,item)，item中的每一个元素都会执行一次func函数
li4 = [1,2,3]
def func(a):
    return a*a
ma = map(func,li4)          #只需要写函数名，不需要括号，执行后返回每一个结果
for i in ma:
    print(i)

#reduce():先按顺序把对象中的元素取出来两个，进行计算然后保存，在与第三个值进行计算（累加）   需要先导包
#reduce(function,sequenccee)   function—函数必须有两个参数的函数（只能是两个），sequence—序列，必须是可迭代对象
from functools import reduce
li5 = [1,2,3,4]
def add(a,b):
    return a+b
res = reduce(add,li5)
print(res)


#拆包  含义：对于函数中的多个返回数据，去掉元组，列表或者字典，直接获取里面数据的过程
tua = (1,2,3,4,)
print(tua)
#单个取出元组中的元素
#方式一：
a,b,c,d = tua
print('a=',a,'b=',b ,'c=',c,'d =',d )       #要求变量的个数和元组内元素的个数相同，不然报错，一般在获取元组值的时候使用
#方式二：
a,*b = tua                  #一般在函数调用时使用
print(a,b)
def funa(a,b,*arges):
    print(a,b)
    print(arges)
funa(1,2,3,4,5,6,7,8,9)
arg = (1,2,3,4,5,6,7,8,9)
funa(*arg)

def func(a,*b):
    print(type(b))
arg=(1,2,3,4)
func(1,2,3,4)

