class Computer():
    def __init__(self,cpu,ram):      #special variable
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("config is ", self.cpu ,self.ram)


com1 = Computer("i5",16)                         # here we have default com1 in Computer(com1,cpu,ram)
com2 = Computer("Ryzon 3",8)


com1.config()
com2.config()

