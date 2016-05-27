#!/usr/bin/python
#encoding=utf-8
import os
def save(ba_name, tie_name, tie_strs):
    base_dir="/home/data/"+ba_name
    if not  os.path.exists(base_dir):
        os.makedirs(base_dir)
        print "创建目录"
    file_save=open(base_dir+"/"+tie_name,"a")
    file_save.write(tie_strs)
    file_save.close()
save("显卡","123123","aabb"*20)
