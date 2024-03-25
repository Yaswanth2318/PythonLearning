
# a = '3'
# b = '7'
#
# print(str.__add__(a,b))

# Method OverRiding
class A:
    def show(self):
        print("In a Show")


class B(A):
    def show(self):
        print("In B Show")


a1 = B()
a1.show()