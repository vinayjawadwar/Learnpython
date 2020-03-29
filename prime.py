num= int(input("Enter a integer"))

for i in range(2,num):
    if num % i ==0:
        print("Not prime")
        break

else:
    print("prime")