#编写一个可以计算给定数阶乘的程序，结果以逗号分割，打印在一行上
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         result = 1
#         for i in range(1,n+1):
#             result*=i
#         return result
# n = int(input("请输入一个整数："))
# print(factorial(n))

def fact(x):
    if x == 0:
        return 1
    return x*fact(x-1)
s = int(input("请输入一个整数："))
print(fact(s))