#!/usr/bin/python
#coding:utf8
#coding=utf8
#coding:utf8
#encoding=utf8
#_*_ coding:utf8 _*_


def fun09(x, *arg1, **arg2):
    print x
    print arg1
    print arg2
fun09(1,2,3,4,5,u=9)
#fun09(1,2,3,4,5,u=9,6,7,8)


def fun08(x, **args):
    print x
    print args

fun08(x=4,y=5)

def fun07(x, *args):
    print x
    print args
fun07(1)
fun07(2,3)
fun07(2,3,4)

def fun06(name="defName", age=0):
    print "name : %s " %name
    print "age : %d " %age


d = {'age':30, 'name':"Jack"}
fun06(**d)
d['age'] = 31
fun06(**d)

d = {'age':40, 'name':"JackMa",'val':"100"}
#fun06(**d)
#fun06(**d) will cause failure because of 'val'
fun06(d['name'],d['age'])
fun06(age=30, name="millo")

fun06()
fun06("myName", 100)

def fun05(x,y):
    print "%s : %s" %(x, y)

fun05('name1', 'name2') 

t = ('name3', 'name4')
fun05(*t)

def fun04(x=1,y=1):
    print "create ",x, "yuan", y,"ge", "icecream"


fun04(y="KKK")
fun04()
fun04(1,4)
def fun03(x):
    print x

s=raw_input(":");
fun03(s)


def fun02():
    if True:
        print "OK"

fun02()

def fun01():
    if True:
        print "good"

fun01()
