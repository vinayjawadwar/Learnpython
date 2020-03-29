
a=10                                #global varialble
def something():
    a=15                          #local variable
    print("inside",a)
something()
print("outside",a)





a=10                                #global varialble   it also work as local variable when it was not present
def something():
    print("inside",a)
something()
print("outside",a)



# updating global variable
a=10
def something():
    global a
    a=15
    print("inside",a)
something()
print("outside",a)



# we want local variable with changing global variable
a=10
def something():
    a=9
    x= globals()['a']                     #return all global var
    print(id(x))
    print("inside",a)
    globals()['a']=15
something()
print("outside",a)


