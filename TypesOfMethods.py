# Types of Method

  #1 instance method
  #2 class methods
  #3 static method


class Student:

    school = 'MGM'

    def __init__(self,m1,m2,m3):                       # instance method--> use self keyword
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return ( self.m1 + self.m2 +self.m3 )/3

    def get_m1(self):      #fetch the value(not change the value)  --> accesors  to fetch the value of m1 use  its not have compulsion to have get method
        return  self.m1
    def set_m1(self,value):                      # set value(change the value) --> mutetors
        self.m1 = value              # similar for all m2 , m3

s1 = Student(34,35,36)
s2 = Student(31,32,33)

print(s1.avg())
print(s2.avg())




#class method

class Student:

    school = 'MGM'                           # use class object

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    @classmethod                             #for use info() as classmethod
    def getschoolname(cls):                              # in class method use cls keyword
        return cls.school

    @staticmethod                                  # static method
    def info():                                              # static works with not any variable use to do extra with our class
        print("This is student class.. in abc module")

s1 = Student(34,35,36)
s2 = Student(31,32,33)

print(Student.getschoolname())

Student.info()