# 使用列表推导输出列表中的每个奇数，该列表由一系列逗号分隔的数字输入
def extract_odd_numbers(input_string):
    numbers = [int(num) for num in input_string.split(",")]
    odd_numbers = [num for num in numbers if num%2 !=0]
    return odd_numbers
list = input("Enter comma-separated numbers: ")
odd_numbers = extract_odd_numbers(list)
print(','.join(map(str,odd_numbers)))

    