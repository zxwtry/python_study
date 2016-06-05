#/usr/bin/python
#coding:utf-8
from __future__ import division
k=1
v=2
operator='/'
result={
    '+':k+v,
    '-':k-v,
    '*':k*v,
    '/':k/v
}
print result
print "result: ", result.get(operator)
def add(x,y):
    return x+y
def minus(x,y):
    return x-y
def multi(x,y):
    return x*y
def div(x,y):
    return x/y
print "multi: ",multi
multi=5
operator={'+':add,'-':minus,'*':multi,'/':div}
print "operator.get: ",operator.get('*')
print (lambda x,o,y:operator.get(o)(x,y))(2,'+',3)
#print operator['/'](2,3)
#print operator.get('/')(2,3)
def operSwitch(x,o,y):
    print operator.get(o)(x,y)    
operSwitch(3,'+',4)
operSwitch(3,'/',4)
#operSwitch(3,'&',4)
#noneerror
def operator(x,o,y):
    if o=='+':
        print(add(x,y))
    elif o=='-':
        print(minus(x,y))
    elif o=='*':
        print(multi(x,y))
    elif o=='/':
        print(div(x,y))
    else:
        print("bad operator")
x=int(raw_input("x:"))
o=raw_input("operator:")
y=int(raw_input("y:"))
operator(x,o,y)
print(5/2)
#2.5

