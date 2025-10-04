# 编写一个程序，以一系列空格分隔的单词作为输入，并在删除所有重复的单词后，按字母顺序排序后打印这些单词。
# 假设向程序输入: hello world and practice makes perfect and hello world again 则输出为: again and hello makes perfect practice world
def main():
    list = input("请输入一系列空格发分隔的单词:")
    list_words = list.split(' ')
    list_del = set(list_words)
    list_end = sorted(list_del)
    print(list_end)

if __name__ == '__main__':
    main()