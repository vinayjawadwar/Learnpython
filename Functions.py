def greet():
    print("Hello")
    print("Good morning")

def add(x,y):
    c=x+y
    print(c)

greet()
add(5,7)


def sum(x,y):
    a=x+y
    return a

result = sum(54,77)
print(result)



def add_sub(x,y):
    a=x+y
    b=x-y
    return a,b

result1,result2 = add_sub(54,11)

print(result1,result2)

