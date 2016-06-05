#!/usr/bin/python
#encoding=utf-8
'''
Class中有很多的特殊方法
    __init__    对象创建时被调用，用于初始化
    __del__     对象删除时被自动调用，用于收尾
    __repr__    使用repr(obj)时自动调用，返回和eval()兼容的对象字符串eval(repr(obj))
    __str__     使用str(obj)时，返回对象的字符串描述
    __cmp__     比较操作符，0相等，1大于，-1小于
    __hash__    返回一个32位的hash value，一般将对象hash后用作dictionary的key
    __nozero__  定义对象是否是逻辑假，返回0表示逻辑假，返回1表示逻辑真
    __len__     使用len(obj)时自动调用，返回对象的长度
    __getitem__ 返回self[key]用来模拟list、dictory等数据结构。
    __setitem__ 设置self[key]，模拟self[key]=value
    __delitem__ 模拟del self[key]，调用这个函数
    __contain__ 使对象像队列一样，处理in语句
    __call__    使对象像函数一样，可以调用，如obj(arg)
'''
###这是教程中的一个示例
class SchoolMember:
    def __init__(self, name, age):
        self.name=name
        self.age=age
        print "进入ScheoolMember的init"
    def tell(self):
        print 'Name:"%s", Age:"%s"'%(self.name, self.age)
class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary=salary
        print "进入Teacher的init"
    def tell(self):
        SchoolMember.tell(self)
        print 'Salary:"%d"'%self.salary
class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks=marks
        print "进入Stuent的init"
    def tell(self):
        SchoolMember.tell(self)
        print 'Marks:"%d"'%self.marks
#t=Teacher("TeacherName",40,20000)
#t.tell()
#s=Student("StudentName",22,90)
#s.tell()

###重载__setattr__实现只读属性
###在给兑现某个set值时，会自动调用__setattr__，接受的参数分别是，对象本身(self)，attribute的名字和要设定的值(value)。那么重载__setattr__就可以实现我们想要保护的属性
class A:
    readonlyValue=100
    def __setattr__(self, attr, value):
        if attr=="readonlyValue":
            raise "不能修改这个只读文件"
#a=A()
#print a.readonlyValue
#a.readonlyValue=102

###重载__getattr__实现对象组合
###实现__getattr__可以通过组合对象的方法，代替继承机制
###类继承和组合对象是面向对象的两种常用复用代码的方式，但是有一个原则：优先使用组合而不是继承
###__getattr__是最后异步，也就是说如果在自身对象或者直接间接的对象中找不到某个属性，那么就会通过__getattr__转嫁到__realobj__上了，从而实现对象的组合。
class B:
    def printMe(self):
        print 'I am B'
    def printOk(self):
        print 'B says OK'
class C:
    def printMe(self):
        print "I am C"
    def printOk(self):
        print "C says OK"
class A:
    __realobj__=B()
    def __getattr__(self, attr):
        return getattr(self.__realobj__,attr)
    def printfMe(self):
        print "I am A"
#a=A()
#a.__realobj__=B()
#a.printMe()
#a.printOk()
#a.__realobj__=C()
#a.printMe()
#a.printOk()

###利用setattr为对象动态增加attribute:
class A:
    def __init__(self, **kws):
        for k,v in kws.items():
            setattr(self, k, v)
    def DumpObj(self):
        for k,v in vars(self).items():
            print "%10s:%s"%(k,v)
#D={"one":1, "two":2, "three":3}
#a=A(five=5,six=6)
#for k,v in D.items():
#    setattr(a,k,v)
#a.DumpObj()

###对象工厂的实现：
class ObjFactory:
    def __init__(self, clsobj=None, *args, **keyargs):
        self.clsobj=clsobj and clsobj or self.__class__
        self.args=args
        self.keyargs=keyargs
    def createObj(self):
        return self.clsobj(*self.args, **self.keyargs)
class testClass:
    def __init__(self, value1, value2, *args, **keyargs):
        for k,v in keyargs.items():
            setattr(self, k, v)
        self.args = args
        self.value1= value1
        self.value2= value2
    def __len__(self):
        return len(self.args)+2
def DumpObj(self):  
        for k,v in vars(self).items():
            print "%10s:%s"%(k,v)
#f=ObjFactory(testClass, 100, 200, 300, 400, 500, one=1, two=2, three=3)        
#DumpObj(f.createObj())
#print len(f.createObj())

###创建一个线程对象，只需要类继承threading.Thread，然后在__init__里首先调用threading.Thread的__init__方法，重写类的run()方法即可
import threading
import time
class myThread(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name=threadname)
    def run(self):
        for i in range(10):
            print self.getName, i
            time.sleep(1)
#Thread1 = myThread("ThreadName1")
#myThread1.start()

###"锁"。锁对象用thread.RLock类创建，mylock=threading.RLock()
mylock=threading.RLock()
class myThread1(threading.Thread):
    var = 100
    def __init__(self, threadname):
        var = 100
        threading.Thread.__init__(self, name=threadname)
    def run(self):
        #当然，这里是不能放置修改共享数据的代码
        mylock.acquire()
        time.sleep(3)
        var = var-1;
        print "%s var is : %d"%(self.threadname,var)
        #这里可以放置修改共享数据的代码
        mylock.release()
        #当然，这里是不能放置修改共享数据的代码
for l in range(10):
    mythread11 = myThread1("thread"+str(l))
    mythread11.start()

###条件变量。用threading.Condition类创建，mycondition=threading.Condition()
###条件变量是如何工作的呢？首先一个线程成功获得一个条件变量后，调用此条件变量的wait()方法会导致这个线程释放这个锁，并进入"blocked"状态，直到另一个线程调用同一个条件变量的notify()方法来唤醒哪个进入"blocked"状态的线程。如果调用这个条件变量的notifyAll()方法就会唤醒所有的在等待的线程。


