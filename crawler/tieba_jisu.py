#!/usr/bin/python
#encoding=utf-8
#贴吧极速版
import urllib
import httplib2

base_url = 'http://tieba.baidu.com/mo/q---1973E7F76569BE76AADDCE7E1592E79C%3AFG%3D1-sz%40320_240%2C-1-3-0--2--wapp_1453584673349_887/m?tn=bdIndex&lp=5014'

#这里是得到某个贴吧的url，如果吧不存在，“xxx吧”尚未建立
ba_url_0="http://tieba.baidu.com/mo/q---1973E7F76569BE76AADDCE7E1592E79C%3AFG%3D1-sz%40320_240%2C-1-3-0--2--wapp_1453584673349_887/m?kw="
#ba_url_1="i&lp=1041"
ba_url_1="&lp=6024"
def getBaURL(ba_name):
    return ba_url_0+ba_name+ba_url_1

#现在暂时不考虑cookie，通过url，可以得到(resp, content)
def visitURL(url):
    h=httplib2.Http()
    resp,content=h.request(url)
    return {"resp":resp,"content":content}

tie20=list()
ref20=list()
tie20_end=20
#从content中解析出前20条帖子
def getTie20(content):
    tie20_end=20
    for l in range(20):
        new_index=content.find(str(l+1)+".&#160;");
        if new_index == int(-1):
            tie20_end = l
            break
        else:
            new_end=content.find("</a>",new_index)
            add=8 if l<9 else 9
            tie20.append(content[new_index+add:new_end].replace("&#160;"," "))
            ref_start=content.find("<a href=\"m?kz=",new_index-80)
            ref_end=content.find("&",ref_start)
            ref20.append(content[ref_start:ref_end])
    l20=range(tie20_end)
    for l in l20:
        print tie20[l]
    for l in l20:
        print ref20[l]

#测试
name=raw_input("输入需要访问的贴吧名：")
url_all=visitURL(getBaURL(name))
getTie20(url_all.get("content"))




