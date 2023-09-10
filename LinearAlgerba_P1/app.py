import numpy as numpy
import matplotlib.pyplot   as pyplot
import numpy.linalg.linalg as LA

def create_D(n):
    D=numpy.eye(n-1,n)#D is a (n-1)*m Matrix
    D = -numpy.roll(D,1)
    D = D +numpy.eye(n-1,n) 
    #now D is 
    #1  -1   0   0
    #0   1  -1   0
    #0   0   1  -1
    print(D)
    return  D

def create_b(n,data):
    _b=data.reshape((n,1))# _b is a vector just contains original data
    temp=numpy.zeros((n-1,1))# temp is (n-1)*n zero matix 
    b=numpy.vstack((_b,temp))# b is a (2n-1)*n matrix
    print(b)
    return  b

def create_A(n, D, landa):
    A=numpy.vstack((numpy.eye(n),landa*D))# a is a (2n-1)-n matrix
    print(A)
    return  A

def solve(data, landa):
    n = len(data);
    D = create_D(n)
    b = create_b(n, data)
    A = create_A(n, D, landa)
    #https://textbooks.math.gatech.edu/ila/least-squares.html
    at = LA.transpose(A)
    ata_1 =LA.inv( numpy.matmul(at,A))
    ata_1 =numpy.matmul(ata_1,at)
    ata_1 =numpy.matmul(ata_1,b)
    print(ata_1)
    return  ata_1




data = numpy.load("btc_price.npy" )#[:1000]
res1000 = solve(data, 1000)
res100 = solve(data, 100)
res10 = solve(data, 10)
res2 = solve(data, 10)
###############
pyplot.plot(res1000,'r',linewidth=3,label='landa = 1000')
pyplot.plot(res100,'g',linewidth=3,label='landa = 100')
pyplot.plot(res10,'c',linewidth=3,label='landa = 10')
pyplot.plot(res2,'b',linewidth=3,label='landa = 2')
pyplot.plot(data,'k',linewidth=1,label='data')
pyplot.legend()
pyplot.show()











