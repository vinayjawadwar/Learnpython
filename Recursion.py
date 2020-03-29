
#def greet():
        # print("Hello")
       #  greet()                      #recursion means again greet calling greet() and it is infinite

# greet()                             #give error




# how to increase limit

import sys
sys.setrecursionlimit(200)
print(sys.getrecursionlimit())
i=0
def greet():
    global i
    i+=1
    print("Hello",i)
    greet()

greet()
