#!/usr/bin/python
#encoding=utf-8
from HTMLParser import HTMLParser
     
html_read=open("tieba_content.txt")
html_str=html_read.readline()
html_read.close()
l20=range(20)
index=list()
end=int(20)
for l in l20:
    index.append(html_str.find(str(l+1)+".&#160;"));
    if index[l] == -1:
        end = l+1;
print end
print index[19]
#tieba_content=open('tieba_content.txt')
#st=tieba_content.readlines();
#print st
