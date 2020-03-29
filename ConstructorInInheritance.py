class A:
    def __init__(self):
        print("in init of A")
    def feature1(self):
        print("feature 1 is working")

    def feature2(self):
        print("feature 2 is working")

class B:                                             # B is subclass which access all features from superclass but not vise versa

    def __init__(self):                                 # if init of B is not present then it print init of A
        print("in init of B")
        super().__init__()                     # this function print init of super class A

    def feature3(self):
        print("feature 3 is working")

    def feature4(self):
            print("feature 4 is working")


class C(A,B):                               # now C has two superclass
    def __init__(self):
        print("in init of C")
        super().__init__()                     # But it print only one because it prefer left one if it not present thrn print right B

    def feat(self):
        super().feature2()
        
a1 = A()
c1 = C()

a1.feature1()
c1.feat()