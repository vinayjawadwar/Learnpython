from numpy import *
arr = array([1,2,1,3])
print(arr)



from numpy import *
arr = array([1,2,1,3],int)
print(arr)


from  numpy import*
arr= linspace(0,15,16)    #0 to 15 with 16 parts
print(arr)

from numpy import*
arr=arange(1,15,2)      # 1 to 15 with diff 2
print(arr)


from numpy import *
arr=logspace(1,40,5)
print(arr)

from numpy import *
arr = logspace(1,40,5)     #first and last value are log to base 10 and middle are remaining parts
print('%.2f' %arr[4])

from numpy import *
arr = zeros(5)           #array of length 5 with all 0 value in float
print(arr)


from numpy import *
arr = ones(5)           #array of length 5 with all 1 value in float
print(arr)


from numpy import *
arr = ones(5,int)           #array of length 5 with all 1 value in int
print(arr)
