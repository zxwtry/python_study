#!/usr/bin/python
#encoding=utf-8
import pickle
import os
import tieba_helper

###从硬盘中读取吧的下载楼信息
def readDictLou(ba_name):
    new_dict=dict()
    diclou_path=tieba_helper.getDictLouInfoPath(ba_name)
    if os.path.exists(diclou_path):
        rf=open(diclou_path,"r")
        new_dict=pickle.load(rf)
        rf.close()
    return new_dict

###将下载楼信息保存到硬盘中
def writeDictLou(ba_name, new_dict):
    diclou_baseDir=tieba_helper.getBaseDir(ba_name)
    diclou_path=tieba_helper.getDictLouInfoPath(ba_name)
    if not os.path.exists(diclou_baseDir):
        os.makedirs(diclou_baseDir)
    wf=open(diclou_path,"w")
    pickle.dump(new_dict,wf)
    wf.close()
#writeDictLou("wp7",{"123":123,"233":233})

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

def persistTiesOnepage():
    return 0    
    
