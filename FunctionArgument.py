def update(x):
    x=8
    print(x)              # 10 update to 8
update(10)



def update(x):
    x=8
    print("x",x)
a=10
update(a)                  # here pass by value 10 not by reference a
print("a",a)


def update(x):
    print(id(x))                      # referce to same address  because pass by value
    x=8
    print(id(x))                 # after changing value of x get diff address because int , str are imutable
    print("x",x)
a=10
print(id(a))
update(a)
print("a",a)

# In python we does't use pass by value or pass by reference none of them.


#mutable
def update(list):
    print(id(list))
    list[1]=25
    print(id(list))                 # after updating also address do not change so list is mutable
    print("x",list)

list=[10,20,30]
print(id(list))
update(list)                           
print("list",list)



