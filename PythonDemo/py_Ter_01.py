#python中的类
class  Washer:
    height = 0
Washer.height = 100
Washer.weight = 200
print(Washer.height)
print(Washer.weight)

wa1 = Washer()
wa2 = Washer()

print(wa1)
print(wa2)

#实例方法
#pythin中使用对象调用类中的方法，被执行的方法至少有一个self参数，在执行是时，将自动把调用该方法的对象本身传递给self
class  Washer1:
    height = 100
    def wash(self):         #self表示调用这个方法的对象
        print("功能洗衣服")
        print(self)
#self代表对象本身，当对象调用实例方法时，python会自动将对象（调用方法的对象）的引用作为参数传递给被调用方法的第一个参数（self）
print(Washer.height)
wa3 = Washer1()
wa3.wash()
print('wa3:',wa3)
wa4 = Washer1()
wa4.wash()
print('wa4:',wa4)

#实例属性(用来为对象添加动态属性)
class  Person:
    name = '小米呦'
    def action(self,*args):
        actions = ''.join(args)
        print(f"{self.name}吃饭{actions}")
pe = Person()
pe.action()
pe1 = Person()
pe1.name = '月月鸟'
pe1.location = '家'
pe1.action('和小米呦在一起',',嘻嘻嘻')

#python中类的构造函数（__init__()）,作用：用来作为属性初始化或者赋值操作（基本同C++）
class  Person1:
    name = '小米呦'
    def __init__(self,name,sex,age):
        self.name = name
        self.sex = sex
        self.age = age
    def action(self,*args):
        print(f"{self.name}是个{self.sex}在{self.age}跟月月鸟（小米呦）在一块")
pe2 = Person1('月月鸟','男',25)
pe2.action()
pe3 = Person1('小米呦','女',19)
pe3.action()

#python中的析构函数__dedl__()，删除对象时默认调用
class cat:
    def __init__(self):
        print('__init__构造函数')
    def __del__(self):
        print('销毁对象')
c = cat()
del c
print('销毁p继续向下执行')