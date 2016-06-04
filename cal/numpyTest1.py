#!/usr/bin/python
#encoding=utf-8
'''
1,  numpy是什么
    numpy是Python的一个科学计算的库，提供了矩阵运算的功能，其一般与Scipy、matplotlib一起使用。骑士，list已经提供了类似于矩阵的表示形式，不过numpy提供了更多函数。
'''

###总是先导入numpy
import numpy
print numpy.version.version #输出1.8.2

###多维数组
###多维数组的类型是：numpy.ndarray
###使用numpy.array方法
###以list或tuple变量为参数产生一维数组：
var1 = numpy.array([1,2.2,3,4])
print var1          #[ 1.   2.2  3.   4. ]
print type(var1)    #<type 'numpy.ndarray'>

###生成数组的时候，可以指定数据类型，例如numpy.int32, numpy.int16, numpy.float64等等
var2 = numpy.array([1,2.2,3,4],dtype=numpy.int32)
print var2          #[1 2 3 4]

###使用numpy.arange方法
var3 = numpy.arange(6)
print var3          #[0 1 2 3 4 5]
print type(var3)    #<type 'numpy.ndarray'>
print numpy.arange(15).reshape(3,5)
                    # [[ 0  1  2  3  4]
                    #  [ 5  6  7  8  9]
                    #  [10 11 12 13 14]]

###使用numpy.linspace方法
###例如，在从1到3产生9个数
var4 = numpy.linspace(1,3,9)
print var4          #[ 1.    1.25  1.5   1.75  2.    2.25  2.5   2.75  3.  ]
var5 = numpy.linspace(1,3,10)
print var5          #[ 1.          1.22222222  1.44444444  1.66666667  1.88888889  2.11111111  2.33333333  2.55555556  2.77777778  3.        ]

###使用numpy.zeros, numpy.ones, numpy.eye等方法可以构造特定的矩阵
var6 = numpy.zeros((3,4))
print var6          #[[ 0.  0.  0.  0.]
                    # [ 0.  0.  0.  0.]
                    # [ 0.  0.  0.  0.]]
var7 = numpy.ones((3,4),dtype=numpy.int32)
print var7          #[[1 1 1 1]
                    # [1 1 1 1]
                    # [1 1 1 1]]
var8 = numpy.eye(3)
print var8          #[[ 1.  0.  0.]
                    # [ 0.  1.  0.]
                    # [ 0.  0.  1.]]
#数组的维数
print var6.ndim     #2
print var7.ndim     #2
print var8.ndim     #2
#数组每一维的维数
print var6.shape    #(3,4)
print var7.shape    #(3,4)
print var8.shape    #(3,3)
#数组中元素的总个数
print var6.size     #12
print var7.size     #12
print var8.size     #9
#元素的类型
print var6.dtype    #float64
print var7.dtype    #int32
print var8.dtype    #float64
#每个元素所占字节数
print var6.itemsize #8
print var7.itemsize #4
print var8.itemsize #8

###for操作
for x in numpy.linspace(1,3,3):
    print x         #1.0
                    #2.0
                    #3.0

###数组的加减乘除
###一句话，元素的操作，行数相同&列数相同，才能操作
print var6+var7
print var6-var7
print var6*var7
print var6/var7

###数组对象自带的方法
print var6.sum()    #0.0
print var7.sum()    #12
print var8.sum()    #3.0
print var6.sum(axis=0)
                    #[ 0.  0.  0.  0.]
print var7.sum(axis=0)
                    #[3 3 3 3]
print var8.sum(axis=0)
                    #[ 1.  1.  1.]
print var6.min()
print var6.max()

###使用numpy下的方法
print numpy.sin(var6)
print numpy.sin(var7)
#floor 返回的不一定是整数，浮点小数部分是0
print numpy.floor(numpy.sin(var7)*4)
print numpy.floor(numpy.exp(var7))
#矩阵的乘法，矩阵乘法规则
print numpy.dot(var8,var8)

###合并数组
###使用numpy下的vstack和hstack函数
###使用的是深拷贝
print numpy.vstack((var6,var7))
print numpy.hstack((var6,var7))

###深拷贝和浅拷贝
###数组对象自带了深拷贝和浅拷贝的方法
var9 = var6.copy()
var0 = var6
var1 = var6[:]
var6[0,1]=99
print var6
print var9          #只有var9是深拷贝
print var0
print var1
#如果引入copy包
#var9=copy.deepcopy(var6) 深拷贝
#var0=copy.copy(var6)     浅拷贝
#浅复制还有一个view
varView = var6.view()
                    #varView就是var6的一个view，属于var6
print varView is var6
                    #False
print varView.base is var6
                    #True
print varView.flags.owndata
                    #False 

###基本的矩阵运算
#转置
print var6
print var6.transpose()
#迹(对角线上所有元素的和)
print var6.trace()
#在numpy.linalg模块中有更多矩阵运算的方法
import numpy.linalg
print numpy.linalg.eig(var8)
                    #特征值和特征向量

###按照行,列进行相加
print var6
print var6.sum(axis=0)
                    #axis=0 选择第0行向下加一直加到最后一行 
                    #就是干掉0维下标
print var6.sum(axis=1)
                    #axis=1 选择第0列向右加一直加到最后一列
                    #就是干掉1维下标
print var6
print var6.cumsum(axis=0)
                    #axis=0 选择第0行向下加，加一次，保存一次
print var6.cumsum(axis=1)
                    #axis=1 选择第0列向右加，加一次，保存一次
