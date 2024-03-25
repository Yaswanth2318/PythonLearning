
# By Comparing two classes we can kow what is multi Threading.//

# Sleep() : gives us how much need in between classes need to execute.//

# for run Method  : we can use .start object // we can see this in the program..


# Here How many Threads?
# Three : Main Thread, Hello Thread and Hi thread.

from threading import *
from time import sleep
class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

class Hi(Thread):

    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)      # Gives 1 sec gap for Output of  two classes

t1 = Hello()  # Object creates with Class
t2 = Hi()

t1.start() # for printing method.
sleep(0.2)      # having two classes prints output in a 0.2 sec gap
t2.start()



t1.join()    #  belongs to Main Thread So ask main thread print after execution of hello and hi thread.
t2.join()
print("bye")   # "bye" belongs to Main Thread So ask main thread print after execution of hello and hi thread.
