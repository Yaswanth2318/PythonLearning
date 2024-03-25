# Duck Typing implementation

class pycharm:         #ide
    def execute(self):                      # here Duck(Bird) is execute(every this to execution)
        print("Compiling")
        print("Running")


class MyEditor:         #ide

    def execute(self):
        print("Convention Check")
        print("Spell Check")
        print("Compiling")
        print("Running")


class laptop:

    def code(self,ide):           # method : Code  and defined ide
        ide.execute()                           # Here If class has execute method is enough to execute the class
                                                #  ...laptop is called Duck Typing.(like interfaces).

ide = pycharm()


lap1 = laptop()
lap1.code(ide)


