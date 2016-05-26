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
#从content中解析出前20条帖子
def getTie20(content):
    l20=range(20)
    index=list()
    end=int(20)
    for l in l20:
        index.append(content.find(str(l+1)+".&#160;"));
        if index[l] == -1:
            end = l+1;
            tieend=content.find("</a>",index[l])
            print "tieend:   ",tieend
            tie20.append(content[index[l]:tieend])
    for l in l20:
        print tie20[l]
    print end
    print index[19]

#测试 visitURL
name=raw_input("输入需要访问的贴吧名：")
url_all=visitURL(getBaURL(name))
getTie20(url_all.get("content"))




