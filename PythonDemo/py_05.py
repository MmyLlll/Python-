#python中的元组和字典
#元组的基本格式：元祖名字 = （y元素1，元素2，元素3......），不同元素可以是不同的数据类型,如果只有一个元素，要在最后加上，，不然数据类型视为改元素的类型，而不是元组
#元组与列表的区别：元组仅支持查找，不支持增删改等修改操作
tua = (1,'a',2,'c')
print(tua,type(tua))
tua1 =  (1,2,3,)
print(type(tua1))

#应用场景
#作为函数的参数和返回值
#格式化输出后面的（）本质上就是元组
name = '小米呦'
age = 18
print("%s的年龄是%d"%(name,age))
info = (name , age)
print("%s的年龄是%d"% info)

#字典的基本格式：字典名 = {键1：值1，键2：值2......}键值形式保存
dic = {'name':'小米呦','age':"18"}
print(dic)
#字典常见操作一
#字典中的剑具备唯一性，但值可以重复（被后面的覆盖）
#字典的常见基本操作  1.查看元素 2.修改元素 3添加元素 4.删除元素
#字典中没有下标，不可以用下标查找，查找需要用键名,如果要查找的键名不存在则会报错
print(dic['name'])                  #方式一：如果要查找的键名（name）不存在则会报错
print(dic.get('nam'))               #方式二：如果查找的元素不存在则返回None
print(dic.get('nam','不存在，返回了自定义的内容'))    #get查找返回自定义的内容

#字典可以通过下标修改对应值的内容
dic['age'] = 17
print(dic['age'])

#添加元素，字典名【下标】 = 值，如果键名存在则修改对应的值，如果键名不存在则新增对应的键值对
dic['age'] = 18
dic['love'] = '月月鸟'
print(dic)

#删除元素
#del 【字典名】直接删除整个字典(彻底删除), del 【键】删除对应的键值对,如果键不存在则报错
#clear()：清空字典里面的内容但是保留字典
#pop()删除制定键值对，键不存在就会报错,popitem()默认删除最后一个键值对
del dic['age']
print(dic)
del dic

dic = {'name':'小米呦','age':"18"}      #上面已经删除，这是重新创建的字典
dic.clear()
print(dic)
dic['love'] = '月月鸟'
print(dic)

dic.pop('love')
print(dic)

#字典常见操作二
#len求字典长度  keys()返回字典里面包含的所有键名   values()取出包含的所有的值  items返回字典包含的所有键值对
dic1 = {'name':'小米呦','age':"18",'lvoe':'月月鸟'}
print(type(len(dic1)))
print(dic1.keys())
for i in dic1.keys():    #只取出键名
    print(dic1[i])

for i in dic1.values():
    print(i)
#字典的键值对是以元组形似保存
for i in dic1.items():
    print(i)
