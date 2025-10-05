# 编写一个接受句子并计算字母和数字的程序。假设程序输入:Hello world! 123 则输出应该是:字母10 数字3
def count_letters_and_digits(sentence):
    letters_count = 0
    digits_count = 0
    for char in sentence:
        if char.isdigit():
            digits_count += 1
        if char.isalpha():
            letters_count += 1
    return letters_count,digits_count

input_sentence = "Hello world! 123"
letters,digits = count_letters_and_digits(input_sentence)
print("数字个数：",digits)
print("字母个数：",letters)

