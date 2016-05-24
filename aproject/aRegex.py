#!/usr/bin/python
#!encoding=utf-8
#元字符
#. ^ $ * + ? {} [] \ | ()
#大部分字母和字符一般都会和自身匹配
#

import re
s=r'abc'
print re.findall(s,"ababc")
st = "top tip tqp tcp tep tvp"
s=r"top"
print re.findall(s,st)
s=r"t[oi]p"
print re.findall(s,st)
s=r"t[^oi]p"
print re.findall(s,st)
s=r"hello"
print re.findall(s,"bbhelloaahellopp")
s=r"^hello"
print re.findall(s,"bbhelloaahellopp")
s=r"^bbhello"
print re.findall(s,"bbhelloaahellopp")
s=r"opp$"
print re.findall(s,"bbhelloaahellopp")
