def add(a,b):              #formal argument a,b
    c=a+b
    print(c)

add(10,45)               # actual argument 10,45   we are actualy passing values



def person(name,age):
    print(name)
    print(age)
person("vinay",20)               # Here we know sequence



def person(name,age):
    print(name)
    print(age)
person(20,"vinay")               # Here we don't know sequence not able to perform more operations like below




#if we don't know the sequence so use keywords
def person(name,age):
    print(name)
    print(age-5)             # it run
person(age=20,name='vinay')



def person(name,age=18):
    print(name)
    print(age)
person('vinay')              # if we don't have default value 18 it will get error


#variable length argument
#if user dosn't known about length so give *b means multiple values
def sum(*b):
    c=0
    for i in b:
        c=c+i
    print(c)

sum(4,6,7,5)