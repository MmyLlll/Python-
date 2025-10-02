# 导入logging,random模块
import logging
import random

from Tools.demo.sortvisu import steps

# 一.logging模块
# 1.logging模块的作用
#   1.提供日志功能，可以记录程序运行的日志信息
#   2.可以设置日志的级别，可以控制日志的输出内容

# 2.日志的作用
#   1.用于记录日志信息
#   2.日志的作用：用来程序调试，用来了解软件运行情况是否正常
#   3.软件程序运行故障分析与问题定位

# 3.级别排序（从高到低）
#     CRITICAL》ERROR>WARRING>INFO>DEBUG>NOTEST
# logging.debug('我是debug')
# logging.info('我是info')
# logging.warning('我是warning')
# logging.error('我是error')
# logging.critical('我是critical')

# 4.logging.basicConfig()        配置root logger的参数
#   1. filename：指定日志文件的文件名，所有会显示的日志都会存放到这个文件中。
# logging.basicConfig(filename='log.log')
# logging.debug('我是debug')
# logging.info('我是info')
# logging.warning('我是warning')
# logging.error('我是error')
# logging.critical('我是critical')
#  2.filemode:指定日志文件的打开模式，'w'表示写模式，'a'表示追加模式。默认是a
# logging.basicConfig(filename='log.log',filemode='a')
# logging.debug('我是debug')
# logging.info('我是info')
# logging.warning('我是warning')
# logging.error('我是error')
# logging.critical('我是critical')
#  3.level:指定日志显示级别，默认是警告信息warning
# logging.basicConfig(filename='log.log',filemode='a',level=logging.NOTSET)
# logging.debug('我是debug')
# logging.info('我是info')
# logging.warning('我是warning')
# logging.error('我是error')
# logging.critical('我是critical')
#  4.format:指定之日志信息的输出模式
# logging.basicConfig(filename='log.log',filemode='w',level=logging.NOTSET,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# logging.debug('我是debug')
# logging.info('我是info')
# logging.warning('我是warning')
# logging.error('我是error')
# logging.critical('我是critical')

# 二.rando模块
# random模块的作用：生成随机数
# 1.random.random()：生成0-1之间的随机数
print(random.random())
# 2.random.uniform()          产生指定范围的随机小数
print(random.uniform(1,10))
# 3.random.randint()          产生指定范围的随机整数,包含开头和结尾
print(random.randint(1,10))
# 4.random.randrange(start,stop,[steps])             产生start，stop范围的政府，包含开头和结尾
#   step指产生随机的补偿，随机选择一个数据
print(random.randrange(0,10,2))