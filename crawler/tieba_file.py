#!/usr/bin/python
#encoding=utf-8
import os

def getTieFilePath(base_dir, tie_kw, tie_name):
    return base_dir+"/"+tie_kw+"_"+tie_name
def getBaseDir(ba_name):
    return "/home/data/"+ba_name


"""
ba_name:  吧的名字，会在/home/data/创建一个ba_name文件夹
tie_name: 贴的标题
tie_strs: 需要append的一个list()
""" 
def save(ba_name, tie_kw, tie_name, tie_strs, tie_lous):
    base_dir=getBaseDir(ba_name)
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
        print "创建目录"
    file_save=open(getTieFilePath(base_dir,tie_kw,tie_name),"a")
    for tie_str in tie_strs:
        file_save.write(tie_str+"\n")
    file_save.close()

"""历史测试
save("wp7","123123123","这个一个测试帖子","我是"*20)
save("wp7","123123123","这个一个测试帖子",["我是dddd","BBB","CCC","DDD"])
"""
