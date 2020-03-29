class Computer():

    def config(self):
        print("i3, 4g , 1tb")

x=9
print(type(x))

y='7'
print(type(y))

com1 = Computer()
com2 = Computer()

print(type(com1))

#  call config()

Computer.config(com1)
Computer.config(com2)                       #when more than one object

com1.config()
com2.config()                             # Here com2 get as argument of class

a=5
print(a.bit_length())