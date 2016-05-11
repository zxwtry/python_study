#!/usr/bin/python
import time

x = ''
while x != "q":
    print "hello"
    time.sleep(1)
    x=raw_input("input : ");
    if x == "K":
        break
else:
    print "end"
while x != "q":
    print "hello"
    time.sleep(1)
    x=raw_input("input : ");
    if not x:
        print "blank"
        break
    if x == 'A':
        break
while True:
    print "hello"
    time.sleep(1)
    x=raw_input("input : ");
    if x == 'A':
        break;
for x in range(1,11):
    print x
    if x == 2:
        print "This is in 2"
        continue;
    if x == 3:
        pass
    if x == 5:
        exit()
    if x == 6:
        break
    print "#"*x

for x in range(20):
    print x
    time.sleep(1)
else:
    print "ending"
