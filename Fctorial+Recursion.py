n=int(input("Enter number for getting factorial"))
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

result=fact(n)
print(result)