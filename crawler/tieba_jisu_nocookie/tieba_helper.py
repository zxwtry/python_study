#!/usr/bin/python
#encoding=utf-8

def delSpecialChar(st):
    return st.replace("\t","").replace("\n","").replace("\\","").replace(" ","").replace("\T","").replace("\N","").replace("\b","").replace("\B","").replace("/","")
def getTieFilePath(base_dir, tie_kw, tie_name):
    return base_dir+"/"+delSpecialChar(tie_kw)+"_"+delSpecialChar(tie_name)
def getHomeDir():
    return "/home/data/"
def getBaseDir(ba_name):
    return getHomeDir()+delSpecialChar(ba_name)
def getDictLouInfoPath(ba_name):
    return getBaseDir(ba_name)+"/dictlou.info"
def getImageDir():
    return getHomeDir()+"images/"
    

