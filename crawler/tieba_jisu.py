#!/usr/bin/python
#encoding=utf-8
#贴吧极速版
import urllib
import httplib2

base_url = 'http://tieba.baidu.com/mo/q---1973E7F76569BE76AADDCE7E1592E79C%3AFG%3D1-sz%40320_240%2C-1-3-0--2--wapp_1453584673349_887/m?tn=bdIndex&lp=5014'

#这里是得到某个贴吧的url，如果吧不存在，“xxx吧”尚未建立
def getBaURL(ba_name):
    return "http://tieba.baidu.com/mo/q---1973E7F76569BE76AADDCE7E1592E79C%3AFG%3D1-sz%40320_240%2C-1-3-0--2--wapp_1453584673349_887/m?kw="+ba_name+"&lp=6024"

#现在暂时不考虑cookie，通过url，可以得到(resp, content)
def visitURL(url):
    h=httplib2.Http()
    resp,content=h.request(url)
    return {"resp":resp,"content":content}

#从content中解析出前20条帖子
def getTie20(content):
    tie20=list()
    ref20=list()
    tie20_end=20
    for l in range(20):
        new_index=content.find(str(l+1)+".&#160;");
        if new_index == int(-1):
            tie20_end = l
            break
        else:
            new_end=content.find("</a>",new_index)
            add=8 if l<9 else 9
            tie20.append(content[new_index+add:new_end].replace("&#160;"," ").replace("&quot;"," "))
            ref_start=content.find("<a href=\"m?kz=",new_index-80)
            ref_end=content.find("&",ref_start)
            ref20.append(content[ref_start+14:ref_end])
    return {"tie20":tie20, "ref20":ref20, "tie20_end":tie20_end}

#进入帖子，看楼
def getTieURL(tiekz):
    return "http://tieba.baidu.com/mo/q---1973E7F76569BE76AADDCE7E1592E79C%3AFG%3D1-sz%40320_240%2C-1-3-0--2--wapp_1453584673349_887/m?kz="+tiekz+"&is_bakan=0&lp=5010&pinf=1_2_0"

#将content写入tie_content.txt
def write():
    url_all=visitURL(getTieURL("4546569064"))
    fileWrite = open("tie_content.txt","w")
    fileWrite.write(url_all.get("content"))
    fileWrite.close()

#测试
write()
#name=raw_input("输入需要访问的贴吧名：")
#url_all=visitURL(getBaURL(name))
#tie=getTie20(url_all.get("content"))
#tie20=tie.get("tie20")
#for l in range(int(tie.get("tie20_end"))):
#    print tie20[l]




