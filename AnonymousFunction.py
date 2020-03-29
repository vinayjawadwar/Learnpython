# The function which not have any name is anonymous function
n=int(input("Enter a integer "))
f = lambda a : a*a
square = f(n)
print("square",square)


#with two values
v = lambda a,b : a+b
sum =  v(6,7)
print("sum",sum)