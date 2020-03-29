
def is_even(n):
    return n%2==0

nums = [4,5,8,71,11,44,66]

even = list(filter(is_even,nums))

print(even)


# using anonymous
nums = [4,5,8,71,11,44,66]
even = list(filter(lambda n : n%2==0 ,nums))                 #filtering the value which satisfy
print(even)

from functools import reduce                           # functools used for function reduce
doubles = list(map(lambda n: n*2,even))                   # map is for change values
print("doubles",doubles)

sum= reduce(lambda a,b : a+b , doubles)
print(sum)
