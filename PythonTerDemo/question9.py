#编写一个程序，接收一行序列作为输入，并在将句子中的所有字符大写后打印行。
def main():
    list = input("请输入一行序列：")
    list_end = list.upper()
    print(list_end)
if __name__ == '__main__':
    main()