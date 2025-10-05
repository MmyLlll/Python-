# 编写一个接收句子的程序，并计算大写字母和小写字母的数量。 假设为程序提供了以下输入:Helo world! 则输出应该是:UPPER CASE 1: LOWER CASE 9
def count_case_letters(sentence):
    upper_case_count = 0
    lower_case_count = 0
    for char in sentence:
        if char.isupper():
            upper_case_count += 1
        if char.islower():
            lower_case_count += 1
    return upper_case_count,lower_case_count

input_sentence = "Hello world! 123"
uppers,lowers = count_case_letters(input_sentence)
print("大写字母个数：",uppers)
print("小写字母个数：",lowers)

