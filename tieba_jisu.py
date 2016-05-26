#!/usr/bin/python
#encoding=utf-8
#贴吧极速版
import urllib
import httplib2

base_url = 'http://tieba.baidu.com/mo/q---1973E7F76569BE76AADDCE7E1592E79C%3AFG%3D1-sz%40320_240%2C-1-3-0--2--wapp_1453584673349_887/m?tn=bdIndex&lp=5014'

#这里是得到某个贴吧的url，如果吧不存在，“xxx吧”尚未建立
ba_url_0="http://tieba.baidu.com/mo/q---1973E7F76569BE76AADDCE7E1592E79C%3AFG%3D1-sz%40320_240%2C-1-3-0--2--wapp_1453584673349_887/m?kw="
ba_url_1="i&lp=1041"
def getBaURL(ba_name):
    return ba_url_0+ba_name+ba_url_1

#现在暂时不考虑cookie，通过url，可以得到(resp, content)
def visitURL(url):
    h=httplib2.http()
    resp,content=h.request(url)
    return ["resp":resp,"content":content]
#获取HTTP对象
h=httplib2.Http()
#发出同步请求，并获取内容
resp,content=h.request(base_url)
print resp
print "="*30
print content

