#多态：同一种行为的不同表现形式   多态的前提：继承和重写
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