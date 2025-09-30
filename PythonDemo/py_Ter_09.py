import re
# 一.匹配分组
# 1. | 匹配左右任意一个表达式         --常用
# res = re.match('abc|def','def')
# print(res.group())

# 2.(ab)将括号中字符作为一个分组              --常用
# res = re.match('\w*@(163|qq|126|789).com','123456@qq.com')
# print(res.group())

# 3.\num匹配分组num匹配带的字符串                --经常在匹配标签时被使用
# res = re.match('<(\w*)>\w*</\\1>','<html>login</html>')
# print(res.group())

# 4.(?P<name>)   分组起别名
# 5.（？p=name）   引用别名为那么分组匹配到的字符串
res = re.match(r'<(?P<L1>\w*)>\w*</(?P=L1)>','<html>login</html>')
print(res.group())