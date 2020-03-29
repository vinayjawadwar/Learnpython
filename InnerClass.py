class Student:

    def  __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name ,self.rollno)
        self.lap.show()


    class Laptop:                                 #inner class
        def __init__(self):
            self.brand = 'Lenovo'
            self.cpu = ' i3'
            self.ram = 4

        def show(self):
            print(self.brand ,self.cpu, self.ram)

s1 = Student("vinay", 2)
s2 = Student("vaibhav" , 3)

s1.show()

lap1 = s1.lap
lap2 = s2.lap

print(id(lap1))
print(id(lap2))



lap1 = Student.Laptop()

