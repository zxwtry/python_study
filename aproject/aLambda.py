#!/usr/bin/python
a=int(raw_input("input the num to cal :"))
l=range(1,a)
sum=reduce(lambda x,y:x*y,l)
print(sum)
l=range(1,9)
sum=reduce(lambda x,y:x*y,l)
print(sum)
sum=reduce(lambda x,y:x+y,(4,7,9))
print(sum)
def f(n):
    if n == 1:
        return 1
    return n*f(n-1)
print(f(4))
def myadd(x,y):
    return x+y
sum=reduce(myadd,(1,2,3))
print(sum)
g1=lambda x:x**3
print(g1(6))
def f(x, y):
    return x*y
g=lambda x,y:x*y
print(f(2,3))
print(g(2,3))
