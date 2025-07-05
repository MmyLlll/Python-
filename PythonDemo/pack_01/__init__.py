print('这是_init_.py文件')
from pack_01 import register                #导入这个包的其他模块
register.reg()
__all__ = ['register']