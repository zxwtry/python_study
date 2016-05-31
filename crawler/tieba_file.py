#!/usr/bin/python
#encoding=utf-8
import os
import tieba_helper
import tieba_persist


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
        print tie_lous[tie_index]
        tie_str=tie_strs[tie_index]
    for tie_str in tie_strs:
        if len(tie_str) <= 5120 and tie_str[0:5] != "\"1.0\"":
            file_save.write(tie_str+"\n")
            isWriteSuccess=True
    print isWriteSuccess
    file_save.close()
    

"""历史测试
save("wp7","123123123","这个一个测试帖子","我是"*20)
save("wp7","123123123","这个一个测试帖子",["我是dddd","BBB","CCC","DDD"])
"""
