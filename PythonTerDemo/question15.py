# 编写一个程序，计算a+ aa+aaa +aaaa的值，给定的数字作为a的值。
# 假设为程序提供了以下输入:9;输出应该是:11106
def calculate_expression(a):
    result = 0
    a_str = str(a)
    a_part = int(a_str)
    aa_part = int(a_str*2)
    aaa_part = int(a_str*3)
    aaaa_part = int(a_str*4)
    result = a_part + aa_part + aaa_part + aaaa_part
    return result

a = input("请输入一个数字：")
output_value = calculate_expression(a)
print(output_value)
