from numpy import *

arr = array([
            [1,2,3,4]
            [5,6,7,8]
            ])

print(arr.dtype)   #Get type of data
print(arr.ndim)    #Get how many dimention array have
print(arr.shape)   #Get no. of columns and rows in array
print(arr.size)    #give siza ex.6



# convert 2d array to 1d array
from numpy import *
arr = array([
            [1,2,3,4]
            [5,6,7,8]
            ])
arr1 = arr.flatten()
print(arr1)


# convert 2d to 3d
from numpy import *
arr = array([
            [1,2,3,4,8,9]
            [5,6,7,8,4,2]
            ])
arr1 = arr.reshape(3,4)            # 3 rows and 4 columns for modify 2d

arr2 = arr.reshape(2,2,3)         # 2*2*3=12
print(arr1)     # Get modified 2d array

print(arr2)     # Get 1 big 3d array in which we get two 2d array each 2d array have two 1d array and each 1d array have 3 elements



# formation of matrix for performing more operations
from numpy import *
arr = array([
            [1,2,3,4]
            [5,6,7,8]
            ])
m= matrix(arr)
print(m)          # output looks similar but able to perform more function with m

#other way
m1= matrix('1 2 3 4; 5 6 7 8 ')     # 2 rows and 4 columns
print(m1)
print(diagonal(m1))               #get only digonal elements
print(m1.min())
print(m1.max())

m2= matrix('1 2 ;3 4; 5 6; 7 8 ')   #4 rows and 2 colums
print(m2)


# multiplication of matrices
from numpy import *
m1= matrix('1 2 3 4; 5 6 7 8 ')
m2= matrix('1 9 3 8; 2 6 7 8 ')

m3 = m1+m2
print(m3)

m4= m1*m2
print(m4)

