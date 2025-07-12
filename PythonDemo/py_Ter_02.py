#封装，单继承，重写，新式类
#面向对象的三大特性：封装（隐藏某些属性或方案（private）），继承，多态
#封装：在属性名或者方法名面前加上两个下划线__(只允许类内部使用，无法通过对象访问)
class Person:
    name = '小米呦'
    __age = 18
    def info(self):
        print('name是：',self.name,"age是:",self.__age)
    def interduce(self):
        print(id(self.__age))
        return self.__age
pe = Person()
pe.info()
#print(pe.__age)                #访问出错
#python中的隐藏属性实际上是将名字修改为：__类名__属性明
print(pe._Person__age)

class man:
    def __play(self):
        print('跟小米呦玩')
    def func(self):
        self.__play()
        #man.__play(self)
m = man()
m.func()
#m.__play()            隐藏方法，不可以被访问

#定义内部方法访问隐藏属性
a = pe.interduce()
print(id(a))
print(a)

#_单下划线开头，声明为私有属性或者方法，外部可以使用也可以被继承（口头约定），但在另一个包导入时将无法导入，一般避免与关键字冲突
#__双下划线 开头，隐藏属性，如果定义在类中，无法在外部直接访问，子类不会继承，要访问只能通过间接的方式，当被作为包导入的时候也无法导入，一般是python中的魔术方法，有特殊含义或者功能


#python中的继承(单继承) class 类名（父类）：
class Person():
    def action1(self):
        print('吃饭')
    def action2(self):
        print('奔跑')
class girls(Person):
    pass                  #pass是占位符：给代码设置空白，可以没有任何带啊也不会报错（也可以用None）
g = girls()
g.action1()
g.action2()

class boys(Person):
    pass
b = boys()
b.action1()
b.action2()
#多重继承（同c++继承父类和父类的父类...的所有未隐藏属性）

#python中的重写 1.常规重写   2. 对父类的方法进行重写
#super().方法名对父类方法进行扩展,super()是使用super类创建出来的对象，可以调用父类的方法（完整写法super(子类名，self).父类方法名）
class Person():
    def money(self):
        print("有1000个w")
    def sleep(self):
        print("sleep")
class man(Person):
    def money(self):
        #Person.money(self)
        super().money()
        super(man,self).sleep()
        print('有100个w')
m  = man()
m.money()

#新式类
class A:
    pass
class AA():
    pass
class AAA(object):    #继承了object或者object的子类的都是新式类（python为所有对象提供object顶级父类，提了一些内置的属性和方法，可以使用dir（）查看
    pass

print(dir(object))

#多继承
#python中多继承的父类中如果有同名的方法，会按顺序调用最先继承的父类中的方法就近原则
class Father(object):
    def action1(self):
        print('嘿嘿嘿')
    def money(self):
        print('100个w可以获取')
class Mother(object):
    def action2(self):
        print('哈哈哈')
    def money(self):
        print('120个w可以获取')
class Son(Father,Mother):
    pass

s = Son()
s.action1()
s.action2()
s.money()

#python中的方法搜索顺序 (__mro__属性)
print(Son.__mro__)