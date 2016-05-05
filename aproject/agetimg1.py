# -*- coding:utf-8 -*-
import re
import urllib

def getHtml(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html

def getImg(html):
	reg = r'<img src="http://ww(.+?\.jpg)" />'
	imgre = re.compile(reg)
	imglist = re.findall(imgre,html)
	x = 0
	for imgurl in imglist:
		urllib.urlretrieve("http://ww"+imgurl,str(x)+".jpg")
		x+=1
	print(str(x)+" : "+"http://ww"+imgurl);

html = getHtml("http://www.lkong.net/thread-1464340-1-1.html")

print getImg(html)
