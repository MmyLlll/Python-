# 您需要编写一个程序，按升序对(名称，年龄，高度)元组进行排序，其中name是字符串，age和height是数字， 元组由控制台输入。
# 排序标准是:
# 1:根据名称排序;
# 2:然后根据年龄排序:
# 3:然后按分数排序。
# 优先级是name>age>得分
# 如果给出以下元组作为程序的输入:
# Tom, 19,80; John,20,90; Jony,17,91; Jony,17,93: Json, 21,85
def sort_tuples(input_string):
    # 将输入字符串按分号分隔成多个部分
    tuples = input_string.split(';')

    # 将每个部分按逗号分隔并转换为元组
    data = [tuple(item.split(',')) for item in tuples]

    # 将元组中的年龄和高度转换为整数
    data = [(name.strip(), int(age.strip()), int(height.strip())) for name, age, height in data]

    # 按照名称、年龄、高度进行排序
    sorted_data = sorted(data, key=lambda x: (x[0], x[1], x[2]))

    return sorted_data

# 输入的元组字符串
input_string = "Tom, 19,80; John,20,90; Jony,17,91; Jony,17,93; Json, 21,85"

# 调用排序函数
sorted_tuples = sort_tuples(input_string)

# 打印排序后的结果
print(sorted_tuples)
