#python中的while循环
i = 1
sum = 0
while i <= 10:
   print('月月鸟的小靓子')
   i += 1
   sum = sum +i
print(sum)
print('Over')

#python中的for循环  基本格式 ： for 临时变量 in可迭代对象：
#                                    循环体
str = 'hellopython'
for i in str:
   print(i)

#range()函数   用来记录循环次数，相当于计数器  range(start,top,step),单参数代表循环次数，双参数是循环的凯斯和结尾
for i in range(1,6):
   print(i)

#unicode：所有字符都是两个字节，字符与数字转换速度快一些，坏处占用空间大
#utf-8：精准，对不同的字符用不同的长度表示，优点节省空间，缺点转换速度比较慢一些
a = 'hello'
print(a,type(a)) #str字符串是以字符为单位进行处理
a1 = a.encode()  #编码
print('编码后',a1)
print(type(a1)) #以字节为单位进行处理
a2 = a1.decode()   #解码
print(a2)

#字符串常见操作   +字符串拼接    *重复输出       in,not in   成员运算符  in：包含返回true，不包含返回false，not in反之
print("小米呦和月月鸟永远在一块\t"*5,'要永远都不分开'*5,sep='\t\t\t')
name = 'xiaomiyou'
print('m' in name)
print('s' in name)
print('m' not in name)
print('s' not in name)

#下表运算符：通过下标可以快速找到的对应的数据   格式：字符串名[下标] ,从右往左数下标用负数
print(name[2])

#切片：含义指对操作的对象截取其中的一部分    语法：[开始位置：结束位置：步长],步长绝对值决定截取间隔，正负号就决定截取方向
st = 'abcdefghijk'
print(st[2:4])
print(st[-1::-1])
print(st[:-1])
print(st[1:6:2])