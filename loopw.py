x=int(input("enter how many times you want to print your name"))
name = input("enter your name")

i=1
while i<=x:
    print(name ,end="")

    j = 3
    while j>=1:
        print("Rocks ",end="")
        j-=1
    i += 1
    print()