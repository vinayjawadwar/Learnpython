def topten():

    yield 5

value = topten()
print(value)
print(value.__next__())

def vinay():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

value2 = vinay()

print(value2)

print(value2.__next__())
print(value2.__next__())


print("for loop to print all the values")
for i in value2:
    print(i)


def vinay2():
    n = 1
    while n<=10:
        sq = n*n
        yield sq                 # yield give next next value till 10
        n +=1

value3 = vinay2()
print("print to ten square")
for i in value3:
    print(i)
