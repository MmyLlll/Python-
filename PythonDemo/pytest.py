print('这是pytest作为模块会显示的内容')
print('pytest')
def test():
    print("嘿嘿嘿")
if __name__  ==  "__main__":
    print('这是pytest自身执行多显示的内容')
    print('pytest2')
    test()

def outer(fn):
    def inner():
        print('这里是装饰器的内层')
        result = fn()
        return result
    return inner

def func():
    print('这里是被装饰的函数')
    return 10
print(outer(func)())

@outer
def func2():
    print('这里是被装饰的函数')
    return 10
print(func2())

#读写操作测试

f = open('test.txt','r+',encoding='utf-8')
print(f.read())
f.write("写入第七行数据")
print(f.read())