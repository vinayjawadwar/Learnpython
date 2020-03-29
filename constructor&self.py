class Computer():
    def __init__(self):
        self.name = "vinay"
        self.age = 20

    def update(self):
        self.age=20

    def compair(self,other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = Computer()                   # constructor is allocate memory to object  here Computer() is constructor
c2 = Computer()

if c1.compair(c2):
    print("They are same")              # if age are diff we get they are diff
else:
    print("They are diff")

print(id(c1))
print(id(c2))

print(c1.name)
print(c2.name)              # print same data
print(c2.age)

c1.name =  "vaibhav"
c1.age = 18

print(c1.name)


c1.update()              # change age of vaibhav because we write c1.function()

print("updated",c1.age)



