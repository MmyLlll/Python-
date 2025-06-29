print(123)

#sep就是用来间隔多个值
print("哈哈哈","嘿嘿嘿","啦啦啦",sep='/')

#end用来设定以.....结尾，默认是换行符‘\n’,可以切换成其他字符
print("米呦",end='$')
print("靓子")

#标识符被包含在（）内对标识符没有影响
(user) = 1
print(user)

#检测数据类型的方法 type()
num = 1
print(type(num))

#布尔类型数据必须首字母大写

#python比较C新加入复数类型数据complex。固定写法：z=a+bj,a是实部，b是虚部,虚数单位必须是j
z = 2+3j
print(z)
print(type(z))

#三引号字符串类型可以有多行
name = """这是第一行
这是第二行
这是第三行"""
print(name)

#%格式化输出，“%” %0num 1.d:使用0补充空白的未使用位置 2.%.num f 设置小数点后的位数 3.%%   输出一个%
text = '月月鸟的小靓子'
print("表达的内容是：%s"%text)
tag = "靓子"
age = 18
print("%s年龄是%6d"%(tag,age))
f = 1.234
print("%s年龄是%.4f"%(tag,f))

#f格式化输出 f"{表达式}"
fname = "米呦"
fage = "18"
print(f"我的名字是：{fname},我的年龄永远{fage}")