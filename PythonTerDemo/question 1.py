#编写一个程序，找到2000到3200年中所有可以被7整除但不能被5整除的所有数组，得到的数字按都好分割，打印在一行上
def find_numbers():
    numbers = []
    for year in range(2000,3201):
        if year%7 == 0 and  year%5 != 0:
            numbers.append(str(year))
    print(','.join(numbers))
find_numbers()