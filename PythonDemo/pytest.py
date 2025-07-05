print('这是pytest作为模块会显示的内容')
print('pytest')
def test():
    print("嘿嘿嘿")
if __name__  ==  "__main__":
    print('这是pytest自身执行多显示的内容')
    print('pytest2')
test()

import pack_01
from pack_01 import *
register.reg()