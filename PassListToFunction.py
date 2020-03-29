def count(list):
    even = 0
    odd = 0
    for i in list:
        if i%2==0:
            even+=1
        elif i%2!=0:
            odd+=1
    return even,odd


list = [20,11,15,14,48,66,7]
even , odd = count(list)

print(even)
print(odd)
print("Even: {} and Odd : {} ".format(even,odd))