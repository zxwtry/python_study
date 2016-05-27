#!/usr/bin/python
#encoding=utf-8
from HTMLParser import HTMLParser
import httplib2
import re

#处理帖内容，主要是消除图片链接
def getWords(tie_str,imgs):
    tie_str=tie_str.replace("&#160;"," ")
    times = int(1)
    while (1):
        times=times+1;
        if(times>=100):
            break
        le_st=tie_str.find("<")
        le_en=tie_str.find(">")
        if le_st == -1:
            break
        img_tmp=tie_str[le_st:le_en+1]
        img_start=img_tmp.find("src=http")
        if (img_start!=-1):
            img_end=img_tmp.find(".jpg",img_start)
            if (img_end!=-1):
                imgs.append(img_tmp[img_start+4:img_end+4].replace("%3A",":").replace("%2F","/"))
        tie_str=tie_str.replace(img_tmp,"")
    return {"tie_str":tie_str}

###从一个Content解析Msg
def getMsgFromContent(content):
    match=re.findall(ur"<div class=\"i\">([\\u4e00-\\u9fa5]*)",content)
    pagenum_start=content.find("一页</a><br/>第");
    pagenum_end=content.find("页",pagenum_start+5)
    pagenum_list=content[pagenum_start+18:pagenum_end].split("/")
    page_now=int(pagenum_list[0])
    page_all=int(pagenum_list[1])
    msg=dict()
    msg["page_now"]=page_now
    msg["page_all"]=page_all
    tie_strs=list()
    tie_imgs=list()
    for l in match:
        tie_start=content.find("<div class=\"i\">"+str(l)+"楼.")
        tie_end=content.find("<br/>",tie_start)
        words=getWords(content[tie_start+15:tie_end],tie_imgs)
        tie_strs.append(words.get("tie_str"))
        ##print getWords(content[tie_start+15:tie_end]).get("tie_str")
    msg["tie_strs"]=tie_strs
    msg["tie_imgs"]=tie_imgs
    return msg

###测试
content_read=open("ba_content.txt","r")
content=content_read.readline()
msg=getMsgFromContent(content)
print msg.get("page_now")
print msg.get("page_all")
tie_strs=msg.get("tie_strs")
for tie_str in tie_strs:
    print tie_str
print msg.get("tie_imgs")

###解析一个吧的数据     
#html_read=open("tieba_content.txt")

#html_str=html_read.readline()
#html_read.close()
#l20=range(20)
#index=list()
#end=int(20)
#for l in l20:
#    index.append(html_str.find(str(l+1)+".&#160;"));
#    if index[l] == -1:
#        end = l+1;
#print end
#print index[19]
#tieba_content=open('tieba_content.txt')
#st=tieba_content.readlines();
#print st
