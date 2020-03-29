x=int(input("How many candies you have?"))
av=10
i=1
while i<=x:
    if i>av:
        print("candies are out of stock")
        break
    print("candy")
    i+=1

print("thank you")


for i in range(1,20):
    if i%2==0:
        continue
    print(i)
print("bye")




for i in range (1,20):
    if i%2!=0:
        pass
    else:
        print("even",i)

