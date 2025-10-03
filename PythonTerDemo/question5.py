# 定义一个至少有两个方法的类:-、geSting:从控制台输入获取字符串;二、printSting:打印大写母的学符事，并写出简单的测试函数来测试类方法。
class StringProcesser:
    def getString(self):
        self.input_string = input("请输入一个包含大小写的字符串：")
    def printString(self):
        if not hasattr(self,'input_string'):
            print("没有获取到字符串，请先调用getString()方法获取输入字符串")
            return
        uppercase_letters = [char for char in self.input_string if char.isupper()]
        print("大写字母："," ".join(uppercase_letters))
        print(self)

def test_string_processer():
    processer = StringProcesser()
    processer.getString()
    processer.printString()
    print(processer)

test_string_processer()
