# a light weight process when you breakdown a beg task into small part that each task called thred

# simple code

class Hello:
    def run(self):
        for i in range(0,5):
            print("hello")

class Hi:
    def run(self):
        for i in range(5):
            print("hi")

t1 = Hello()
t2= Hi()

t1.run()
t2.run()


print("=========using thread=====================")
from threading import *

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("hello")

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("hi")


t1 = Hello()
t2= Hi()

t1.start()
t2.start()                   #it is very fast or small program so it didn't take gap between hi & hello

print("=========printing alternating=====================")

from time import sleep
from threading import *

class Hello(Thread):
    def run(self):
        for i in range(3):
            print("hello")
            sleep(1)                   # it is sleep or stop for 1 sec and then execute next

class Hi(Thread):
    def run(self):
        for i in range(3):
            print("hi")
            sleep(1)                           # it is sleep or stop for 1 sec and then execute next

t1 = Hello()
t2= Hi()

t1.start()
t2.start()                   # here get hellohi because we get same thread at same time  parallel soooo



print("=========printing alternating=====================")

from time import sleep
from threading import *

class Hello(Thread):
    def run(self):
        for i in range(3):
            print("hello")
            sleep(1)                   # it is sleep or stop for 1 sec and then execute next

class Hi(Thread):
    def run(self):
        for i in range(3):
            print("hi")
            sleep(1)                           # it is sleep or stop for 1 sec and then execute next

t1 = Hello()
t2= Hi()

t1.start()
sleep(0.2)
t2.start()

t1.join()
t2.join()

print("Bye")