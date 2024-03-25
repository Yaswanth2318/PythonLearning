class student:

     def __init__(self):
         self.name = 'Yash'
         self.id = 1
         self.lap = self.laptop()     #inner class object/Constructor.
     def show(self):
         print(self.name,self.id)
         self.lap.show()        #inner class method shown here to print
     class laptop:    #inner class

        def __init__(self):
            self.brand = 'mac'
            self.cpu = 'm1pro chip'
            self.ram = 16

        def show(self):
            print(self.brand,self.cpu,self.ram)



s1 = student()
s2 = student()
s1.show()
s2.show()

# print(s1.name,s1.id)
# print(s2.name,s2.id)