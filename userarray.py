from array import*
arr = array('i',[])

n=int(input("Enter length of array"))

for i in range(n):
    x= int(input("Enter a value"))
    arr.append(x)
print(arr)

val=int(input("Enter the value for search"))

k=0
for j in arr:
    if j==val:
        print(k)
        break
    k+=1

print(arr.index(val))