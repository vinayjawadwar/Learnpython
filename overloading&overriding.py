# method overloading

class Student:

    def __init__(self,m1,m2):
        self.m1  = m1
        self.m2 = m2

    def sum(self,a=None,b=None,c=None):
         s = 0
         if a!=None and b!=None and c!=None:
             s = a+b+c
         elif a!=None and b!=None:
             s=a+b
         else:
             s =a
         return s


s1 = Student(57,77)
s2 = Student(68,75)

print(s1.sum(64,5,44))
print(s1.sum(64,5))
print(s1.sum(44))


# method overriding

class A:
    def show(self):
        print("in A show")


class B(A):
    def show(self):                      # if here is not show function then it overrides show function of A
        print("in B show")



a1 = A()
a1.show()


b1 = B()
b1.show()