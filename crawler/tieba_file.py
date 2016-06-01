#!/usr/bin/python
#encoding=utf-8
import os
import tieba_helper
import tieba_persist
import re
import time

"""
ba_name:  吧的名字，会在/home/data/创建一个ba_name文件夹
tie_name: 贴的标题
tie_strs: 需要append的一个list()
""" 
def save(ba_name, tie_kw, tie_name, tie_strs, tie_lous):
    base_dir=tieba_helper.getBaseDir(ba_name)
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
        print "创建目录"
    if tie_kw == "" or tie_name == "" or tie_kw == "_" or tie_name == "+":
        return
    oldLous=tieba_persist.louOfBaName(ba_name,tie_kw)
    file_save=open(tieba_helper.getTieFilePath(base_dir,tie_kw,tie_name),"a")
    isWriteSuccess=False
    for tie_index in range(len(tie_strs)):
        tie_str=tie_strs[tie_index]
        if len(tie_str) <= 5120 and tie_str[0:5] != "\"1.0\"" and tie_lous[tie_index] > oldLous:
            file_save.write(tie_str+"\n")
            isWriteSuccess=True
            oldLous=tie_lous[tie_index]
    if isWriteSuccess:
        dict_lou=tieba_persist.readDictLou(ba_name)
        dict_lou[tie_kw]=oldLous
        tieba_persist.writeDictLou(ba_name,dict_lou)
    file_save.close()
    
def downloadImages(tie_imgs):
    base_img_path=str(tieba_helper.getImageDir())
    print type(base_img_path)
    if not os.path.exists(base_img_path):
        os.makedirs(base_img_path)
    for tie_img in tie_imgs:
        img_path=str(tieba_helper.getImageDir())+downloadImageName(tie_img)
        print img_path 

def downloadImageName(tie_img):
    if len(tie_img) < 10:
        return ""
    res=r"[0-9a-z]*.jpg$"
    imageName = str(re.findall(res,tie_img))
    if len(imageName) < 5:
        return str(time.time())+".jpg"
    else:
        return imageName

downloadImages(["http://imgsrc.baidu.com/forum/w%3D580/sign=e9f69adf2af5e0feee1889096c6234e5/0a672a2442a7d933d17c71b5aa4bd11371f00177.jpg"])


"""历史测试
save("wp7","123123123","这个一个测试帖子","我是"*20)
save("wp7","123123123","这个一个测试帖子",["我是dddd","BBB","CCC","DDD"])
"""
