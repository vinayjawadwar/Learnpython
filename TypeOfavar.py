class Car:
    wheels= 4                                  # define var outside ___init___& in class called class var(namespace)
    def __init__(self):
        self.mil = 10                 # define var in __init__ is instance var (namespace)
        self.com = 'BMW'

c1 = Car()
c2 = Car()

Car.wheels = 5                     # change class namespace ( affect all the objects)

print(c1.com , c1.mil ,c1.wheels)
print(c2.com , c2.mil , c2.wheels)          # get same values

c1.mil = 8
c1.com = "Audi"
print(c1.com , c1.mil ,c1.wheels)
