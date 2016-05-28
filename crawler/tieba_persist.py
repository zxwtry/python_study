#!/usr/bin/python
#encoding=utf-8
import pickle
import os

###从硬盘中读取吧的下载楼信息
def readDictLou(ba_name):
    new_dict=dict()
    diclou_path="/home/data/"+ba_name+"/dictlou.info"
    if os.path.exists(diclou_path):
        rf=open(diclou_path,"r")
        new_dict=pickle.load(rf)
        rf.close()
    return new_dict

###将下载楼信息保存到硬盘中
def writeDictLou(ba_name, new_dict):
    diclou_path="/home/data/"+ba_name+"/dictlou.info"
    wf=open(diclou_path,"w")
    pickle.dump(new_dict,wf)
    wf.close()

###吧为ba_name,贴为tie_kw
###返回该贴的最大保存楼
def louOfBaName(ba_name,tie_kw):
    new_dict=readDictLou(ba_name)
    if len(new_dict) == 0:
        return 0 
    if tie_kw in new_dict:
        return new_dict[tie_kw]
    else:
        return 0

