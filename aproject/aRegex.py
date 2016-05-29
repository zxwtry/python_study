#!/usr/bin/python
#!encoding=utf-8
#元字符
#. ^ $ * + ? {} [] \ | ()
#大部分字母和字符一般都会和自身匹配
#

import re
s=r"[0-9]+"
st="a122bb3dc9d7"
ans=re.findall(s,st)
print ans[0]

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

#\d [0-9]
#\D [^0-9]
#\s 匹配任何空白字符 [\t\n\r\f\v]
#\S 匹配任何非空字符 [^\t\n\r\f\v]
#\w 匹配任何字母数字字符 [a-zA-Z0-9_]
#\W 匹配任何非字母数字字符 [^a-zA-Z0-9_]
#\  可用于取消所有的元字符：\[ 或　\\

st="010-12345678"
s=r"^010-\d{8}"
print re.findall(s,st)

#* 表示重复 0次就是没有
s=r"ab*"
print re.findall(s ,"a")
print re.findall(s ,"ab")
print re.findall(s ,"abababababab")

#+ 表示重复　至少出现一次
s=r"ab+"
print re.findall(s ,"a")
print re.findall(s ,"ab")
print re.findall(s ,"abababababab")

#? 表示重复　出现一次或0次
s=r"ab?"
print re.findall(s ,"a")
print re.findall(s ,"ab")
print re.findall(s ,"abababababab")

#{m,n} 表示重复　至少m  至多n
#{0,} *
#{1,} +
#{0,1} ? 
s=r"ab?"
print re.findall(s ,"a")
print re.findall(s ,"ab")
print re.findall(s ,"abababababab")

#编译正则表达式
r = r"\d{3,4}-?\d{8}"
print re.findall(r, "010-12345678")
p_tel = re.compile(r);
print p_tel.findall("010-12345678");

#不匹配大小写 re.IGNORECASE
csvt_re = re.compile(r'csvt',re.I)
print csvt_re.findall("CSVT");

#反斜杠的麻烦
#字符串前加"r"反斜杠就不会被任何特殊方式处理
#\section       要匹配的字符串
#\\section      为re.compile取消反斜杠的特殊意义
#\\\\section    为"\\section"的字符串实值(String literals)取消反斜杠的特殊意义

print  "re.findall(r\"\\taab\",\"\\taab\") : \t", re.findall(r"\taab","\taab")
print  "re.findall(\"\\taab\",\"\\taab\") : \t", re.findall("\taab","\taab")

print  "re.findall(r\"\\taab\",r\"\\taab\") : \t", re.findall(r"\taab",r"\taab")
print  "re.findall(\"\\taab\",r\"\\taab\") : \t\t", re.findall("\taab",r"\taab")

print  "re.findall(r\"\\taab\",r\"\\taab\") : \t", re.findall(r"\taab",r"aab")
print  "re.findall(\"\\taab\",r\"\\taab\") : \t\t", re.findall("\taab",r"\taab")

r_b=r"\paab"
r_B="\paab"
print "re.findall(r_b,\"\paab\") : ", re.findall(r_b,"\paab")
print "re.findall(r_B,\"\paab\") : ", re.findall(r_B,"\paab")



