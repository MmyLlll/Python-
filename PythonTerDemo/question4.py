#编写一个程序，该程序接收控制台以逗号分隔的数字序列，并生成包含每个数字的列表和元组,假设，向程序提供以下输入:34
#岁,67年,55岁,33岁,12日,98年; 则输出为:!"34’，"67’，"55’，"33’,"12’，"98(“34"，"67"，"55’，"33，"12’，"98”)
import re
def extract_numbers(input_string):
    number = re.findall(r'\d+',input_string)
    return number

def generate_list_and_tuple(numbers):
    number_list = numbers
    number_tuple = tuple(numbers)
    return number_list,number_tuple

def main():
    number = input("请输入以逗号分隔的数字序列，并包含一些非数字字符（如'34岁,67年,55岁,33岁,12日,98年'）：")
    numbers = extract_numbers(number)
    number_list,number_tuple = generate_list_and_tuple(numbers)
    print(f"列表: {', '.join(repr(num) for num in number_list)}")
    print('列表：', number_list)
    print('元组: ', number_tuple)

if __name__ ==  "__main__":
    main()
