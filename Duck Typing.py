class Pycharm:
    def execute(self):
        print("editor")
        print("compiler")

class Myeditor:

    def execute(self):
        print("spelcheck")
        print("convention check")
        print("editor")
        print("compiler")

class Laptop:
    def code(self,ide):
         ide.execute()

ide = Pycharm()

lap1= Laptop()
lap1.code(ide)

ide = Myeditor()

lap1= Laptop()
lap1.code(ide)
