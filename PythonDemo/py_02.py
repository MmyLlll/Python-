print(123)

# 运算符 //取整除，取商的整数部分，向下取整（不管四舍五入原则，直接忽略小数）
a = 5
b = 2
print(a//b)

# 运算符 **取幂数 ， m**n：m的n次方
print(a**b)

#算数优先级 幂>乘,除,取余数，取整数>加减

#input(prompt)输入函数，prompt是提示，会在控制台显示
#name = input("请输入姓名：")
#print("姓名是：%s"%name)

#/t制表符 通常表示四个字符，也称缩进
print("小米呦\t不离开月月鸟")

#\n 换行符

#\r 表示将当前位置移到本行开头
print("abcd\refg")

#r 输出原生字符串
print(r"/t/r/n///")

#python首行缩进不正确会报错
age = 19
if age<18:
    print("年龄小于18岁")
else:
    print("可以陪鹏鹏了哦")

a=100
b=200
print(a==b)

#and运算符等同于&&，左右都为真才为真
c= '鹏鹏'
s= '米呦'
if c == '鹏鹏' and s == '米呦':
    print("在一块了")

#or运算符等同于||，左右有一个为真即为真
t = '刃影'
f = '花花'
if f == '花花' or t == '米呦':
    print("在一块了")
else:
    print("都不对")

#not运算符等同于！，真为假假为真
print(not 3>9)

#三元表达式，类似与三目运算符   基本格式：为真结果if判断条件else为假结果
x=50
y=10
if x <= y:
    print('a小于等于b')
else:
    print('a大于b')

print('a小于等于b')if x <= y else print('a大于b')

#python中 if_elif等同于 if else if格式
v =2

if v< 10:
    print('差劲')
elif v==10:
    print('一般')
elif v > 10:
    print('挺牛')

