#递归函数
def add():
    s= 0
    for i in range(1,101):
        s += i
    print(s)
add()
def add2(n):    #要累加到第n项
    if n<=0:
        return 0
    return n+add2(n-1)
print(add2(100))

#递归实现斐波那契数列
def addf(n):
    if n <= 1:
        return n
    return addf(n-2)+addf(n-1)
print(addf(5))

#闭包   条件：1.必须是嵌套函数2.内层函数使用外层函数的局部变量3.外层函数的返回值是内层函数的函数名
def outer():
    n = 10
    def inner():
        print(10)
    return inner
print(outer())
outer()()

#函数引用
def funa():
    print(123)
print(funa)             #函数名储存的是函数的地址
#id()可以查看变量的地址，可以用来判断两个变量是否是同一个值的引用
a = 1   #a只是一个变量名，用来存储1这个数值所在的地址，就是a里面存储了1这个值内存地址的引用
print(id(a))
a=2
print(id(a))
print(id(2))

def test():
    print('这是test函数')
test()
print(test)             #输出的是tets函数所在内存的地址
te = test
te()                    #通过引用调用函数

#装饰器
def test1():
    print('找小米呦去')
def test2(fn):
    fn()
    print('小米呦在这呢')
test2(test1)
#装饰器的作用：在不修改原有代码的基础上添加新的功能，条件：1.不修改源程序或函数的代码  2.不改变函数或程序的调用方法
