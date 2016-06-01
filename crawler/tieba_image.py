#!/usr/bin/python
#encoding=utf-8
import urllib

def downloadAnImageFromURL(url):
    urllib.urlretrieve(url,"/home/a.jpg")
