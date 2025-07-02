#字符操作，数组操作
#列表：基本格式   列表名 = [元素1，元素2，元素3,......]，元素之间的数据类型可以各不相同
li = [1,2,'a',4]
print(li,type(li))
print(li[2])

#列表也可以进行切片操作
print(li[1:4])

#列表是可迭代对象，可以for循环遍历取值
for i in li:
    print(i)

#添加元素  append（）整体添加，extend（）把字符串分割成单个字符添加，insert（）指定位置插入元素
list  = ['one','two','three']
list.append('four')
print(list)
list.extend('five')
print(list)
list.insert(2,"穿插")
print(list)

#修改元素,通过下标就可以直接修改

#查找元素   in  not in

#删除元素 del：格式 del 列表或者del 列表【索引】  pop:制定下标删除元素，python.以上默认删除最后一个元素   remove：根据元素的值进行删除,列表中不存在就会报错
lidel = ['a','b','c','d','e','f','g']
del lidel[2]        #根据索引删除
print(lidel)

lidel.pop(0)
print(lidel)

lidel.remove('g')
print(lidel)

#排序 sort：将列表按特定顺序排序，默认从小到大   reverse:倒序，将列表反过去
num = [1,3,9,5,7,2,4,6,8]
num.sort()
print(num)

num.reverse()
print(num)

#列表推导式   基本格式：一.【表达式  for 变量 in 列表（也可以是迭代对象）】 二.【表达式  for 变量 in 列表（也可以是迭代对象） if 条件】
il = [1,2,3,4,5,6]
il.reverse()
[print(i) for i in il]

il1 = []
for i in range(1,11):
    if(i%2 == 0):
        continue
    else:
        il1.append(i)
print(il1)

il2 = []
[il2.append(i) for i in range(1,11) if(i%2 != 0)]
print(il2)

#列表嵌套
il3 = [[1,2,3],[4,5,6],[7,8,9]]
print(il3[1][0])