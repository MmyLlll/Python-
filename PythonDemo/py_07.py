#python中的类型转换，忽略简单内容
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

