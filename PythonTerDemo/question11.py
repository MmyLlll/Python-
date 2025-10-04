# 编写一个程序，接收一系列以逗号分隔的4位二进制数作为输入，然后检査它们是否可被5整除， 可被5整除的数字将以逗号分隔的顺序打印。
def check_divisible_by_s():
    input_sequence = input("请输入一系列以逗号分割的是4位二进制数列表：")
    binary_numbers = input_sequence.split(",")
    divisible_by_s_list = []
    for i in binary_numbers:
        binary_number = i.strip()
        decimal_number = int(binary_number,2)
        if decimal_number % 5 ==0:
            divisible_by_s_list.append(binary_number)
    print(divisible_by_s_list)

if __name__ == '__main__':
    check_divisible_by_s()
