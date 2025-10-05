# 编写一个程序，找到1000到3000之间并且所有位数均为偶数的所有数字，比如2000，2002等;获得的数字都以逗号分隔的顺序，打印在一行上。
def find_even_digits():
    even_digitis =  []
    for number in range(2000,3001):
        if number%2==0:
            even_digitis.append(number)
    return even_digitis

list = find_even_digits()
result = ','.join(map(str,list))
print(result)