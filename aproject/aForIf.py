#!/usr/bin/python

def fun():
    return 0;

sum = 0
for x in range(1,101):
    sum += x;
print(sum)

for x in range(1,10,2):
    print str(x)+"kkk"

for x in [1,2,3,4]:
    print str(x)+" hello world"

for x in {"ab", "cb", "ef"}:
    print x + "hello"


x = int(raw_input("input: "))
y = int(raw_input("input: "))

if x >= 90:
    if y >= 90:
        print "A"
    else:
        print "AB"
    print "KKKKKKK"
elif x >= 80 and y >= 80:
    print 'B'
elif x >= 70:
    print 'C'
elif x >= 60:
    print 'D'
else:
    print "E"
