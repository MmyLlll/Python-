# 导入os，sys模块
import os
import sys
# 一.os模块
# 作用：操作系统接口，可以执行系统命令、创建、删除文件、目录等。
# 1.os.name   只是正在使用的工作平台（返回操作系统类型）
print(os.name)
# 对于window，返回nt，对于Linux，返回posix

# 2.os.getenv(h环境变量名称)       读取环境变量
print(os.getenv('PATH'))

# 3.os.path.split()             把目录名和文件名分离，以元组的形式接受，第一个元素是目录路径，第二个元素是文件名字
print(os.path.split('C:\\Users\\Administrator\\Desktop\\test.txt'))
o = os.path.split('C:\\Users\\Administrator\\Desktop\\test.txt')
print(o[0])
print(o[1])
print(type(o))

# 4.os.path.dirname()         显示split分割的第一个元素，即目录
# 5.os.pathbasename()         显示split分割的第二个元素，即文件名
print(os.path.dirname('C:\\Users\\Administrator\\Desktop\\test.txt'))
print(os.path.basename('C:\\Users\\Administrator\\Desktop\\test.txt'))

# 6.os.path.exists()            判断路径（文件或者目录是否存在），存在返回true不存在返回false
print(os.path.exists('C:\\Users\\Administrator\\Desktop\\test.txt'))

# 7.os.path.isfile()             判断是否存在文件
# 8.os.path.isdir()              判断是否存在目录

# 9.os.path.abspath()     获取当前路径下的绝对路径
print(os.path.abspath(r'D:\WDM'))

# 10.os.path.isabs()      判断当前路径是否是绝对路径
print(os.path.isabs(r'D:\WDM\管理学'))


# 二.sys模块
# 作用：负责程序跟python解释器的交互
# 1.sys.getdefaultencoding()         获取系统默认的编码格式
print(sys.getdefaultencoding())

# 2.sys.path       获取换环境变量的路径，跟解释器相关,以列表形式返回
print(sys.path[0])
print(type(sys.path))

# 3.sys.platform              获取操作系统平台名称
print(sys.platform)

# 4.sys.version           获取python解释器的版本信息
print(sys.version)