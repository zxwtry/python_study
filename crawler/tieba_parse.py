#!/usr/bin/python
#encoding=utf-8
from HTMLParser import HTMLParser
     
html_read=open("tieba_content.txt")
html_str=html_read.readline()
html_read.close()
l20=range(20)
index=[]
for l in l20:
     index.append(html_str.find(str(l+1)+".&#160;"));

print index[4]
#tieba_content=open('tieba_content.txt')
#st=tieba_content.readlines();
#print st
