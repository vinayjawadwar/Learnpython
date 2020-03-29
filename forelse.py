nums=[12,15,4,16,85,11]

for i in nums:

    if i%5==0:
        print(i)
    else:
        print(i,"not divisible by 5")




nums=[12,14,4,16,84,11]
for i in nums:
    if i%5==0:
        print(i)
        break
else:
    print("not found")