#!usr/bin/python
#!encoding=utf-8

#序列处理函数：filter zip map reduce
print "[x for x in range(20) if x % 3 == 0]:\t",  [x for x in range(20) if x % 3 == 0]
print "reduce(lambda x,y:x+y,range(101)): \t", reduce(lambda x,y:x+y,range(101))
l=range(101)
n=0
for i in l:
   n+=i
print n 
a=[1,2,3]
b=[2,4,6]
def fm(x,y):
    return x*y
print map(fm,a,b)
name=['name1','name2','name3']
age=[11,12,13]
tel=[131,132,133]
print zip(name,age,tel)
print map(None,name,age,tel)
def f(x):
    if x>5:
        return True
    else:
        return False
l = range(10)
print filter(f,l)


print "\"192.168.1.123\".split('.') return list :\t", "192.168.1.123".split('.')
print "\"192.168.1.123\".split('.',1) return list :\t", "192.168.1.123".split('.',1)
#('a',"A"):两个参数代表全部替换
#('a',"A",N):三个参数代表替换前面N个
print "\"abcabcabc\".replace('a',\"A\"):\t", "abcabcabc".replace('a',"A") 
print "\"hello world\".capitalize():\t", "hello world".capitalize() 

#type:  type,    int,    long,   float,  complex
#type:  str,     list,   tuple,  hex,    oct
#type:  chr,     ord 　　chr(97)返回'a'  ord('a')返回97

str1 = "1234598"
print "ord(\'1\'):\t",ord('1') 
print "ord(\'A\'):\t",ord('A') 
print "ord(\'a\'):\t",ord('a') 

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
