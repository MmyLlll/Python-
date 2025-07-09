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
