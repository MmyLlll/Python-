#python中的类型转换，忽略简单内容（（int），（float），（char）....）
#eval()函数,执行一个字符窜表达式，并返回结果，eval（）可以实现字符串到list，dict，tuple，str之间的转换
print(eval('10+10'))
str = '[[1,2],[3,4],[5,6]]'             #字符串转换list
print(type(str))
print(eval(str),type(eval(str)))

str1 = "{'米呦':'我的love','年龄':18}"            #字符串转换字典
print(type(str1))
print(eval(str1),type(eval(str1)))

str2 = '(1,2,3,4,5)'
print(type(str2))
print(eval(str2),type(eval(str2)))

#list（）：可以将可迭代对象转换为列表,对象必须是可迭代对象
print(list('abcdefg'),type(list('abcdefg')))
print(list((1,2,3,4)),type(list((1,2,3))))
print(list({'米呦':'我的love','年龄':18}),type(list({'米呦':'我的love','年龄':18})))     #字典转换成列表会取键名作为列表的值

#python中赋值操作完全共享资源，一个改变另一个也会跟这个改变，类似于c中的指针

#浅拷贝<数据半共享>：会创建一个新的对象，拷贝第一层的数据，嵌套层（内部元素）会指向原来的地址
#[1,2,3,4,5,[66,99,88]]（外层的地址不同，内层的地址相同）
#优点：拷贝速度快，占用空间少，拷贝效率高
import copy       #导入copy模块
li = [1,2,3,4,5,[66,99,88]]
li2 = copy.copy(li)
print(li,id(li))            #id()产看内存地址
print(li2,id(li2))
li.append(8)
print(li,id(li))
print(li2,id(li2))
#往嵌套列表添加元素
li[5].append(55)
print(li,id(li))
print(li2,id(li2))
print('li[5]的地址：',id(li[1]))                 #内层嵌套（内部元素）的地址相同
print('li2[5]的地址：',id(li2[1]))

#深拷贝<数据完全不共享>：第一层的数据和内部嵌套（内部元素）的其它层数据完全拷贝，拷贝后和原来的对象无任何关联
#[1,2,3,4,5,[66,99,88]]（外层内层的地址都不同）
#优点：拷贝效率高，节省内存
import copy       #导入copy模块
li1 = [1,2,3,4,5,[66,99,88]]
li3 = copy.deepcopy(li1)
print(li1,id(li1))            #id()产看内存地址
print(li3,id(li3))
print('li1[5]的地址：',id(li1[5]))                 #内层嵌套（内部元素）的地址也不相同
print('li3[5]的地址：',id(li3[5]))
li1.append(9)
li1[5].append(55)
print('li1:',li1)
print('li3:',li3)

#可变对象（内存地址不会变）：允许修改的对象就是可变对象，这种数据类型就是可变类型，常见可变类型：list、dict、set....
set = {'1','2','3','4'}
print(set)

#不可变对象：如果修改对象的值就会分配新的内存空间，常见类型：int、char、float、tuple、str