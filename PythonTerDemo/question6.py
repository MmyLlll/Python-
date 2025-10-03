#编写一个程序，根据给定的公式计算并打印值:。其中，假设C=50。H=30，D是一个变量，它的值应该以逗号分隔的序列输入到程序中。
# 例:程序的输入序列为(以逗号分隔):100，150，180;则程序输出为:18，22，24;
import math

def calculate_q(d_values):
    C = 50
    H = 30
    result = []
    for D in d_values:
        Q = math.sqrt((2*C*D)/H)
        result.append(round(Q))
    return result

def main():
    input_sequence = input("Enter comma-separated sequence of D values: ")
    q_values = [float(d) for d in input_sequence.split(",")]
    q_values = calculate_q(q_values)
    print(','.join(map(str,q_values)))      #map(str, q_values)：map() 函数会将 q_values 列表中的每个元素应用 str 函数进行转换，即把每个数字转换为字符串。map() 返回的是一个迭代器。

if __name__ == "__main__":
    main()

