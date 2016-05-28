#!/usr/bin/python
#encoding=utf-8
from HTMLParser import HTMLParser
import httplib2
import re

#从content中解析出前20条帖子，这里是访问吧得到帖子
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
    pagenum_start=content.find("</a><br/>第");
    pagenum_end=content.find("页",pagenum_start+2)
    if (pagenum_start==-1):
        page_now=1
        page_all=1
    else:
        pagenum_list=content[pagenum_start+12:pagenum_end].split("/")
        page_now=int(pagenum_list[0])
        page_all=int(pagenum_list[1])
    msg=dict()
    msg["page_now"]=page_now
    msg["page_all"]=page_all
    tie_strs=list()
    tie_imgs=list()
    tie_lous=list()
    for l in match:
        tie_start=content.find("<div class=\"i\">"+str(l)+"楼.")
        tie_end=content.find("<br/>",tie_start)
        words=getWords(content[tie_start+15:tie_end],tie_imgs)
        tie_str_withlou=words.get("tie_str") 
        tie_strs.append(tie_str_withlou)
        lou_end=tie_str_withlou.find("楼")
        if lou_end == -1:
            tie_lous.append(1)
        else:
            lou_num_str=tie_str_withlou[0:lou_end]
            tie_lous.append(int(lou_num_str))
        ##print getWords(content[tie_start+15:tie_end]).get("tie_str")
    msg["tie_strs"]=tie_strs
    msg["tie_imgs"]=tie_imgs
    msg["tie_lous"]=tie_lous
    return msg

###这里是tieba_jisu.py调用的版本
#content_read=open("ba_content.txt","r")
#content=content_read.readline()
#msg=getMsgFromContent(content)
#print msg.get("page_now")
#print msg.get("page_all")
#tie_strs=msg.get("tie_strs")
#for tie_str in tie_strs:
#    print tie_str
#print msg.get("tie_imgs")



###老版本，看着用     
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
