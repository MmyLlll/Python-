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

#range()函数   用来记录循环次数，相当于计数器  range(start,top,step),单参数代表循环次数，双参数是循环的开始和结尾
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

#字符串常见操作
#fine(子字符串，开始位置下标，结束位置下标)：检测某个字符或字符串是否包含在字符串当中，如果在就返回下标位置，如果不在就返回-1
love  = 'miyou'
print(love.find('mi'))

#index(子字符串，开始位置下标，结束位置下标):检测某个字符或字符串是否包含在字符当中，如果在就返回首字符的下标位置，否则就会报错

#find和inex的区别：find 没找到返回-1不影响程序的进一步执行，index没找到则会报错终止程序的运行

#count（），返回某个字符或字符串在整个字符串中出现的次数，没有就返回0

#startSwitch（）/endSwitch（）：判断是不是以某个字符串开头/结尾，是的就返回true，不是返回false，如果设置开始结束为止，则在指定范围内检查

#isupper（）：检查字符串中所有字母是否都为大写，是就返回true

#replace（）：字符串替换
st = '门前大桥下，游过一群鹅'
print(st.replace('鹅','鸭'))

#split():指定分隔符分割字符串,以列表的形式返回
rst = 'hello.python'
print(rst.split('.'))

#capitalize():第一个字符大写
print(rst.capitalize())

#lower():大写字母专为小写

#upper():小写字母转为大写
print((rst.upper()).lower())

