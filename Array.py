# import array
# array.array('i',[5,4,3,2,1])


# import array as arr
# arr.array('i',[5,4,3,2,1])


from array import*
values= array('i',[5,4,3,2,1])
print(values)
print(values.buffer_info())    #Gives address and size

from array import*
values= array('i',[5,4,3,2,1])
values.reverse()
print(values)

from array import*
values= array('i',[5,4,3,2,1])
print(values[1:4])


from array import*
values= array('i',[5,4,3,2,1])
for i in range(5):
    print(values[i])


from array import*
values= array('i',[5,4,-3,2,1])   # 'i' for int
for i in range(len(values)):
    print(values[i])


from array import*
values= array('u',['a','e','i','o','u'])     #'u' for string
for i in range(len(values)):
    print(values[i])


from array import*
values= array('i',[5,4,-3,2,1])   # 'i' for int
newArr = array(values.typecode, (a  for a in values))
for i in newArr:
    print(i)


from array import*
values= array('i',[5,4,-3,2,1])   # 'i' for int
newArr = array(values.typecode, (a*a  for a in values))
for i in newArr:
    print(i)



from array import*
values= array('i',[5,4,-3,2,1])   # 'i' for int
newArr = array(values.typecode, (a*a  for a in values))
i=0

while i<len(newArr):
    print(newArr[i])
    i+=1