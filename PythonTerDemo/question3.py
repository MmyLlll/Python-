#使用给定的整数n，编写城西生成一个包含（i,ixi）的字典，该字典包含从1到h之间的整数（两者都包含），然后打印字典
def generate_dict(n):
    result_dict = {}
    for i in range(1,n+1):
        result_dict[i] = i*i
    return result_dict
n = int(input("Enteer a number:"))
print(generate_dict(n))
        