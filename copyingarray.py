from numpy import *
arr = array([1,2,3,4,5])
arr = arr+5
print(arr)


from numpy import *
arr1= array([1,2,3,4,5])
arr2= array([4,5,6,7,8])
arr=arr1+arr2
print(arr)


from numpy import *

arr1= array([1,2,4,6,7])
print(sin(arr1))
print(cos(arr1))
print(log(arr1))
print(sqrt(arr1))
print(sum(arr1))
print(min(arr1))
print(max(arr1))
print(sort(arr1))



from numpy import *
arr1= array([1,2,3,4,5])
arr2= array([4,5,6,7,8])
print(concatenate([arr1,arr2]))



from numpy import *
arr1 = array([8,9,8,5,5])

arr2=arr1              # copying array

print(arr1)
print(arr2)            # get same values

print(id(arr2))
print(id(arr1))        # But get same address they are pointing and storing at same address  called Aliasing



from numpy import *
arr1 = array([8,9,8,5,5])
arr2 = arr1.view()     #create view and at diff address

arr1 [1]=7            # modify in both  so it is shallow copy
print(arr1)
print(arr2)


from numpy import *
arr1 = array([8,9,8,5,5])
arr2 = arr1.copy()              # now this is deap copy
arr1 [1]=7            # modify in only arr1 so it is deap  copy
print(arr1)
print(arr2)