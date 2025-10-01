import re
from re import split

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
# res = re.match(r'<(?P<L1>\w*)>\w*</(?P=L1)>','<html>login</html>')
# print(res.group())

# 二.高级用法
# 1.search（）：扫描整个字符串并返回一个成功匹配的对象，如果没有匹配成功，则返回None。
# res = re.search('tho','python')
# print(res.group())

# 2.findall()：扫描整个字符串并返回所有成功匹配的对象组成的列表。
# res = re.findall('th','python,th')
# print(res)
# print(type(res))

# 总结：match（）从头开始匹配，匹配成功返回match对象，通过group（）提取，匹配失败返回None，只匹配一次
#      search（）：从头到尾，匹配成功晚会返回第一个成功匹配的对象，通过group（）提取，匹配失败返回None，只匹配一次
#      findall()：从头到尾，匹配成功返回一个列表，匹配所有成功的数据，而且不需要通过group（）方法提取

# 3.sub(pattern,repl,string,count)：替换字符串中的匹配项，第一个参数为匹配的正则表达式，第二个参数为替换的字符串，第三个参数为要替换的字符串。
#     pattern：正则表达式（代表需要被替代的，也就是字符串里面的内容）
#     repl：新内容
#     string：字符串
#     count：指定替换的次数，如果不指定，则全部替换。
# res = re.sub('th','TH','python,th',1)
# print(res)

# 4.split(pattern,string,maxsplit)
# pattern：正则表达式（代表需要被替代的，也就是字符串里面的内容）
# string :字符串
# maxsplit:指定最大分割次数#     repl：新内容
# res = re.split(',','python,th,is,a,good,day')
# print(res)

# 三.贪婪与非贪婪匹配
# 1.贪婪匹配：正则表达式默认是贪婪匹配，也就是尽可能多的匹配字符。
# res = re.match('py.*','python123')
# print(res.group())
# 2.非贪婪匹配：在正则表达式中，加上？，表示该分组为非贪婪匹配，也就是尽可能少的匹配字符。
# ress = re.match('py..+?','python123')
# print(ress.group())

# 四.原生字符串
# 1.原生字符串：在字符串前面加上r，表示原生字符串，不进行转义。
print(r"pro\tnt")
res = re.match(r"pro\tnt","pro\tnt")
print(res.group())