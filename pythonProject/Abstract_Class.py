
from abc import ABC, abstractmethod    #importing of absract class

class computer(ABC):           # abstract class /its a class wwhich has abstract methods.
    @abstractmethod                # Abstract method which has only defination.
    def process(self):
        pass

class laptop(computer):           # by using abstract class we are creating classes in a OOPS way.
    pass
    def process(self):
        print("running")


class monitor(computer):
    pass
    def process(self):
        print("running")


com2 = monitor()
com2.process()
com1 = laptop()
com1.process()