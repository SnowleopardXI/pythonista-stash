# coding: utf-8
"""
Unicode and Chinese Convert Tool
"""
print('Choose your choice:')
n='''
            1:Encode string to Unicode
            2:Decode Unicode to string
'''
c=int(eval(input(n))) #定义菜单变量
if c == 1: #进入菜单1的判断
    print('Type string to be encoded:')
    inp=input()
    out = inp.encode('unicode_escape')
    print(out) # 去掉编码结果前的 b
if c == 2:
    print('Type string to be decoded:')
    inp2=input()
    print(inp2.encode('utf-8').decode('unicode_escape'))