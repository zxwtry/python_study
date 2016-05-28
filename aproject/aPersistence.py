#!/usr/bin/python
#encoding=utf-8
import pickle

def saveToDisk():
    dataset=[1,4,2,6,3]
    outputFile="dataset.data"
    fw=open(outputFile,"w")
    pickle.dump(dataset,fw)
    fw.close()

def readFromDisk():
    inputFile="dataset.data"
    fr=open(inputFile,"r")
    dataset=pickle.load(fr)
    fr.close()
    return dataset

#saveToDisk()
print readFromDisk()
