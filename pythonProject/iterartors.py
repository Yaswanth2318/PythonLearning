# nums = [12,3,4,56]
#
# # for i in nums:
# #     print(i)
#
#
# it = iter(nums)        # iterator creation  give the object of iterator
# print(it.__next__())  # one method of print iterator     #gives the next object in the iterator
#
# print(next(it))       # another way
#
# for i in it:
#     print(i)

#iter and next Concept
class Top:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):            
        if self.num <=20:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration

values = Top()

for i in values:
    print(i)







