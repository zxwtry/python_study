#!/usr/bin/python

#t = (1,2)

#def fun02(int x, int y):
#    print x, y
#fun02(t)



a = 100
b = "I am global var b"

def fun01():
    a = 99
    print "local position : a=" + str(a)
    global y
    y = 123
    global b
    b =23

print "before fun01 : b=" + str(b)

fun01()
print "global position : a=" + str(a)
print "glocal def in fun01 : y=" + str(y)

print "after fun01 : b="+str(b)

