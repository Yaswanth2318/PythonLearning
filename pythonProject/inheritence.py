# Constructor in inheritance

class A:

     def __init__(self):                  #Construtor1
         print("in A init")
     def feature1(self):
         print("feature1 is working")

     def feature2(self):
         print("feature2 is working")


class B:                                 #Constructor2 # How Constructor Behaves?
                                            # First it checks the Constructor in Existing(or) Class or Sub class then it go to Super() Class.

    def __init__(self):
        print("in B init")

    def feature3(self):
        print("feature3 is working")

    def feature4(self):
        print("feature4 is working")



class C(A,B):
    def __init__(self):
        super().__init__()               # super() for getting Constructor from Classes
                                            # print "A" Class because while we call Super() because of MRO
        print("in C init")                      # Method Resolution Order(Left to Right).

    def feature5(self):
        print("feature5 is working")

    def feature6(self):
        print("feature6 is working")

    def feature(self):                 # We can use Super() class in Normal Method not only in Constructor Method.
        super().feature1()

c1 = C()
c1.feature()
