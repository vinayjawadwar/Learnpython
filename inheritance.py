class A:
    def feature1(self):
        print("feature 1 is working")

    def feature2(self):
        print("feature 2 is working")

class B(A):                                # B is child(sub) class of A that B inheriting(access) features from A
     def feature3(self):
        print("feature 3 is working")

     def feature4(self):
            print("feature 4 is working")

class C():                             # C is child(sub) class of B then also A that C inheriting features from both A & B
    def feature5(self):
        print("feature 5 is working")

class D(A,C):                               # multiple inheritance so access feature of A ,C
    def feature6(self):
     print("feature 6 is working")

a1 = A()

a1.feature1()
a1.feature2()

b1 = B()

b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()


c1 = C()

c1.feature5()

d1 = D()

d1.feature1()
d1.feature2()
d1.feature5()
d1.feature6()