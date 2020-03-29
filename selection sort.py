
def sort(array):
    for i in range(len(array)):
        minpos=i

        for j in range(i,len(array)):
            if array[j]<array[minpos]:
                minpos=j


        temp =array[i]
        array[i] = array[minpos]
        array[minpos] = temp
        print(array)

array= list()
n=int(input("enter lenght of array want to insert"))
print("enter numbers in array")
for i in range(n):
    n = input("num: ")
    array.append(n)

sort(array)
print(array)