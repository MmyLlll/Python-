#多态：同一种行为的不同表现形式,多态的前提：继承和重写
class Animal(object):
    def shout(self):
        print('动物会叫')
class Dog(Animal):
    def shout(self):
        print('小狗汪汪汪')
class Cat(Animal):
    def shout(self):
        print('小猫喵喵喵')
#同一个函数展现出来不同的形态
d = Dog()
c = Cat()
d.shout()
c.shout()
#多态性：不同功能的函数了可以使用相同的函数名字，定义一个统一接口，一个接口多种实现
class Animal1(object):
    def eat(self):
        print('吃东西')
class Pig(Animal1):
    def eat(self):
        print('猪吃猪食')
class Dog(Animal1):
    def eat(self):
        print('狗吃狗食')
def test(obj):
    obj.eat()
animal = Animal1()
pig = Pig()
dog = Dog()
test(animal)
test(pig)
test(dog)

#静态方法：@staticmethod,与类无关，可以转换成函数使用,作用：取消不必要的参数传递，有利于减少不必要的内存占用和性能消耗
class Person(object):
    @staticmethod
    def func():            #不需要self参数既可以使用对象访问，也可以使用类访问
        print('人是会学习的动物')
Person.func()
pe = Person()
pe.func()

#类方法：使用装饰器@classmethod来标识其为类方法，对于类方法，第一个参数必须是类对象，一般以cls作为第一个参数，类方法内部可以访问类属性，或者调用类中的其他方法
#使用场景：当方法中需要使用到类对象（如访问私有类属性）是定义类方，一般配合类属性使用
#@classmethod
#    def 方法名（cls，形参）
#           方法体
class Person1(object):
    @classmethod
    def sleep(cls):         #cls代表类对象本身
        print(cls)
        print('人会睡觉')
    @classmethod
    def walk(cls):
        print('人会跑')
Person1.sleep()
print(Person1)

#类中的三种方法：实例方法（普通方法），静态方法，类方法
#实例方法（普通方法）：只能通过实例调用，可以访问和修改实例属性，可以调用其他实例方法和类方法
#静态方法@staticmethod：可以通过类名或实例调用，不能访问实例属性和类属性，因为静态方法和类并没有什么联系
#类方法@classmethod:可以通过类名和实例调用，相当于一个普通函数，只是放在类里面方便管理

#单列模式
#__init___()和__new__()函数
# __init__():是用来初始化对象，可以对属性赋值
# __new_()：是有objec基类提供的内置静态方法，作用是在内存中为对象分配空间和返回对象的引用，创建并返回类的实例，实例化对象时首先会调用的是__new__（）方法而不是__init__()方法
#           而__new__方法时object基类提供的方法，所有类都会继承object基类，所以每个类如果重写了__new__()方法，需要在重写的__new__（）方法中扩展父类的__new__（）
#           方法，并将父类的__new__()函数作为函数的返回值，否则python解释器得不到分配和对地址的应用的内存空间。
#           __new__()是静态方法，所以将其作为返回值时必须传入参数cls
#__new__()方法会创建并返回一个类的实例，如果返回的不是一个类的实例将不会调用__init__（）方法
class Test(object):
    def __init__(self):
        print('这是__init__（）构造函数')
    def __new__(cls, *args, **kwargs):
        print('这是__new__()函数')
        print(super().__new__(cls))                 #cls参数是为了指出要返回的类的类型
        return super().__new__(cls)
te = Test()             #先调用__new__（）方法，在调用__init__（）方法
print(te)

#单列模式
#只能存在一个实例化对象，优点是节省空间，减少不必要的资源浪费，缺点：多线程访问时容易引发线程安全问题
#实现方式：1.通过@classmethod  2.通过装饰器实现   3.通过重写__new__（）实现（重点）   4.通过导入模块实现

#通过重写__new__（）方法实现单列模式
# #设计流程：1.定义一个类属性，初始值为None，用来记录单列对象的引用(地址)  2.重写__new__()方法 3.对用来判断记录单列对象的类属性进行判断   4.根据判断选择创建还是返回引用
class Singleton(object):
    #obj用来记录被创建对象的引用
    obj  = None
    def __new__(cls, *args, **kwargs):
        print('这是__new__()方法')
        if cls.obj == None:
            cls.obj = super().__new__(cls)
        return cls.obj
    def __init__(self):
        print('这是__init__（）方法')
s = Singleton()
print('s:',s)
s2 = Singleton()
print('s2:',s2)

#通过导入模块实现单列模式,模块就是天然的单列模式
from pytest import test as te1
from pytest import test as te2
print('te1:',te1)
print('te1:',te2)

#魔法方法：在Python中__xxx__()这种双下滑线的方法就是魔法方法，指具有特殊功能的函数
#__new__():在内存中为对象分配空间并返回对象的引用
#__init__():初始化对象或给属性赋值（构造函数）
#__doc__:类或函数的描述信息
#__module__():表示当前操作对象所在模块
#__class__():表示当前操作对象所在的类
#__str__():对象的描述信息
#__del__():删除对象（析构函数）
#__call__():使一个实例对象成为可以调用的对象
#__dict__():返回对象具有的属性和方法

class Person(object):
    """类的描述信息__doc__"""             #必须使用多行注释，单行注释无效
    name = ''
    def action(self):
        pass
    def __str__(self):
        return '这里是str的返回值'
    def __call__(self):
        print('这是__call__方法')

#__doc__()魔法方法&魔法属性
print(Person.__doc__)

#__moudle__()和__class__()
p = Person()
p.action()
print(p.__module__)             #输出所在模块
print(p.__class__)              #输出所在类

#__str__(),如果类中定义了此方法，那么在打印对象时，默认输出该方法的返回值，也就是打印方法中return的数据，该方法必须返回一个字符串
p1 = Person()
print(p1)               #会输出__str__（）方法的返回值

#__call__()：是一个实例对象成为一个可调用对象，像函数一样可以被调用
#k可调用对象：函数\内置函数和类都是可调用对象，凡是可以把一对（）应用到某个对象上的都可以称之为可调用对象
#callable（）：判断一个对象是否是可调用函数
p2 = Person()
p2()
print(callable(p2))

print(p.__dict__)
