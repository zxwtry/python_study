#!usr/bin/python

a = ("a", "b", "c")
s = {1:111, 5:555, 4:444, 3:333, 2:222}
for k,v in s.items():
    print str(k)+" "+str(v)
else:
    print "ending"




for x in range( len(a) ):
    print a[x]
for x in s:
    print x
