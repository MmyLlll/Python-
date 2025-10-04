# 编写一个程序，以逗号分隔的单词序列作为输入，按照字母顺序对每个单词进行排序，并通过逗号分隔的序列来打印单词。
# 假设向程序输入:without,hello,bag,world;则输出为:bag,hello,without,world;
def sort_words(input_string):
    words = input_string.split(",")
    words.sort()
    sorted_string = ','.join(words)
    return sorted_string

input_string = "without,hello,bag,world"
list = sort_words(input_string)
print(list)