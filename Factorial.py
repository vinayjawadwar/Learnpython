
n= int(input("Enter value to get factorial of that number"))

def fact(n):
    f=1
    for i in range(1,n+1):
       f=f*i
    return f

print(fact(n))