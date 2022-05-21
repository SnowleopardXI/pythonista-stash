# -*- coding: utf-8 -*-
import base64

print('Choose your choice:')
n='''
            1:Encode string to base64
            2:Decode base64 to string
'''
c=int(eval(input(n))) #定义菜单变量
if c == 1: #进入菜单1的判断
    print('Type string to be encoded:')
    inp=input()
    out = str(base64.encodebytes(inp.encode("utf-8")), "utf-8")
    print(out) # 去掉编码结果前的 b
if c == 2:
    print('Type string to be decoded:')
    inp2=bytes(input(),('utf-8'))
    dec = base64.decodebytes(inp2)
    print(dec.decode())
