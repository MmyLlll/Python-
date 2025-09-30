import re
# 1.正则表达式
# 一.字符串处理工具
# 注意：需要导入re模块
# 1.2 特点：
#         语法比较负责，可读性较差
#         通用性很强，使用于多种编程语言

# 1.3 步骤：
#         1.导入re模块
#         2.使用match()进行匹配操作
#           re.match()能匹配出以XXX开头的字符串
#             如果起始位置没有匹配成功，返回None
# re.match(pattern,string,flags)
#         pattern:匹配的正则表达式
#         string：要匹配的字符串
# res = re.match("第",'第二个校色huahua')
# print(res)
# #         3.如果上一步数据匹配成功，使用group（）提取数据
# print(res.group())
#注意：match是从开始位置匹配，匹配不到就没有

# 二、匹配单个字符
# 1.’.‘匹配任意一个字符，除\n以外        --常用
# res = re.match(".","hello")
# print(res.group())
# # 2.[]匹配[]中列举的字符，匹配一个字符                     --常用
# ress = re.match('[he]',"ello")
# print(ress.group())
# 3./d匹配数字   --常用
# resss = re.match('\d','5243')
# print(resss.group())
# 4.匹配非数字                 --常用
# ressss = re.match('\D','xaxas')             #只要不是数字都可以匹配
# print(ressss.group())
# 5. \s,匹配空格空白
# res = re.match('\s.....','  hello')
# print(res.group())
# 6.\S,匹配非空白
# res = re.match('\S','xa')
# print(res.group())
# 7.\w,匹配单词字符，即a-z，A-Z，0-9，汉字             --常用
# res = re.match('\w',"花花uahua")
# print(res.group())
# 8.\W匹配非单词字符
# res = re.match('\W','..')
# print(res.group())

# 三.匹配多个字符
# 1.*匹配前一个字符出现0次或者无限次，即可有可无                   --常用
# res = re.match('\d*',"123456")
# print(res.group())
# 2.+匹配前一个字符出现1次或者无限次，至少一次                     --常用
# res = re.match('\d+',"123地主家的傻儿子")
# print(res.group())
# 3.？匹配前一个字符出现一次或者0次，即1次或者0次                  --常用
# res = re.match('\d?','123hello')
# print(res.group())
# 4.{m}匹配前一个字符出现m次
# res = re.match('\w{5}',"python")
# print(res.group())
# 5.{m，n}匹配前一个字符出现从m次到n次
# 注意必须符合m<n
# res = re.match('\w{1,3}','00hello')
# # print(res.group())

# 四.匹配开头和结尾
# 1.^：匹配以某字符串开头，表示对...取反
# res = re.match('^py','python')
# print(res.group())
# # 注意：^在[]中表示不存在
# ress = re.match('[^py]','thon')         #[^py]表示匹配py之外的字符
# print(ress.group())
# 2.$匹配以某个字符串结尾
res = re.match('.*n$','python')
print(res.group())