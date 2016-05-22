#!usr/bin/python

#range, xrange
#xrange is much more efficent than range
xobj = xrange(10)
print "xobj:\t",xobj

#cmp
str1 = "abc"
str2 = "a"
print "cmp(str1, str2): \t", cmp(str1,str2)
print "cmp(str1, str1): \t", cmp(str1,str1)


l=range(1,5)
print "isinstance(l,list): \t",isinstance(l,list)
print "isinstance(l,tuple): \t",isinstance(l,tuple)
print "isinstance(l,int): \t",isinstance(l,int)


l=range(0,100,2)
if type(l) == type([]):
    print "Same Type"
else:
    print "Diff Type"
#print "type(l): ",type(l)
#print "type([]): ",type([])

#callable() means if the funtion is modified
print callable(min)
f=0
print "callable(f=0): ",callable(f)
def f():
    pass
print "callable(f function): ",callable(f)
l = range(1,100)
print "max: ", max(l)
print "min: ", min(l)
print "len: ", len(l)
print "divmod(100,17): ", divmod(100,17)
print "pow(2,7): ", pow(2,7)
print "pow(2,7,3): ", pow(2,7,3)
print "pow(2,7,5): ", pow(2,7,5)
print "round(5): ", round(5)
print "round(4.3): ", round(4.3)
print "round(4.7): ", round(4.7)
print "round(4.5): ", round(4.5)
print(abs(-19990))
def my_abs(x):
    if x < 0:
        return -x
    else:
        return x
print my_abs(10)
