def div(a,b):
    if a>b:
        return a/b
    else:
        return b/a

print(div(15,45))


#Using decorator
def div(a,b):
    print(a/b)

def smart(function):                       # takes function as parameter only possible in pyhon
    def inner(a,b):
        if a<b:
            a,b = b,a
        return  function(a,b)
    return inner
div = smart(div)
div(2,4)