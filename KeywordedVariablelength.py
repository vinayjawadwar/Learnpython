def person(name,*data):
    print(name)
    print(data)

person("vinay",20,'NANDED',7894564224)              #which data is for what don't know so we use keywords


def person(name,**data):                   # one star for data and other star for keywords which are not defined
    print(name)
    print(data)
person("vinay",age=20,city='NANDED',mob=7894564224)


# use for loop for data
def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)                                     #i,j are key and value pair
person("vinay",age=20,city='NANDED',mob=7894564224)
