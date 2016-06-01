#!/usr/bin/python
#encoding=utf-8
#贴吧极速版
import urllib
import httplib2
import tieba_parse
import time
import tieba_file
import random

base_url = 'http://tieba.baidu.com/mo/q---1973E7F76569BE76AADDCE7E1592E79C%3AFG%3D1-sz%40320_240%2C-1-3-0--2--wapp_1453584673349_887/m?tn=bdIndex&lp=5014'

#这里是得到某个贴吧的url，如果吧不存在，“xxx吧”尚未建立
def getBaURL(ba_name):
    return "http://tieba.baidu.com/mo/q---1973E7F76569BE76AADDCE7E1592E79C%3AFG%3D1-sz%40320_240%2C-1-3-0--2--wapp_1453584673349_887/m?kw="+ba_name+"&lp=6024"

#现在暂时不考虑cookie，通过url，可以得到(resp, content)
def visitURL(url):
    h=httplib2.Http()
    resp,content=h.request(url)
    return {"resp":resp,"content":content}

#进入帖子，看楼
def getTieURL(tiekz):
    return "http://tieba.baidu.com/mo/q---1973E7F76569BE76AADDCE7E1592E79C%3AFG%3D1-sz%40320_240%2C-1-3-0--2--wapp_1453584673349_887/m?kz="+tiekz+"&is_bakan=0&lp=5010&pinf=1_2_0"

#将content写入tie_content.txt
def write():
    url_all=visitURL(getTieURL("4327492443"))
    fileWrite = open("ba_content.txt","w")
    fileWrite.write(url_all.get("content"))
    fileWrite.close()

def getURLOfYe(page_now,tiekz):
    return "http://tieba.baidu.com/mo/q---1973E7F76569BE76AADDCE7E1592E79C%3AFG%3D1-sz%40320_240%2C-1-3-0--2--wapp_1453584673349_887/m?kz="+tiekz+"&new_word=&pinf=1_2_0&pn="+str(page_now*30)+"&lp=6021"

def visitAllYes(tiekz,page_now, page_all):
    for page_here in range(page_all-1):
        urlYe=getURLOfYe(page_here+1,tiekz)
        tie_all=visitURL(urlYe)
        msg=tieba_parse.getMsgFromContent(tie_all.get("content"))
        tieba_file.save(ba_name,ref20[l],tie20[l],msg.get("tie_strs"),msg.get("tie_lous"))
        for tie_str in msg.get("tie_strs"):
            if len(tie_str) <= 5120 and tie_str[0:5] != "\"1.0\"":
                print tie_str
        print "page_now:\t\t",msg.get("page_now")
        print "page_all:\t\t",msg.get("page_all")
        time.sleep(random.randint(3,9))


#测试
#url_all=visitURL(getTieURL("4554428746"))
#url_all=visitURL(getTieURL("4572569332"))
#msg=tieba_parse.getMsgFromContent(url_all.get("content"))
#print msg.get("page_now")
#print msg.get("page_all")
#print msg.get("tie_imgs")


###访问一个贴吧，得到首页的帖子
while(True):
    ba_name="wp7"
    url_all=visitURL(getBaURL(ba_name))
    tie=tieba_parse.getTie20(url_all.get("content"))
    tie20=tie.get("tie20")
    ref20=tie.get("ref20")
    for l in range(int(tie.get("tie20_end"))):
        print "帖子标题：\t\t",tie20[l]
        tie_all=visitURL(getTieURL(ref20[l]))
        msg=tieba_parse.getMsgFromContent(tie_all.get("content"))
        tieba_file.save(ba_name,ref20[l],tie20[l],msg.get("tie_strs"),msg.get("tie_lous"))
        for tie_str in msg.get("tie_strs"):
            if len(tie_str) <= 5120 and tie_str[0:5] != "\"1.0\"":
                print tie_str
        print "page_now:\t\t",msg.get("page_now")
        print "page_all:\t\t",msg.get("page_all")
        visitAllYes(ref20[l],msg["page_now"],msg["page_all"])
        time.sleep(random.randint(3,9))
    time.sleep(random.randint(100,300))


